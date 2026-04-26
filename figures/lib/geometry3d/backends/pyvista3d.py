"""Working PyVista backend for geometry-native geometry3d renders."""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pyvista as pv
from matplotlib import colormaps
from matplotlib.colors import Normalize, to_hex

from ..cameras import CameraPreset, get_camera_preset
from ..exporters import ensure_parent
from ..primitives import SUPPORTED_ANNOTATION_KINDS, SUPPORTED_OBJECT_KINDS
from ..scene_spec import FigureLayout, SceneAnnotation, SceneObject, SceneSpec
from ..styles import StylePreset, get_style_preset

pv.OFF_SCREEN = True


def _resolve_color(style: StylePreset, params: dict, key: str = 'color'):
    palette_key = params.get(f'{key}_key')
    if palette_key:
        try:
            return style.palette[palette_key]
        except KeyError as exc:
            raise KeyError(f'Unknown style palette key: {palette_key}') from exc
    return params.get(key)


def _window_size(layout: FigureLayout) -> tuple[int, int]:
    width = max(640, int(layout.figsize[0] * layout.dpi))
    height = max(480, int(layout.figsize[1] * layout.dpi))
    return width, height


def _resolved_bounds(layout: FigureLayout, camera: CameraPreset) -> tuple[float, float, float, float, float, float]:
    xlim = camera.xlim or layout.xlim or (-1.0, 1.0)
    ylim = camera.ylim or layout.ylim or (-1.0, 1.0)
    zlim = camera.zlim or layout.zlim or (-1.0, 1.0)
    return (float(xlim[0]), float(xlim[1]), float(ylim[0]), float(ylim[1]), float(zlim[0]), float(zlim[1]))


def _apply_camera(plotter: pv.Plotter, layout: FigureLayout, camera_name: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, CameraPreset]:
    camera = get_camera_preset(camera_name)
    bounds = _resolved_bounds(layout, camera)
    xmin, xmax, ymin, ymax, zmin, zmax = bounds
    center = np.array([(xmin + xmax) / 2.0, (ymin + ymax) / 2.0, (zmin + zmax) / 2.0], dtype=float)
    extents = np.array([xmax - xmin, ymax - ymin, zmax - zmin], dtype=float)
    radius = float(max(extents.max() * 1.1, 1.0)) * camera.distance_scale

    az = math.radians(camera.azimuth_deg)
    el = math.radians(camera.elevation_deg)
    direction = np.array([
        math.cos(el) * math.cos(az),
        math.cos(el) * math.sin(az),
        math.sin(el),
    ])
    position = center + radius * direction

    plotter.camera.position = tuple(position)
    plotter.camera.focal_point = tuple(center)
    plotter.camera.up = camera.view_up
    if camera.projection_mode == 'orthographic':
        plotter.camera.parallel_projection = True
        if camera.orthographic_scale is not None:
            plotter.camera.parallel_scale = float(camera.orthographic_scale) / max(camera.zoom, 1e-6)
        else:
            plotter.camera.parallel_scale = float(max(extents.max() / 2.0, 1.0)) * camera.distance_scale / max(camera.zoom, 1e-6)
    else:
        plotter.camera.parallel_projection = False
        plotter.camera.view_angle = float(camera.view_angle_deg)
    if camera.zoom != 1.0:
        plotter.camera.zoom(camera.zoom)
    plotter.reset_camera_clipping_range()
    return center, position, direction, radius, camera


def _build_grid(params: dict) -> pv.StructuredGrid:
    x = np.asarray(params['x'])
    y = np.asarray(params['y'])
    z = np.asarray(params['z'])
    grid = pv.StructuredGrid(x, y, z)
    if 'scalar_field' in params:
        grid.point_data['geometry3d_scalars'] = np.asarray(params['scalar_field']).ravel(order='F')
    return grid


def _stride_slice(size: int, stride: int) -> list[int]:
    step = max(1, int(stride))
    indices = list(range(0, size, step))
    if not indices or indices[-1] != size - 1:
        indices.append(size - 1)
    return indices


def _downsample_structured_arrays(params: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.asarray(params['x'])
    y = np.asarray(params['y'])
    z = np.asarray(params['z'])
    rstride = int(params.get('rstride', 1))
    cstride = int(params.get('cstride', 1))
    row_idx = _stride_slice(x.shape[0], rstride)
    col_idx = _stride_slice(x.shape[1], cstride)
    return x[np.ix_(row_idx, col_idx)], y[np.ix_(row_idx, col_idx)], z[np.ix_(row_idx, col_idx)]


def _surface_kwargs(style: StylePreset, params: dict) -> dict:
    kwargs: dict = {
        'opacity': float(params.get('alpha', 1.0)),
        'smooth_shading': bool(params.get('shade', True)),
        'show_edges': False,
        'ambient': float(params.get('ambient', 0.22)),
        'diffuse': float(params.get('diffuse', 0.88)),
        'specular': float(params.get('specular', 0.05)),
        'specular_power': float(params.get('specular_power', 6.0)),
    }
    resolved_color = _resolve_color(style, params)
    if 'scalar_field' in params:
        scalars = np.asarray(params['scalar_field'])
        kwargs['scalars'] = 'geometry3d_scalars'
        kwargs['cmap'] = params.get('colormap', 'viridis')
        kwargs['clim'] = (float(np.nanmin(scalars)), float(np.nanmax(scalars)))
        kwargs['show_scalar_bar'] = False
        if 'alpha' in params:
            kwargs['opacity'] = float(params['alpha'])
    elif resolved_color is not None:
        kwargs['color'] = resolved_color
    return kwargs


def _add_surface(plotter: pv.Plotter, obj: SceneObject, style: StylePreset) -> None:
    grid = _build_grid(obj.params)
    plotter.add_mesh(grid, **_surface_kwargs(style, obj.params))


def _add_wireframe(plotter: pv.Plotter, obj: SceneObject, style: StylePreset) -> None:
    x, y, z = _downsample_structured_arrays(obj.params)
    grid = pv.StructuredGrid(x, y, z)
    plotter.add_mesh(
        grid,
        style='wireframe',
        color=_resolve_color(style, obj.params) or '#ffffff',
        opacity=float(obj.params.get('alpha', 1.0)),
        line_width=float(obj.params.get('linewidth', 1.0)),
        render_lines_as_tubes=True,
        ambient=0.35,
        diffuse=0.65,
        specular=0.02,
        specular_power=4.0,
    )


def _arrow_mesh(start: np.ndarray, direction: np.ndarray, linewidth: float, arrow_length_ratio: float, tip_radius_scale: float = 1.5) -> pv.PolyData:
    norm = float(np.linalg.norm(direction))
    if norm == 0.0:
        return pv.PolyData()
    shaft_radius = max(0.006, 0.006 * linewidth)
    tip_radius = shaft_radius * 1.9 * tip_radius_scale
    tip_length = min(0.42, max(0.16, arrow_length_ratio))
    return pv.Arrow(
        start=tuple(start.tolist()),
        direction=tuple((direction / norm).tolist()),
        scale=norm,
        tip_length=tip_length,
        tip_radius=tip_radius,
        shaft_radius=shaft_radius,
    )


def _add_vectors(plotter: pv.Plotter, obj: SceneObject, style: StylePreset) -> None:
    params = obj.params
    color = _resolve_color(style, params) or '#ffffff'
    opacity = float(params.get('alpha', 1.0))
    linewidth = float(params.get('linewidth', 1.0))
    arrow_length_ratio = float(params.get('arrow_length_ratio', 0.25))
    ambient = float(params.get('ambient', 0.18))
    diffuse = float(params.get('diffuse', 0.88))
    specular = float(params.get('specular', 0.04))
    specular_power = float(params.get('specular_power', 5.0))
    tip_radius_scale = float(params.get('tip_radius_scale', 1.5))

    starts = np.column_stack([np.asarray(params['x']), np.asarray(params['y']), np.asarray(params['z'])])
    vecs = np.column_stack([np.asarray(params['u']), np.asarray(params['v']), np.asarray(params['w'])])
    meshes: list[pv.PolyData] = []
    for start, direction in zip(starts, vecs, strict=False):
        mesh = _arrow_mesh(start, direction, linewidth, arrow_length_ratio, tip_radius_scale)
        if mesh.n_points:
            meshes.append(mesh)
    if not meshes:
        return
    merged = meshes[0]
    for mesh in meshes[1:]:
        merged = merged.merge(mesh)
    plotter.add_mesh(
        merged,
        color=color,
        opacity=opacity,
        smooth_shading=True,
        ambient=ambient,
        diffuse=diffuse,
        specular=specular,
        specular_power=specular_power,
    )


def _normalize_point_colors(color) -> str | list[str]:
    if isinstance(color, str):
        return color
    if isinstance(color, (list, tuple, np.ndarray)):
        if len(color) == 0:
            return '#ffffff'
        if isinstance(color[0], str):
            return list(color)
        return [to_hex(entry) for entry in color]
    return '#ffffff'


def _add_points(plotter: pv.Plotter, obj: SceneObject, style: StylePreset) -> None:
    params = obj.params
    points = np.column_stack([np.asarray(params['x']), np.asarray(params['y']), np.asarray(params['z'])])
    colors = _normalize_point_colors(_resolve_color(style, params) or params.get('color', '#ffffff'))
    point_size = max(2.0, float(np.sqrt(float(params.get('size', 32))) * 1.2))
    opacity = float(params.get('alpha', 1.0))
    if isinstance(colors, list):
        if len(colors) != len(points):
            raise ValueError('Point-marker color list must match number of points')
        for point, color in zip(points, colors, strict=False):
            plotter.add_points(
                np.array([point]),
                color=color,
                opacity=opacity,
                point_size=point_size,
                render_points_as_spheres=True,
            )
        return
    plotter.add_points(
        points,
        color=colors,
        opacity=opacity,
        point_size=point_size,
        render_points_as_spheres=True,
    )


def _add_annotation(plotter: pv.Plotter, annotation: SceneAnnotation, style: StylePreset, layout: FigureLayout) -> None:
    if annotation.kind not in SUPPORTED_ANNOTATION_KINDS:
        raise KeyError(f'Unsupported geometry3d annotation kind for pyvista backend: {annotation.kind}')
    params = annotation.params
    color = _resolve_color(style, params) or '#ffffff'
    fontsize = int(params.get('fontsize', 12))

    if annotation.kind == 'text2d':
        width, height = _window_size(layout)
        position = (int(float(params['x']) * width), int(float(params['y']) * height))
        plotter.add_text(annotation.text or '', position=position, font_size=fontsize, color=color, viewport=False)
        return

    if annotation.kind == 'text3d':
        point = np.array([[float(params['x']), float(params['y']), float(params['z'])]])
        plotter.add_point_labels(
            point,
            [annotation.text or ''],
            font_size=max(10, fontsize),
            text_color=color,
            show_points=False,
            shape=None,
            fill_shape=False,
            background_opacity=0.0,
            always_visible=True,
            margin=0,
        )
        return

    raise KeyError(f'Unhandled geometry3d annotation kind: {annotation.kind}')


def _configure_lighting(
    plotter: pv.Plotter,
    *,
    center: np.ndarray,
    position: np.ndarray,
    direction: np.ndarray,
    radius: float,
    camera: CameraPreset,
) -> None:
    view_dir = center - position
    view_dir = view_dir / max(float(np.linalg.norm(view_dir)), 1e-9)
    up = np.asarray(camera.view_up, dtype=float)
    up = up / max(float(np.linalg.norm(up)), 1e-9)
    right = np.cross(view_dir, up)
    if float(np.linalg.norm(right)) < 1e-9:
        right = np.array([1.0, 0.0, 0.0], dtype=float)
    right = right / max(float(np.linalg.norm(right)), 1e-9)

    light_position = position + 0.22 * radius * right + 0.18 * radius * up

    try:
        plotter.remove_all_lights()
    except Exception:
        pass

    key_light = pv.Light(
        position=tuple((position + 0.16 * radius * right + 0.14 * radius * up).tolist()),
        focal_point=tuple(center.tolist()),
        color='white',
        intensity=0.72,
        positional=False,
    )
    plotter.add_light(key_light)

    fill_light = pv.Light(
        position=tuple((position - 0.22 * radius * right - 0.08 * radius * up).tolist()),
        focal_point=tuple(center.tolist()),
        color='white',
        intensity=0.28,
        positional=False,
    )
    plotter.add_light(fill_light)

    rim_light = pv.Light(
        position=tuple((center - 0.45 * radius * view_dir + 0.10 * radius * up).tolist()),
        focal_point=tuple(center.tolist()),
        color='white',
        intensity=0.16,
        positional=False,
    )
    plotter.add_light(rim_light)


def _apply_layout(plotter: pv.Plotter, layout: FigureLayout, style: StylePreset, camera_name: str) -> None:
    center, position, direction, radius, camera = _apply_camera(plotter, layout, camera_name)
    _configure_lighting(plotter, center=center, position=position, direction=direction, radius=radius, camera=camera)
    if layout.show_axes:
        plotter.show_bounds(
            bounds=_resolved_bounds(layout, get_camera_preset(camera_name)),
            xtitle=layout.axis_labels[0],
            ytitle=layout.axis_labels[1],
            ztitle=layout.axis_labels[2],
            color=style.axis_label_color,
            font_size=14,
            use_3d_text=False,
            grid=None,
            location='outer',
            ticks='outside',
            minor_ticks=False,
            all_edges=True,
        )
    if layout.title:
        plotter.add_text(layout.title, position='upper_edge', font_size=20, color=style.title_color)


def render_scene(*, scene: SceneSpec, output_path: Path, camera_name: str, style_name: str) -> Path:
    scene.validate()
    style = get_style_preset(style_name)
    window_size = _window_size(scene.layout)
    plotter = pv.Plotter(off_screen=True, window_size=window_size)
    plotter.set_background(style.background)

    for obj in scene.objects:
        if obj.kind not in SUPPORTED_OBJECT_KINDS:
            raise KeyError(f'Unsupported geometry3d object kind for pyvista backend: {obj.kind}')
        if obj.kind == 'sampled_surface':
            _add_surface(plotter, obj, style)
        elif obj.kind == 'sampled_wireframe':
            _add_wireframe(plotter, obj, style)
        elif obj.kind == 'vector_set':
            _add_vectors(plotter, obj, style)
        elif obj.kind == 'point_markers':
            _add_points(plotter, obj, style)
        else:
            raise KeyError(f'Unhandled geometry3d object kind: {obj.kind}')

    _apply_layout(plotter, scene.layout, style, camera_name)

    for annotation in scene.annotations:
        _add_annotation(plotter, annotation, style, scene.layout)

    ensure_parent(output_path)
    plotter.show(screenshot=str(output_path), auto_close=True)
    return output_path
