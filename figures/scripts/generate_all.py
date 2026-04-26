#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
REGISTRY = ROOT / "figures.yml"
DEFAULT_FIGURES_PYTHON = WORKSPACE / ".venv" / "bin" / "python"


def resolve_figures_python() -> str:
    env_python = os.environ.get("FIGURES_PYTHON")
    if env_python:
        return env_python
    if DEFAULT_FIGURES_PYTHON.exists():
        return str(DEFAULT_FIGURES_PYTHON)
    return sys.executable


def parse_registry(path: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if re.match(r"^\s*-\s+id:\s+", line):
            if current:
                entries.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
            continue
        m = re.match(r"^\s+(source|output|chapter):\s+(.*)$", line)
        if m and current is not None:
            current[m.group(1)] = m.group(2).strip()
    if current:
        entries.append(current)
    return entries


def run_entry(entry: dict[str, str], figures_python: str) -> int:
    source = WORKSPACE / entry["source"]
    if source.suffix == ".py":
        cmd = [figures_python, str(source)]
    elif source.suffix == ".R":
        cmd = ["Rscript", str(source)]
    elif source.name.endswith(".prompt.md"):
        output = WORKSPACE / entry["output"]
        if output.exists():
            print(f"\n==> {entry['id']}\nprompt-backed figure; checked output exists: {output}")
            return 0
        print(f"\n==> {entry['id']}\nmissing prompt-backed output: {output}")
        return 1
    else:
        print(f"skip unsupported source type: {source}")
        return 0
    print(f"\n==> {entry['id']}\n$ {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=WORKSPACE).returncode


def main() -> int:
    entries = parse_registry(REGISTRY)
    if not entries:
        print("No figures found in registry")
        return 1
    figures_python = resolve_figures_python()
    print(f"Using Python figure interpreter: {figures_python}")
    failures = []
    for entry in entries:
        rc = run_entry(entry, figures_python)
        if rc != 0:
            failures.append((entry["id"], rc))
    if failures:
        print("\nFailures:")
        for fig_id, rc in failures:
            print(f"- {fig_id}: exit {rc}")
        return 1
    print(f"\nRendered {len(entries)} figure(s) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
