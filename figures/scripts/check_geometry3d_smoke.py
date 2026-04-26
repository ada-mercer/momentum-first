#!/usr/bin/env python3
"""Minimal smoke checks for the implemented geometry3d path."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB_ROOT = ROOT / 'lib'
if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

from geometry3d.manifest import load_manifest
from geometry3d.runtime import render_scene

MANIFEST = ROOT / 'manifests' / 'geometry3d.yml'


def main() -> int:
    parser = argparse.ArgumentParser(description='Run a minimal geometry3d smoke check.')
    parser.add_argument('--backend', default=None, help='Optional backend override, for example matplotlib3d or pyvista3d.')
    args = parser.parse_args()

    manifest = load_manifest(MANIFEST)
    family = manifest.get_family('foundations-shells')
    scene = family.get_scene('foundations-shells')
    print(f'manifest phase: {manifest.phase}')
    print(f'family: {family.family_id}')
    print(f'scene: {scene.scene_id}')
    print(f'backend: {args.backend or family.default_backend}')
    output = render_scene(MANIFEST, 'foundations-shells', 'foundations-shells', backend_name=args.backend, verbose=True)
    print(f'output exists: {output.exists()} size={output.stat().st_size}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
