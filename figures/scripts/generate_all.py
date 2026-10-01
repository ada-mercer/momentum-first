#!/usr/bin/env python3
"""Compatibility entrypoint for the single registry builder."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(
        str(Path(__file__).resolve().parents[2] / "tooling/scripts/build_figures.py"),
        run_name="__main__",
    )
