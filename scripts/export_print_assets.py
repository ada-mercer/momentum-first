#!/usr/bin/env python3
"""Export print-oriented release assets from the rendered book output."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "_book"
OUT_DIR = ROOT / "dist" / "print"


def newest(paths: list[Path]) -> Path | None:
    return max(paths, key=lambda p: p.stat().st_mtime, default=None)


def main() -> int:
    pdf = newest(list(BOOK_DIR.glob("*.pdf")))
    if pdf is None:
        print("[fail] no rendered PDF found under _book/; run `quarto render --profile pdf` first", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target_pdf = OUT_DIR / "Momentum-First.pdf"
    shutil.copy2(pdf, target_pdf)

    print(f"[ok] exported {target_pdf.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
