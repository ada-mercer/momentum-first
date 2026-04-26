#!/usr/bin/env python3
"""Render a geometry3d scene with multiple backends and preserve comparison copies."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB_ROOT = ROOT / 'lib'
if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

from geometry3d.manifest import load_manifest
from geometry3d.runtime import render_scene

MANIFEST = ROOT / 'manifests' / 'geometry3d.yml'


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Compare geometry3d scene renders across backends.')
    parser.add_argument('--family', required=True)
    parser.add_argument('--scene', required=True)
    parser.add_argument('--backends', nargs='+', default=['matplotlib3d', 'pyvista3d'])
    parser.add_argument('--manifest', default=str(MANIFEST))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest = load_manifest(args.manifest)
    review_dir = manifest.build_root / args.family / 'review'
    review_dir.mkdir(parents=True, exist_ok=True)

    for backend in args.backends:
        output = render_scene(args.manifest, args.family, args.scene, backend_name=backend, verbose=True)
        review_copy = review_dir / f'{args.scene}-{backend}.png'
        shutil.copyfile(output, review_copy)
        print(f'{backend}: {review_copy} size={review_copy.stat().st_size} sha256={sha256(review_copy)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
