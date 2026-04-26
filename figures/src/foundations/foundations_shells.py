#!/usr/bin/env python3
"""Compatibility wrapper for the migrated foundations-shells figure.

The real implementation now lives in `figures/src/geometry3d/foundations-shells/family.py`
and renders through the shared geometry3d scene/camera/style/backend path.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

FIGURES_ROOT = Path(__file__).resolve().parents[2]
LIB_ROOT = FIGURES_ROOT / 'lib'


def _maybe_reexec_with_figures_python() -> None:
    if os.environ.get('_GEOMETRY3D_BOOTSTRAPPED') == '1':
        return
    env_python = os.environ.get('FIGURES_PYTHON')
    default_python = FIGURES_ROOT.parent / '.venv' / 'bin' / 'python'
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

MANIFEST = FIGURES_ROOT / 'manifests' / 'geometry3d.yml'
LEGACY_OUTPUT = FIGURES_ROOT / 'build' / 'foundations' / 'foundations-shells.png'


if __name__ == '__main__':
    render_scene(MANIFEST, 'foundations-shells', 'foundations-shells')
    print(LEGACY_OUTPUT)
