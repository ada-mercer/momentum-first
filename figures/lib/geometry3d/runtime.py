"""Runtime helpers for geometry3d rendering."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from .backends import render_scene_with_backend
from .cameras import get_camera_preset
from .exporters import build_output_path, validate_output_file
from .manifest import FamilyManifest, GeometryManifest, load_manifest
from .scene_spec import SceneSpec
from .styles import get_style_preset


def _ensure_lib_on_path(manifest: GeometryManifest) -> None:
    lib_parent = str(manifest.library_root.parent)
    if lib_parent not in sys.path:
        sys.path.insert(0, lib_parent)


def _load_module_from_path(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem.replace('-', '_'), path)
    if spec is None or spec.loader is None:
        raise ImportError(f'Could not create import spec for {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _build_scene(manifest: GeometryManifest, family: FamilyManifest, scene_id: str | None) -> tuple[SceneSpec, object, object]:
    if family.module is None:
        raise NotImplementedError(f'Family {family.family_id} has no implementation module yet')
    _ensure_lib_on_path(manifest)
    module_path = manifest.project_root / family.module
    module = _load_module_from_path(module_path)
    scene_manifest = family.get_scene(scene_id)
    try:
        builder = getattr(module, scene_manifest.function)
    except AttributeError as exc:
        raise AttributeError(f'Family module {module_path} has no builder {scene_manifest.function!r}') from exc
    scene = builder()
    if not isinstance(scene, SceneSpec):
        raise TypeError(f'Builder {scene_manifest.function} did not return a SceneSpec')
    scene.validate()
    return scene, module, scene_manifest


def render_scene(
    manifest_path: str | Path,
    family_id: str,
    scene_id: str | None = None,
    *,
    backend_name: str | None = None,
    camera_name: str | None = None,
    style_name: str | None = None,
    verbose: bool = False,
) -> Path:
    manifest = load_manifest(manifest_path)
    family = manifest.get_family(family_id)
    scene, _module, scene_manifest = _build_scene(manifest, family, scene_id)

    backend = (
        backend_name
        or scene_manifest.default_backend
        or scene_manifest.canonical_backend
        or family.default_backend
        or family.canonical_backend
        or manifest.default_backend
        or manifest.primary_backend
    )
    camera = camera_name or scene.default_camera or family.default_camera
    style = style_name or scene.default_style or family.default_style
    if not style:
        raise ValueError(f'No style could be resolved for {family_id}/{scene.scene_id}')

    get_camera_preset(camera)
    get_style_preset(style)

    output_target = scene.get_output(scene_manifest.output_kind)
    output_path = build_output_path(manifest.build_root, family.family_id, output_target)
    render_scene_with_backend(
        backend,
        scene=scene,
        output_path=output_path,
        camera_name=camera,
        style_name=style,
    )
    validate_output_file(output_path)

    if hasattr(_module, 'post_render'):
        _module.post_render(
            scene=scene,
            output_path=output_path,
            manifest=manifest,
            family=family,
            backend_name=backend,
            camera_name=camera,
            style_name=style,
        )

    if verbose:
        print(f'rendered {family.family_id}/{scene.scene_id} -> {output_path}')
    return output_path


def render_family(
    manifest_path: str | Path,
    family_id: str,
    *,
    backend_name: str | None = None,
    camera_name: str | None = None,
    style_name: str | None = None,
    verbose: bool = False,
) -> list[Path]:
    manifest = load_manifest(manifest_path)
    family = manifest.get_family(family_id)
    if not family.scenes:
        raise NotImplementedError(f'Family {family_id} has no implemented scenes yet')
    outputs = []
    for scene_manifest in family.scenes:
        outputs.append(
            render_scene(
                manifest.path,
                family_id,
                scene_id=scene_manifest.scene_id,
                backend_name=backend_name,
                camera_name=camera_name,
                style_name=style_name,
                verbose=verbose,
            )
        )
    return outputs
