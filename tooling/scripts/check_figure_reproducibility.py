#!/usr/bin/env python3
"""Validate bounded renderer drift and restore committed canonical PNG bytes."""

from __future__ import annotations

import io
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]

# Matplotlib's PNG encoder varies across supported host runtimes even when the
# rendered pixels are materially identical. Keep this exception explicit and
# narrow; all other canonical figure outputs remain byte-exact.
TOLERANT_PNGS = {
    "figures/build/foundations/foundations-shells.png",
    "figures/build/geometry3d/foundations-shells/canonical/foundations-shells.png",
}
MAX_MEAN_CHANNEL_DELTA = 1.0
MAX_HIGH_DELTA_PIXEL_FRACTION = 0.01
HIGH_DELTA = 16


def _run(*args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        list(args),
        cwd=ROOT,
        check=True,
        capture_output=True,
    )


def _changed_build_paths() -> list[str]:
    result = _run(
        "git",
        "diff",
        "--name-only",
        "--diff-filter=ACMRT",
        "HEAD",
        "--",
        "figures/build",
    )
    return [line for line in result.stdout.decode("utf-8").splitlines() if line]


def _committed_bytes(path: str) -> bytes:
    return _run("git", "show", f"HEAD:{path}").stdout


def _pixel_metrics(reference: bytes, generated_path: Path) -> tuple[float, float, int]:
    with Image.open(io.BytesIO(reference)) as expected_image:
        expected = np.asarray(expected_image.convert("RGBA"), dtype=np.int16)
    with Image.open(generated_path) as actual_image:
        actual = np.asarray(actual_image.convert("RGBA"), dtype=np.int16)

    if expected.shape != actual.shape:
        raise ValueError(f"dimension mismatch: expected {expected.shape}, got {actual.shape}")

    delta = np.abs(expected - actual)
    mean_channel_delta = float(delta.mean())
    high_delta_fraction = float(np.any(delta > HIGH_DELTA, axis=2).mean())
    return mean_channel_delta, high_delta_fraction, int(delta.max())


def main() -> int:
    changed = _changed_build_paths()
    if not changed:
        print("[ok] canonical figure outputs are byte-exact")
        return 0

    unexpected = [path for path in changed if path not in TOLERANT_PNGS]
    if unexpected:
        print("[fail] unexpected canonical figure drift:")
        for path in unexpected:
            print(f"  - {path}")
        return 1

    failed = False
    for path in changed:
        reference = _committed_bytes(path)
        generated_path = ROOT / path
        try:
            mean_delta, high_fraction, max_delta = _pixel_metrics(reference, generated_path)
        except ValueError as exc:
            print(f"[fail] {path}: {exc}")
            failed = True
            continue

        print(
            f"[check] {path}: mean-channel-delta={mean_delta:.6f}, "
            f"high-delta-pixels={high_fraction:.6%}, max-channel-delta={max_delta}"
        )
        if (
            mean_delta > MAX_MEAN_CHANNEL_DELTA
            or high_fraction > MAX_HIGH_DELTA_PIXEL_FRACTION
        ):
            print(f"[fail] {path}: pixel drift exceeds the bounded renderer tolerance")
            failed = True
            continue

        # The repository bytes are canonical. Restore them after accepting only
        # bounded renderer/encoding drift so the later book render uses the
        # committed asset and the working tree returns to byte-exact cleanliness.
        generated_path.write_bytes(reference)
        print(f"[ok] {path}: bounded drift accepted; canonical bytes restored")

    if failed:
        return 1

    remaining = _changed_build_paths()
    if remaining:
        print(f"[fail] canonical figure drift remains after restoration: {remaining}")
        return 1

    print("[ok] registered figure regeneration is reproducible within declared bounds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
