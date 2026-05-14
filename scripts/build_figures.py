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


def runner_for(src: Path, python: Path) -> list[str] | None:
    suffix = src.suffix.lower()
    if suffix == ".py":
        return [str(python), str(src)]
    if suffix == ".r":
        return ["Rscript", str(src)]
    if src.name.endswith((".prompt.md", ".provenance.md")):
        return None
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

    built = 0
    checked_static = 0
    for fig in figures:
        src = root / fig["source"]
        output = root / fig["output"]
        if not src.exists():
            raise FileNotFoundError(f"Missing figure source for {fig['id']}: {src}")
        cmd = runner_for(src, python)
        if cmd is None:
            if not output.exists() or output.stat().st_size == 0:
                raise FileNotFoundError(
                    f"Figure {fig['id']} uses non-executable source {src.name}; "
                    f"expected checked output at {output}"
                )
            print(f"[ok] checked static/generated figure {fig['id']}: {output.relative_to(root)}")
            checked_static += 1
            continue
        print(f"Building {fig['id']} from {src}...")
        subprocess.run(cmd, check=True, cwd=root)
        if not output.exists() or output.stat().st_size == 0:
            raise FileNotFoundError(f"Figure {fig['id']} did not produce {output}")
        built += 1

    print(f"[ok] built {built} executable figure(s); checked {checked_static} static/generated figure(s).")


if __name__ == "__main__":
    main()
