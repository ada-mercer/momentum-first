#!/usr/bin/env python3
"""Dependency smoke test for the Momentum First book repo."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CheckFailure(RuntimeError):
    pass


def run_cmd(cmd: list[str], *, cwd: Path | None = None) -> tuple[int, str, str]:
    proc = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise CheckFailure(f"missing command: {name}")
    return path


def check_version(name: str, cmd: list[str]) -> None:
    require_command(name)
    code, out, err = run_cmd(cmd)
    if code != 0:
        raise CheckFailure(f"{name} version check failed: {err or out}")
    print(f"[ok] {name}: {(out or err).splitlines()[0]}")


def check_python_imports() -> None:
    modules = ["numpy", "matplotlib", "pandas", "yaml", "nbformat", "pytest"]
    venv_python = ROOT / ".venv" / "bin" / "python"
    python_bin = venv_python if venv_python.exists() else Path(sys.executable)
    code, out, err = run_cmd(
        [
            str(python_bin),
            "-c",
            (
                "import numpy, matplotlib, pandas, yaml, nbformat, pytest; "
                "print('numpy,matplotlib,pandas,yaml,nbformat,pytest')"
            ),
        ]
    )
    if code != 0:
        raise CheckFailure(f"python import check failed via {python_bin}: {err or out}")
    env_label = "repo venv" if venv_python.exists() else "current python"
    print(f"[ok] python imports ({env_label}): {out.strip()}")


def check_r_packages() -> None:
    require_command("Rscript")
    env = os.environ.copy()
    env.setdefault("R_LIBS_USER", str(Path.home() / ".local/share/R/%p-library/%v"))
    proc = subprocess.run(
        [
            "Rscript",
            "-e",
            'dir.create(path.expand(Sys.getenv("R_LIBS_USER")), recursive=TRUE, showWarnings=FALSE); .libPaths(c(path.expand(Sys.getenv("R_LIBS_USER")), .libPaths())); pkgs <- c("knitr","rmarkdown"); miss <- pkgs[!vapply(pkgs, requireNamespace, logical(1), quietly=TRUE)]; if (length(miss)) { message(paste(miss, collapse=",")); quit(status=1) } else { cat("knitr,rmarkdown\n") }',
        ],
        capture_output=True,
        text=True,
        env=env,
    )
    code, out, err = proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    if code != 0:
        raise CheckFailure(f"R package check failed: {err or out}")
    print(f"[ok] R packages: {out.strip()}")


def check_julia_basic() -> None:
    require_command("julia")
    code, out, err = run_cmd(["julia", "-e", 'println("julia-ok")'])
    if code != 0 or "julia-ok" not in out:
        raise CheckFailure(f"Julia smoke test failed: {err or out}")
    print("[ok] julia: julia-ok")


def check_quarto_render() -> None:
    require_command("quarto")
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        qmd = tmp_path / "smoke.qmd"
        qmd.write_text(
            textwrap.dedent(
                """
                ---
                title: "Dependency Smoke Test"
                format: html
                ---

                # Smoke Test

                This is a minimal Quarto render check.
                """
            ).strip()
            + "\n",
            encoding="utf-8",
        )
        code, out, err = run_cmd(["quarto", "render", str(qmd)], cwd=tmp_path)
        if code != 0:
            raise CheckFailure(f"Quarto render failed: {err or out}")
        html = tmp_path / "smoke.html"
        if not html.exists():
            raise CheckFailure("Quarto render did not produce smoke.html")
    print("[ok] quarto render: smoke.html generated")


def check_pdf_toolchain() -> None:
    for name, cmd in [
        ("latexmk", ["latexmk", "-v"]),
        ("biber", ["biber", "--version"]),
    ]:
        require_command(name)
        code, out, err = run_cmd(cmd)
        if code != 0:
            raise CheckFailure(f"{name} check failed: {err or out}")
        print(f"[ok] {name}: {(out or err).splitlines()[0]}")


def main() -> int:
    print(f"Running dependency checks in {ROOT}")
    try:
        check_version("git", ["git", "--version"])
        check_version("python3", ["python3", "--version"])
        venv_python = ROOT / ".venv" / "bin" / "python"
        if venv_python.exists():
            code, out, err = run_cmd([str(venv_python), "--version"])
            if code != 0:
                raise CheckFailure(f"repo venv python version check failed: {err or out}")
            print(f"[ok] repo-venv-python: {(out or err).splitlines()[0]}")
        check_version("quarto", ["quarto", "--version"])
        check_version("R", ["R", "--version"])
        check_version("julia", ["julia", "--version"])
        check_version("dot", ["dot", "-V"])
        check_version("inkscape", ["inkscape", "--version"])
        check_version("rsvg-convert", ["rsvg-convert", "--version"])
        check_python_imports()
        check_r_packages()
        check_julia_basic()
        check_quarto_render()
        check_pdf_toolchain()
    except CheckFailure as exc:
        print(f"[fail] {exc}", file=sys.stderr)
        return 1

    print("All baseline dependency checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
