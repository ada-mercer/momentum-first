#!/usr/bin/env python3
"""Build manuscript figures from the registry."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

# Prefer the repo virtualenv for optional dependencies like PyYAML, even when this
# script is launched by the system Python.
_root = Path(__file__).resolve().parents[2]
_venv_site = _root / ".venv" / "lib"
if _venv_site.exists():
    matches = sorted(_venv_site.glob("python*/site-packages"))
    if matches:
        sys.path.insert(0, str(matches[-1]))

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised only in missing-dependency envs
    print(
        "[fail] Missing PyYAML, required to read figures/figures.yml.\n"
        "Install minimal/dev dependencies with one of:\n"
        "  python3 -m pip install -r tooling/ci/requirements-minimal.txt\n"
        "  python3 -m pip install -r tooling/ci/requirements.txt",
        file=sys.stderr,
    )
    raise SystemExit(1) from exc


def runner_for(src: Path, python: Path) -> list[str] | None:
    suffix = src.suffix.lower()
    if suffix == ".py":
        return [str(python), str(src)]
    if suffix == ".r":
        return ["Rscript", str(src)]
    if src.name.endswith((".prompt.md", ".provenance.md")):
        return None
    raise ValueError(f"Unsupported figure source type: {src}")


def check_python_modules(python: Path, modules: list[str]) -> None:
    if not modules:
        return
    code = "; ".join(f"import {module}" for module in modules)
    proc = subprocess.run([str(python), "-c", code], capture_output=True, text=True)
    if proc.returncode != 0:
        print(
            "[fail] Missing Python dependency for figure builds.\n"
            f"Python: {python}\n"
            f"Required modules: {', '.join(modules)}\n"
            "Install figure/dev dependencies with:\n"
            "  python3 -m pip install -r tooling/ci/requirements.txt\n"
            "or run only non-figure checks with:\n"
            "  python3 tooling/scripts/check_dependencies.py --mode minimal\n"
            f"Details: {proc.stderr.strip() or proc.stdout.strip()}",
            file=sys.stderr,
        )
        raise SystemExit(1)


def require_command(name: str, *, purpose: str) -> None:
    if shutil.which(name):
        return
    print(
        f"[fail] Missing command `{name}`, required for {purpose}.\n"
        "Install the full/figure toolchain, or run a minimal lint-only check instead:\n"
        "  python3 tooling/scripts/check_dependencies.py --mode minimal",
        file=sys.stderr,
    )
    raise SystemExit(1)


def preflight(figures: list[dict[str, object]], python: Path) -> None:
    sources = [Path(str(fig.get("source", ""))) for fig in figures]
    if any(src.suffix.lower() == ".py" for src in sources):
        # Current executable Python figures depend on the repo figure/dev stack.
        check_python_modules(python, ["numpy", "matplotlib"])
    if any(src.suffix.lower() == ".r" for src in sources):
        require_command("Rscript", purpose="registered .R figure sources")


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    registry = root / "figures" / "figures.yml"
    venv_python = root / ".venv" / "bin" / "python"
    python = venv_python if venv_python.exists() else Path(sys.executable)

    data = yaml.safe_load(registry.read_text(encoding="utf-8")) or {}
    figures = data.get("figures", [])
    if not figures:
        print("No figures registered.")
        return

    preflight(figures, python)

    built = 0
    checked_static = 0
    for fig in figures:
        src = root / str(fig["source"])
        output = root / str(fig["output"])
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
