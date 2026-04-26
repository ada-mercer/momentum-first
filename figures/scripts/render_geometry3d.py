#!/usr/bin/env python3
"""Render one geometry3d scene through the manifest-backed shared layer."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB_ROOT = ROOT / 'lib'


def _maybe_reexec_with_figures_python() -> None:
    if os.environ.get('_GEOMETRY3D_BOOTSTRAPPED') == '1':
        return
    env_python = os.environ.get('FIGURES_PYTHON')
    default_python = ROOT.parent / '.venv' / 'bin' / 'python'
    target = Path(env_python).resolve() if env_python else default_python.resolve() if default_python.exists() else None
    if target is None:
        return
    if Path(sys.executable).resolve() == target:
        return
    env = os.environ.copy()
    env['_GEOMETRY3D_BOOTSTRAPPED'] = '1'
    raise SystemExit(subprocess.run([str(target), __file__, *sys.argv[1:]], env=env).returncode)


_maybe_reexec_with_figures_python()

if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

from geometry3d.runtime import render_scene

MANIFEST = ROOT / 'manifests' / 'geometry3d.yml'
DOCS = ROOT / 'docs' / 'geometry3d' / 'QUICKSTART.md'


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Render one geometry3d scene.')
    parser.add_argument('--family', required=True, help='Geometry3d family slug, for example foundations-shells.')
    parser.add_argument('--scene', help='Scene id within the family. Defaults to the family canonical scene.')
    parser.add_argument('--backend', help='Backend override. Without this, runtime uses the family default from the manifest.')
    parser.add_argument('--camera', help='Camera preset override.')
    parser.add_argument('--style', help='Style preset override.')
    parser.add_argument('--manifest', default=str(MANIFEST), help='Path to geometry3d manifest.')
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        output = render_scene(
            args.manifest,
            args.family,
            args.scene,
            backend_name=args.backend,
            camera_name=args.camera,
            style_name=args.style,
            verbose=True,
        )
    except Exception as exc:
        print(f'geometry3d render failed: {exc}')
        print(f'See {DOCS} for the current supported workflow.')
        return 1
    print(output)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
