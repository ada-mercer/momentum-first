#!/usr/bin/env python3
"""Check (default) or set the immutable publication image in all consumer jobs.

Actions needs literal container images before checkout, so workflow copies are
checked projections of tooling/ci/image/reference.txt, not independent choices.
No image is built, pulled, published or adopted remotely by this command.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = Path("tooling/ci/image/reference.txt")
WORKFLOWS = ("benchmark-ci-image.yml", "build-figures.yml", "render-book.yml", "release-book.yml")
IMAGE_RE = re.compile(r"ghcr\.io/ada-mercer/momentum-first-build@sha256:[0-9a-f]{64}")
LINE_RE = re.compile(r"^(\s+image: )([^\s]+)$", re.M)


def synchronize(root: Path, image: str | None = None) -> list[str]:
    expected = image if image is not None else (root / REFERENCE).read_text().strip()
    if not IMAGE_RE.fullmatch(expected):
        raise ValueError("publication image must be the project GHCR image pinned by a SHA-256 digest")
    updates = []
    for name in WORKFLOWS:
        path = root / ".github/workflows" / name
        text = path.read_text()
        matches = list(LINE_RE.finditer(text))
        if len(matches) != 1 or not IMAGE_RE.fullmatch(matches[0].group(2)):
            raise ValueError(f"unexpected container-image layout in {name}; no files updated")
        if matches[0].group(2) != expected:
            updates.append((path, LINE_RE.sub(lambda m: m.group(1) + expected, text)))
    if image is not None:
        # Validate every consumer before writing any of them.
        for path, text in updates:
            path.write_text(text)
        (root / REFERENCE).write_text(expected + "\n")
    return [str(path.relative_to(root)) for path, _ in updates]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--set", dest="image", help="Set a previously benchmarked immutable image")
    args = parser.parse_args()
    try:
        changed = synchronize(ROOT, args.image)
    except (ValueError, OSError) as exc:
        print(f"[fail] {exc}")
        return 1
    if args.image is None and changed:
        print("[fail] CI image references differ: " + ", ".join(changed))
        return 1
    print("[ok] publication workflows match the maintained image reference")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
