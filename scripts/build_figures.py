#!/usr/bin/env python3
"""Build manuscript figures.

Initial placeholder entrypoint for future figure orchestration.
"""

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    figures_dir = root / "figures"
    print(f"Figure build placeholder. Root: {root}")
    print(f"Figures directory: {figures_dir}")


if __name__ == "__main__":
    main()
