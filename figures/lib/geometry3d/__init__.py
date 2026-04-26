"""Shared support layer for native 3D geometry figures."""

from .cameras import CameraPreset, get_camera_preset, list_camera_presets
from .manifest import FamilyManifest, GeometryManifest, SceneManifest, load_manifest
from .primitives import (
    DEFAULT_MESH_RESOLUTION,
    BoundingBox,
    MeshResolution,
    bounding_box_coordinate_system_components,
    bounding_box_from_points,
    coordinate_system_components,
    half_sphere_shell_objects,
    sphere_shell_objects,
    vector_components,
    vector_object,
)
from .runtime import render_family, render_scene
from .scene_spec import FigureLayout, OutputTarget, SceneAnnotation, SceneObject, SceneSpec
from .styles import StylePreset, get_style_preset, list_style_presets

__all__ = [
    'BoundingBox',
    'CameraPreset',
    'DEFAULT_MESH_RESOLUTION',
    'bounding_box_coordinate_system_components',
    'bounding_box_from_points',
    'coordinate_system_components',
    'FamilyManifest',
    'FigureLayout',
    'GeometryManifest',
    'half_sphere_shell_objects',
    'MeshResolution',
    'OutputTarget',
    'SceneAnnotation',
    'SceneManifest',
    'SceneObject',
    'SceneSpec',
    'sphere_shell_objects',
    'StylePreset',
    'vector_components',
    'vector_object',
    'get_camera_preset',
    'get_style_preset',
    'list_camera_presets',
    'list_style_presets',
    'load_manifest',
    'render_family',
    'render_scene',
]
