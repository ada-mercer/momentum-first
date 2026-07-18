#!/usr/bin/env python3
"""Lightweight manuscript structure and cross-reference checks.

This is intentionally modest: Quarto remains the authoritative renderer, while this
script catches common repo-hygiene errors before a full render.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - dependency check should catch this first
    yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[2]
QUARTO = ROOT / "_quarto.yml"
REF_PREFIXES = ("fig", "tbl", "eq", "sec", "lst", "thm", "lem", "cor", "prp", "exm", "def")

INCLUDE_RE = re.compile(r"\{\{<\s+include\s+([^\s>]+)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
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
            out.extend(iter_book_chapters(item.get("chapters")))
    return out


def declared_files(config: dict) -> list[Path]:
    paths: list[str] = []
    project_render = config.get("project", {}).get("render", [])
    if isinstance(project_render, str):
        paths.append(project_render)
    else:
        paths.extend(project_render or [])
    paths.extend(iter_book_chapters(config.get("book", {}).get("chapters")))

    seen: set[Path] = set()
    out: list[Path] = []
    for raw in paths:
        p = (ROOT / raw).resolve()
        if p not in seen:
            out.append(p)
            seen.add(p)
    return out


def resolve_relative(raw: str, source: Path) -> Path | None:
    cleaned = raw.strip().strip('"\'')
    cleaned = cleaned.split("{", 1)[0].strip()
    cleaned = cleaned.split(None, 1)[0].strip()
    if not cleaned or cleaned.startswith(("http://", "https://", "mailto:", "#")):
        return None
    candidate = (source.parent / cleaned).resolve()
    if candidate.exists():
        return candidate
    return (ROOT / cleaned).resolve()


def collect_qmd_tree(start_files: list[Path]) -> tuple[set[Path], list[str]]:
    seen: set[Path] = set()
    errors: list[str] = []
    stack = list(start_files)
    while stack:
        path = stack.pop()
        if path in seen:
            continue
        seen.add(path)
        if not path.exists():
            errors.append(f"missing declared/include file: {path.relative_to(ROOT)}")
            continue
        if path.suffix.lower() not in {".qmd", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in INCLUDE_RE.finditer(text):
            resolved = resolve_relative(match.group(1), path)
            if resolved is not None:
                stack.append(resolved)
    return seen, errors


def check_assets(files: set[Path]) -> list[str]:
    errors: list[str] = []
    for path in sorted(files):
        if not path.exists() or path.suffix.lower() not in {".qmd", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in IMAGE_RE.finditer(text):
            target = resolve_relative(match.group(1), path)
            if target is not None and not target.exists():
                errors.append(
                    f"missing image asset in {path.relative_to(ROOT)}: {match.group(1)}"
                )
    return errors


def check_refs(files: set[Path]) -> list[str]:
    ids: set[str] = set()
    refs: dict[str, list[Path]] = {}
    for path in files:
        if not path.exists() or path.suffix.lower() not in {".qmd", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        ids.update(ID_RE.findall(text))
        for ref in REF_RE.findall(text):
            refs.setdefault(ref, []).append(path)

    errors: list[str] = []
    for ref, locations in sorted(refs.items()):
        if ref not in ids:
            where = ", ".join(str(p.relative_to(ROOT)) for p in locations[:3])
            errors.append(f"unresolved cross-reference @{ref} in {where}")
    return errors


def main() -> int:
    config = load_quarto()
    start_files = declared_files(config)
    errors: list[str] = []

    for path in start_files:
        if not path.exists():
            errors.append(f"missing file declared in _quarto.yml: {path.relative_to(ROOT)}")

    files, include_errors = collect_qmd_tree(start_files)
    errors.extend(include_errors)
    errors.extend(check_assets(files))
    errors.extend(check_refs(files))

    if errors:
        for error in errors:
            print(f"[fail] {error}", file=sys.stderr)
        return 1

    print(f"[ok] checked {len(files)} manuscript/source files for includes, assets, and explicit refs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
