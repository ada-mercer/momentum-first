#!/usr/bin/env python3
"""Generate the manuscript status table from the canonical YAML ledger.

Reads `metadata/manuscript-status.yml` (the single source of truth) and writes a
Markdown table to `backmatter/_manuscript-status-table.md`, which the rendered
page `backmatter/manuscript-status.qmd` includes. Keeping the generated table in
a separate `_`-prefixed partial means Quarto never treats it as its own chapter,
and the qmd stays a thin wrapper.

Run manually with `python scripts/build_manuscript_status.py`, or let it run
automatically at Quarto pre-render (wired in `_quarto.yml`).
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - check_dependencies.py should catch this
    print("[error] PyYAML is required (pip install pyyaml)", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "metadata" / "manuscript-status.yml"
OUTPUT = ROOT / "backmatter" / "_manuscript-status-table.md"

MATURITY_LABELS = {
    "seed": "Seed",
    "working_draft": "Working draft",
    "stabilizing": "Stabilizing",
    "mature": "Mature",
}
VERIFICATION_LABELS = {
    "none": "—",
    "V1": "V1 (editorial)",
    "V2": "V2 (conceptual)",
    "V3": "V3 (technical)",
}


def _label(value: str, table: dict[str, str]) -> str:
    return table.get(value, value)


def _verification_cell(verification: str, verified_by: str) -> str:
    label = _label(verification, VERIFICATION_LABELS)
    if verification != "none" and verified_by:
        return f"{label} · {verified_by.strip()}"
    return label


def _row(entry: dict) -> str:
    return (
        f"| {entry.get('title', entry.get('id', '?'))} "
        f"| {_label(entry.get('maturity', 'seed'), MATURITY_LABELS)} "
        f"| {_verification_cell(entry.get('verification', 'none'), entry.get('verified_by', ''))} "
        f"| {str(entry.get('note', '')).strip()} |"
    )


def main() -> int:
    if not LEDGER.exists():
        print(f"[error] missing ledger: {LEDGER}", file=sys.stderr)
        return 1

    data = yaml.safe_load(LEDGER.read_text(encoding="utf-8")) or {}

    lines: list[str] = [
        "<!-- GENERATED FILE — do not edit. Source: metadata/manuscript-status.yml",
        "     Regenerate with: python scripts/build_manuscript_status.py -->",
        "",
        "| Chapter | Maturity | Verification | Notes |",
        "|---|---|---|---|",
    ]

    for ch in data.get("chapters", []) or []:
        lines.append(_row(ch))

    appx = data.get("appendices")
    if appx:
        lines.append(_row(appx))

    lines.append("")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] wrote {OUTPUT.relative_to(ROOT)} ({len(data.get('chapters', []) or [])} chapters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
