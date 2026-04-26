"""Output helpers for geometry3d."""

from __future__ import annotations

from pathlib import Path

from .primitives import SUPPORTED_OUTPUT_KINDS
from .scene_spec import OutputTarget

OUTPUT_SUFFIXES = {
    'canonical_png': '.png',
    'preview_png': '.png',
}


def build_output_path(build_root: Path, family: str, target: OutputTarget) -> Path:
    if target.kind not in SUPPORTED_OUTPUT_KINDS:
        raise KeyError(f'Unsupported geometry3d output kind: {target.kind}')
    suffix = OUTPUT_SUFFIXES[target.kind]
    filename = target.filename
    if not filename.endswith(suffix):
        filename = f'{filename}{suffix}'
    return build_root / family / target.subdir / filename


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def validate_output_file(path: Path) -> Path:
    if not path.exists():
        raise FileNotFoundError(f'Expected render output was not created: {path}')
    if path.stat().st_size == 0:
        raise ValueError(f'Render output is empty: {path}')
    return path
