#!/usr/bin/env python3
"""Build manuscript tables from an optional registry.

If `tables/tables.yml` does not exist, there are no canonical generated tables yet
and the command exits cleanly. A future registry can contain entries like:

- id: example-table
  command: python scripts/make_example_table.py
  output: tables/build/example-table.csv
"""

from __future__ import annotations

import shlex
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - dependency check should catch this first
    yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "tables" / "tables.yml"


def main() -> int:
    if not REGISTRY.exists():
        print("[ok] no tables/tables.yml registry; no generated tables to build")
        return 0
    if yaml is None:
        print("[fail] PyYAML is required to read tables/tables.yml", file=sys.stderr)
        return 1

    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    tables = data.get("tables", data if isinstance(data, list) else [])
    if not isinstance(tables, list):
        print("[fail] table registry must be a list or contain a 'tables' list", file=sys.stderr)
        return 1

    built = 0
    for table in tables:
        if not isinstance(table, dict):
            print(f"[fail] invalid table entry: {table!r}", file=sys.stderr)
            return 1
        table_id = table.get("id", "<unnamed>")
        command = table.get("command")
        output = table.get("output")
        if not command or not output:
            print(f"[fail] table {table_id} must define command and output", file=sys.stderr)
            return 1
        print(f"Building table {table_id}...")
        subprocess.run(shlex.split(command), check=True, cwd=ROOT)
        output_path = ROOT / output
        if not output_path.exists() or output_path.stat().st_size == 0:
            print(f"[fail] table {table_id} did not produce non-empty {output}", file=sys.stderr)
            return 1
        built += 1

    print(f"[ok] built {built} table(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
