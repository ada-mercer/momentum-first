#!/usr/bin/env python3
"""Build manuscript figures from the registry."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# Prefer the repo virtualenv for optional dependencies like PyYAML, even when this
# script is launched by the system Python.
_root = Path(__file__).resolve().parents[1]
_venv_site = _root / ".venv" / "lib"
if _venv_site.exists():
    matches = sorted(_venv_site.glob("python*/site-packages"))
    if matches:
        sys.path.insert(0, str(matches[-1]))

import yaml


def runner_for(src: Path, python: Path) -> list[str]:
    suffix = src.suffix.lower()
    if suffix == ".py":
        return [str(python), str(src)]
    if suffix in {".r", ".R".lower()}:  # normalized below anyway
        return ["Rscript", str(src)]
    raise ValueError(f"Unsupported figure source type: {src}")


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
        cmd = runner_for(src, python)
        print(f"Building {fig['id']} from {src}...")
        subprocess.run(cmd, check=True, cwd=root)

    print(f"Built {len(figures)} figures.")


if __name__ == "__main__":
    main()
