"""Working matplotlib backend for the first real geometry3d path."""

from __future__ import annotations

from pathlib import Path
import math

import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import colormaps
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

from ..cameras import get_camera_preset
from ..exporters import ensure_parent
from ..primitives import SUPPORTED_ANNOTATION_KINDS, SUPPORTED_OBJECT_KINDS
from ..scene_spec import FigureLayout, SceneAnnotation, SceneObject, SceneSpec
from ..styles import StylePreset, get_style_preset


def _resolved_limits(layout: FigureLayout, camera_name: str) -> tuple[tuple[float, float] | None, tuple[float, float] | None, tuple[float, float] | None]:
    camera = get_camera_preset(camera_name)
    return camera.xlim or layout.xlim, camera.ylim or layout.ylim, camera.zlim or layout.zlim


def _calibrated_orthographic_limits(
    xlim: tuple[float, float] | None,
    ylim: tuple[float, float] | None,
    zlim: tuple[float, float] | None,
    *,
    camera_name: str,
) -> tuple[tuple[float, float] | None, tuple[float, float] | None, tuple[float, float] | None]:
    camera = get_camera_preset(camera_name)
    if camera.orthographic_scale is None or ylim is None:
        return xlim, ylim, zlim

    y_center = 0.5 * (ylim[0] + ylim[1])
    y_half = 0.5 * (ylim[1] - ylim[0])
    if y_half <= 0:
        return xlim, ylim, zlim

    scale_factor = float(camera.orthographic_scale) / float(y_half)

    def scale_limits(lims: tuple[float, float] | None, axis_scale: float = 1.0) -> tuple[float, float] | None:
        if lims is None:
            return None
        center = 0.5 * (lims[0] + lims[1])
        half = 0.5 * (lims[1] - lims[0]) * scale_factor * axis_scale
        return (center - half, center + half)

    axis_scale = camera.matplotlib_limit_scale or (1.0, 1.0, 1.0)
    return scale_limits(xlim, axis_scale[0]), scale_limits(ylim, axis_scale[1]), scale_limits(zlim, axis_scale[2])


def _isotropic_box_aspect(
    xlim: tuple[float, float] | None,
    ylim: tuple[float, float] | None,
    zlim: tuple[float, float] | None,
) -> tuple[float, float, float] | None:
    if xlim is None or ylim is None or zlim is None:
        return None
    xspan = float(xlim[1] - xlim[0])
    yspan = float(ylim[1] - ylim[0])
    zspan = float(zlim[1] - zlim[0])
    if xspan <= 0 or yspan <= 0 or zspan <= 0:
        return None
    return (xspan, yspan, zspan)


def _apply_layout(ax, layout: FigureLayout, camera_name: str, style_name: str) -> None:
    camera = get_camera_preset(camera_name)
    style = get_style_preset(style_name)
    xlim, ylim, zlim = _resolved_limits(layout, camera_name)

    if camera.projection_mode == 'orthographic':
        ax.set_proj_type('ortho')
        xlim, ylim, zlim = _calibrated_orthographic_limits(xlim, ylim, zlim, camera_name=camera_name)
    else:
        focal_length = 1.0 / math.tan(math.radians(camera.view_angle_deg) / 2.0)
        ax.set_proj_type('persp', focal_length=focal_length)

    ax.view_init(elev=camera.elevation_deg, azim=camera.azimuth_deg)
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)
    if zlim:
        ax.set_zlim(*zlim)
    isotropic_aspect = _isotropic_box_aspect(xlim, ylim, zlim)
    if isotropic_aspect is not None:
        ax.set_box_aspect(isotropic_aspect)

    if layout.show_axes:
        ax.set_xlabel(layout.axis_labels[0], color=style.axis_label_color, labelpad=8)
        ax.set_ylabel(layout.axis_labels[1], color=style.axis_label_color, labelpad=8)
        ax.set_zlabel(layout.axis_labels[2], color=style.axis_label_color, labelpad=8)
        ax.tick_params(colors=style.tick_color, labelsize=9)
    else:
        ax.set_axis_off()

    if layout.title:
        ax.set_title(layout.title, color=style.title_color, fontsize=13, pad=16)

    ax.grid(layout.show_grid)
    frame_color = style.frame_color or style.tick_color
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor(style.pane_rgba)
        axis.pane.set_edgecolor(frame_color)
        try:
            axis.pane.set_linewidth(0.9)
        except Exception:
            pass
        axis._axinfo['grid']['linewidth'] = 0.0
        axis._axinfo['axisline']['color'] = frame_color
        axis._axinfo['axisline']['linewidth'] = 1.05
        axis._axinfo['tick']['color'] = style.tick_color


def _resolve_color(style: StylePreset, params: dict, key: str = 'color'):
    palette_key = params.get(f'{key}_key')
    if palette_key:
        try:
            return style.palette[palette_key]
        except KeyError as exc:
            raise KeyError(f'Unknown style palette key: {palette_key}') from exc
    return params.get(key)


def _surface_facecolors(obj: SceneObject):
    params = obj.params
    if 'facecolors' in params:
        return np.asarray(params['facecolors'])
    if 'scalar_field' in params:
        scalars = np.asarray(params['scalar_field'])
        norm = Normalize(vmin=float(np.nanmin(scalars)), vmax=float(np.nanmax(scalars)))
        cmap = colormaps.get_cmap(params.get('colormap', 'viridis'))
        colors = cmap(norm(scalars))
        if 'alpha' in params:
            colors[..., 3] = float(params['alpha'])
        return colors
    return None


def _render_object(ax, obj: SceneObject, style: StylePreset) -> None:
    if obj.kind not in SUPPORTED_OBJECT_KINDS:
        raise KeyError(f'Unsupported geometry3d object kind for matplotlib backend: {obj.kind}')

    params = obj.params
    if obj.kind == 'sampled_surface':
        kwargs = {
            'linewidth': params.get('linewidth', 0),
            'edgecolor': params.get('edgecolor', 'none'),
            'antialiased': params.get('antialiased', True),
            'shade': params.get('shade', True),
            'zsort': params.get('zsort', 'average'),
            'zorder': params.get('zorder'),
        }
        resolved_color = _resolve_color(style, params)
        if resolved_color is not None:
            kwargs['color'] = resolved_color
        if 'alpha' in params:
            kwargs['alpha'] = params['alpha']
        facecolors = _surface_facecolors(obj)
        if facecolors is not None:
            kwargs['facecolors'] = facecolors
            kwargs.pop('color', None)
        ax.plot_surface(np.asarray(params['x']), np.asarray(params['y']), np.asarray(params['z']), **kwargs)
        return

    if obj.kind == 'sampled_wireframe':
        ax.plot_wireframe(
            np.asarray(params['x']),
            np.asarray(params['y']),
            np.asarray(params['z']),
            rstride=int(params.get('rstride', 10)),
            cstride=int(params.get('cstride', 10)),
            color=_resolve_color(style, params) or '#ffffff',
            alpha=float(params.get('alpha', 1.0)),
            linewidth=float(params.get('linewidth', 0.5)),
            zorder=params.get('zorder'),
        )
        return

    if obj.kind == 'vector_set':
        ax.quiver(
            np.asarray(params['x']),
            np.asarray(params['y']),
            np.asarray(params['z']),
            np.asarray(params['u']),
            np.asarray(params['v']),
            np.asarray(params['w']),
            color=_resolve_color(style, params) or '#ffffff',
            linewidth=float(params.get('linewidth', 1.0)),
            arrow_length_ratio=float(params.get('arrow_length_ratio', 0.2)),
            alpha=float(params.get('alpha', 1.0)),
            zorder=params.get('zorder'),
        )
        return

    if obj.kind == 'point_markers':
        ax.scatter(
            np.asarray(params['x']),
            np.asarray(params['y']),
            np.asarray(params['z']),
            c=_resolve_color(style, params) or '#ffffff',
            s=float(params.get('size', 32)),
            alpha=float(params.get('alpha', 1.0)),
            zorder=params.get('zorder'),
        )
        return

    raise KeyError(f'Unhandled geometry3d object kind: {obj.kind}')


def _render_annotation(ax, annotation: SceneAnnotation, style: StylePreset) -> None:
    if annotation.kind not in SUPPORTED_ANNOTATION_KINDS:
        raise KeyError(f'Unsupported geometry3d annotation kind for matplotlib backend: {annotation.kind}')
    params = annotation.params
    if annotation.kind == 'text3d':
        ax.text(
            float(params['x']),
            float(params['y']),
            float(params['z']),
            annotation.text or '',
            color=_resolve_color(style, params) or '#ffffff',
            fontsize=float(params.get('fontsize', 12)),
        )
        return
    if annotation.kind == 'text2d':
        ax.text2D(
            float(params['x']),
            float(params['y']),
            annotation.text or '',
            transform=ax.transAxes,
            color=_resolve_color(style, params) or '#ffffff',
            fontsize=float(params.get('fontsize', 12)),
        )
        return
    raise KeyError(f'Unhandled geometry3d annotation kind: {annotation.kind}')


def render_scene(*, scene: SceneSpec, output_path: Path, camera_name: str, style_name: str) -> Path:
    scene.validate()
    style = get_style_preset(style_name)
    fig = plt.figure(figsize=scene.layout.figsize, dpi=scene.layout.dpi)
    ax = fig.add_subplot(111, projection='3d', computed_zorder=False)
    fig.patch.set_facecolor(style.background)
    ax.set_facecolor(style.background)

    for obj in scene.objects:
        _render_object(ax, obj, style)
    for annotation in scene.annotations:
        _render_annotation(ax, annotation, style)
    _apply_layout(ax, scene.layout, camera_name, style_name)

    ensure_parent(output_path)
    plt.savefig(output_path, facecolor=fig.get_facecolor(), bbox_inches=scene.layout.bbox_inches)
    plt.close(fig)
    return output_path
