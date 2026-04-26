"""Backend registry and dispatch for geometry3d."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..scene_spec import SceneSpec


@dataclass(frozen=True, slots=True)
class BackendSpec:
    name: str
    purpose: str
    supports_interactive: bool
    headless_friendly: bool


BACKEND_REGISTRY: dict[str, BackendSpec] = {
    'matplotlib3d': BackendSpec(
        name='matplotlib3d',
        purpose='Default static manuscript backend',
        supports_interactive=False,
        headless_friendly=True,
    ),
    'pyvista3d': BackendSpec(
        name='pyvista3d',
        purpose='Higher-fidelity surface backend for richer scenes',
        supports_interactive=True,
        headless_friendly=False,
    ),
    'plotly3d': BackendSpec(
        name='plotly3d',
        purpose='Browser-facing interactive inspection backend',
        supports_interactive=True,
        headless_friendly=True,
    ),
}


def get_backend_spec(name: str) -> BackendSpec:
    try:
        return BACKEND_REGISTRY[name]
    except KeyError as exc:
        raise KeyError(f'Unknown geometry3d backend: {name}') from exc


def render_scene_with_backend(
    name: str,
    *,
    scene: SceneSpec,
    output_path: Path,
    camera_name: str,
    style_name: str,
) -> Path:
    if name == 'matplotlib3d':
        from .matplotlib3d import render_scene

        return render_scene(scene=scene, output_path=output_path, camera_name=camera_name, style_name=style_name)
    if name == 'pyvista3d':
        from .pyvista3d import render_scene

        return render_scene(scene=scene, output_path=output_path, camera_name=camera_name, style_name=style_name)
    if name == 'plotly3d':
        raise NotImplementedError('Backend plotly3d is still a stub')
    raise KeyError(f'Unknown geometry3d backend: {name}')
