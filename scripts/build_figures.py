#!/usr/bin/env python3
"""Build manuscript figures from the registry."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    registry = root / "figures" / "figures.yml"
    venv_python = root / ".venv" / "bin" / "python"
    python = venv_python if venv_python.exists() else Path(sys.executable)

    data = yaml.safe_load(registry.read_text()) or {}
    figures = data.get("figures", [])
    if not figures:
        print("No figures registered.")
        return

    for fig in figures:
        src = root / fig["source"]
        print(f"Building {fig['id']} from {src}...")
        subprocess.run([str(python), str(src)], check=True, cwd=root)

    print(f"Built {len(figures)} figures.")


if __name__ == "__main__":
    main()
