#!/usr/bin/env python3
"""Shared local/CI validation; source checks do not rewrite manuscript outputs.

--publication additionally rebuilds figures against a clean canonical-output
baseline. Rendering and every publishing action remain separate commands.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def run_python(*args: str) -> int:
    print(f"[run] {' '.join(args)}", flush=True)
    return subprocess.run([sys.executable, *args], cwd=ROOT).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publication", action="store_true")
    args = parser.parse_args()
    checks = [
        ("dependencies", ["tooling/scripts/check_dependencies.py", "--mode",
                          "publication" if args.publication else "minimal"]),
        ("tests", ["-m", "pytest", "tooling/tests"]),
        ("crossrefs", ["tooling/scripts/check_crossrefs.py"]),
        ("status", ["tooling/scripts/build_manuscript_status.py", "--check"]),
    ]
    failed = [name for name, command in checks if run_python(*command)]
    if failed:
        print(f"[fail] validation: {', '.join(failed)}")
        return 1
    if args.publication:
        state = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", "figures/build"],
            cwd=ROOT, capture_output=True, text=True,
        )
        if state.returncode or state.stdout.strip():
            print("[fail] publication figure check requires a clean figures/build baseline; "
                  "use an isolated accepted snapshot to preserve authoring changes")
            return 1
        for script in ("build_figures.py", "check_figure_reproducibility.py"):
            if run_python(f"tooling/scripts/{script}"):
                return 1
    print("[ok] validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
