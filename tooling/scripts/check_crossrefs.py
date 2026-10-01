#!/usr/bin/env python3
"""Lightweight manuscript structure and cross-reference checks.

This is intentionally modest: Quarto remains the authoritative renderer, while this
script catches common repo-hygiene errors before a full render.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:  # pragma: no cover - dependency check should catch this first
    yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[2]
QUARTO = ROOT / "_quarto.yml"
REF_PREFIXES = ("fig", "tbl", "eq", "sec", "lst", "thm", "lem", "cor", "prp", "exm", "def")

INCLUDE_RE = re.compile(r"\{\{<\s+include\s+([^\s>]+)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
ID_RE = re.compile(r"\{#([A-Za-z][A-Za-z0-9_-]*)")
REF_RE = re.compile(r"(?<![\w.-])@((?:" + "|".join(REF_PREFIXES) + r")-[A-Za-z0-9_-]+)")


class CheckFailure(RuntimeError):
    pass


def load_quarto() -> dict:
    if yaml is None:
        raise CheckFailure("PyYAML is required to read _quarto.yml")
    if not QUARTO.exists():
        raise CheckFailure("missing _quarto.yml")
    data = yaml.safe_load(QUARTO.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise CheckFailure("_quarto.yml did not parse as a mapping")
    return data


def iter_book_chapters(items: list | None) -> list[str]:
    out: list[str] = []
    for item in items or []:
        if isinstance(item, str):
            out.append(item)
        elif isinstance(item, dict):
            part = item.get("part", "")
            if isinstance(part, str) and part.endswith((".qmd", ".md")):
                out.append(part)
            out.extend(iter_book_chapters(item.get("chapters")))
    return out


def declared_files(config: dict) -> list[Path]:
    # Quarto books derive project.render from these book entries. Do not maintain
    # another chapter list or scan every QMD (which would promote candidates).
    book = config.get("book", {})
    paths = iter_book_chapters(book.get("chapters"))
    if book.get("references"):
        paths.append(book["references"])
    paths.extend(iter_book_chapters(book.get("appendices")))

    seen: set[Path] = set()
    out: list[Path] = []
    for raw in paths:
        p = (ROOT / raw).resolve()
        if p not in seen:
            out.append(p)
            seen.add(p)
    return out


def link_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<"):
        return raw[1:].split(">", 1)[0]
    return raw.split(None, 1)[0].strip('"\'') if raw else ""


def resolve_relative(raw: str, source: Path) -> Path | None:
    cleaned = link_target(raw)
    parsed = urlsplit(cleaned)
    if not cleaned or parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path = unquote(parsed.path)
    return ((ROOT / path.lstrip("/")) if path.startswith("/")
            else source.parent / path).resolve()


def display(path: Path) -> str:
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def manuscript_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    # Ignore literal examples, while leaving ordinary math and Quarto divs intact.
    return re.sub(r"^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text, flags=re.M | re.S)


def collect_qmd_tree(start_files: list[Path]) -> tuple[set[Path], list[str]]:
    seen: set[Path] = set()
    errors: list[str] = []
    stack = list(start_files)
    while stack:
        path = stack.pop()
        if path in seen:
            continue
        seen.add(path)
        if not path.is_relative_to(ROOT):
            errors.append(f"include escapes project root: {display(path)}")
            continue
        if not path.exists():
            errors.append(f"missing declared/include file: {display(path)}")
            continue
        if path.suffix.lower() not in {".qmd", ".md"}:
            continue
        text = manuscript_text(path)
        for match in INCLUDE_RE.finditer(text):
            resolved = resolve_relative(match.group(1), path)
            if resolved is not None:
                stack.append(resolved)
    return seen, errors


def check_assets(files: set[Path]) -> list[str]:
    errors: list[str] = []
    for path in sorted(files):
        if not path.is_relative_to(ROOT) or not path.exists() or path.suffix.lower() not in {".qmd", ".md"}:
            continue
        text = manuscript_text(path)
        for match in IMAGE_RE.finditer(text):
            target = resolve_relative(match.group(1), path)
            if target is not None and not target.exists():
                errors.append(
                    f"missing image asset in {path.relative_to(ROOT)}: {match.group(1)}"
                )
    return errors


def check_refs(files: set[Path]) -> list[str]:
    ids: dict[str, list[Path]] = defaultdict(list)
    refs: dict[str, list[Path]] = {}
    for path in files:
        if not path.is_relative_to(ROOT) or not path.exists() or path.suffix.lower() not in {".qmd", ".md"}:
            continue
        text = manuscript_text(path)
        for label in ID_RE.findall(text):
            ids[label].append(path)
        for ref in REF_RE.findall(text):
            refs.setdefault(ref, []).append(path)

    errors: list[str] = []
    for label, locations in sorted(ids.items()):
        if len(locations) > 1:
            errors.append(f"duplicate explicit ID #{label} in " + ", ".join(display(p) for p in locations))
    for ref, locations in sorted(refs.items()):
        if ref not in ids:
            where = ", ".join(str(p.relative_to(ROOT)) for p in locations[:3])
            errors.append(f"unresolved cross-reference @{ref} in {where}")
    return errors


def check_links(files: set[Path]) -> list[str]:
    errors: list[str] = []
    target_ids: dict[Path, set[str]] = {}
    for source in sorted(files):
        if not source.is_relative_to(ROOT) or not source.is_file() or source.suffix not in {".qmd", ".md"}:
            continue
        for raw in LINK_RE.findall(manuscript_text(source)):
            target = resolve_relative(raw, source)
            if target is None:
                continue
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"missing/outside-project link in {display(source)}: {raw}")
            elif target.suffix == ".qmd" and target not in files:
                errors.append(f"linked QMD is not in the book: {display(source)} -> {raw}")
            else:
                anchor = unquote(urlsplit(link_target(raw)).fragment)
                if (anchor.startswith(tuple(prefix + "-" for prefix in REF_PREFIXES))
                        and target.suffix in {".qmd", ".md"}):
                    if target not in target_ids:
                        # A Quarto wrapper owns the anchors of its included
                        # sections, but not anchors from unrelated book pages.
                        closure, include_errors = collect_qmd_tree([target])
                        errors.extend(include_errors)
                        target_ids[target] = {
                            label for path in closure
                            if path.is_relative_to(ROOT) and path.is_file()
                            and path.suffix in {".qmd", ".md"}
                            for label in ID_RE.findall(manuscript_text(path))
                        }
                    if anchor not in target_ids[target]:
                        errors.append(f"missing explicit link anchor in {display(source)}: {raw}")
    return errors


def check_sidebar(files: set[Path]) -> list[str]:
    def targets(items):
        for item in items or []:
            if isinstance(item, str):
                yield item
            elif isinstance(item, dict):
                if item.get("href"):
                    yield item["href"]
                yield from targets(item.get("contents"))

    errors: list[str] = []
    for profile in [QUARTO, *sorted(ROOT.glob("_quarto-*.yml"))]:
        config = yaml.safe_load(profile.read_text(encoding="utf-8")) or {}
        contents = config.get("book", {}).get("sidebar", {}).get("contents", [])
        if isinstance(contents, str):
            continue
        for raw in targets(contents):
            path = resolve_relative(raw, profile)
            if path is not None and path.suffix == ".qmd" and (not path.exists() or path not in files):
                errors.append(f"sidebar QMD is not in the book: {profile.name} -> {raw}")
    return errors


def main() -> int:
    config = load_quarto()
    start_files = declared_files(config)
    errors: list[str] = []

    files, include_errors = collect_qmd_tree(start_files)
    errors.extend(include_errors)
    errors.extend(check_assets(files))
    errors.extend(check_refs(files))
    errors.extend(check_links(files))
    errors.extend(check_sidebar(files))

    if errors:
        for error in errors:
            print(f"[fail] {error}", file=sys.stderr)
        return 1

    print(f"[ok] checked {len(files)} manuscript/source files for includes, assets, and explicit refs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
