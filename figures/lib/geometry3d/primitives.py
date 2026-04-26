"""Shared primitive helpers for the current real geometry3d path.

Phase 3 adds first-class shared support for spherical shells and half-spherical
shells without widening the scene-object vocabulary more than needed.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .scene_spec import SceneObject

SUPPORTED_OBJECT_KINDS = {
    'sampled_surface',
    'sampled_wireframe',
    'vector_set',
    'point_markers',
}

SUPPORTED_ANNOTATION_KINDS = {
    'text2d',
    'text3d',
}

SUPPORTED_OUTPUT_KINDS = {
    'canonical_png',
    'preview_png',
}


@dataclass(frozen=True, slots=True)
class MeshResolution:
    theta_samples: int = 240
    phi_samples: int = 240
    wire_rstride: int = 8
    wire_cstride: int = 8


@dataclass(frozen=True, slots=True)
class BoundingBox:
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    zmin: float
    zmax: float

    @property
    def xspan(self) -> float:
        return self.xmax - self.xmin

    @property
    def yspan(self) -> float:
        return self.ymax - self.ymin

    @property
    def zspan(self) -> float:
        return self.zmax - self.zmin

    @property
    def center(self) -> tuple[float, float, float]:
        return (
            0.5 * (self.xmin + self.xmax),
            0.5 * (self.ymin + self.ymax),
            0.5 * (self.zmin + self.zmax),
        )


DEFAULT_MESH_RESOLUTION = MeshResolution()


def _axis_vector(axis: str) -> np.ndarray:
    basis = {
        'x': np.array([1.0, 0.0, 0.0], dtype=float),
        'y': np.array([0.0, 1.0, 0.0], dtype=float),
        'z': np.array([0.0, 0.0, 1.0], dtype=float),
    }.get(axis)
    if basis is None:
        raise ValueError(f'Unsupported coordinate axis: {axis!r}')
    return basis


def _length_map(lengths: float | tuple[float, float, float] | dict[str, float]) -> dict[str, float]:
    if isinstance(lengths, (int, float)):
        return {'x': float(lengths), 'y': float(lengths), 'z': float(lengths)}
    if isinstance(lengths, tuple):
        if len(lengths) != 3:
            raise ValueError('Coordinate-system length tuple must have exactly three entries')
        return {'x': float(lengths[0]), 'y': float(lengths[1]), 'z': float(lengths[2])}
    return {axis: float(lengths.get(axis, 1.0)) for axis in ('x', 'y', 'z')}


def _corner_coordinate(bounds: BoundingBox, axis: str, side: str) -> float:
    if axis == 'x':
        return bounds.xmin if side == 'min' else bounds.xmax
    if axis == 'y':
        return bounds.ymin if side == 'min' else bounds.ymax
    if axis == 'z':
        return bounds.zmin if side == 'min' else bounds.zmax
    raise ValueError(f'Unsupported bounding-box axis: {axis!r}')


def _axis_span(bounds: BoundingBox, axis: str) -> float:
    if axis == 'x':
        return bounds.xspan
    if axis == 'y':
        return bounds.yspan
    if axis == 'z':
        return bounds.zspan
    raise ValueError(f'Unsupported bounding-box axis: {axis!r}')


def _resolve_vector_direction(
    *,
    start: np.ndarray,
    direction: tuple[float, float, float] | np.ndarray | None,
    end: tuple[float, float, float] | np.ndarray | None,
    length: float | None,
    normalize_direction: bool,
) -> np.ndarray:
    if direction is None and end is None:
        raise ValueError('Provide either direction or end for a vector helper')
    if direction is not None and end is not None:
        raise ValueError('Provide direction or end, not both')

    if end is not None:
        vector = np.asarray(end, dtype=float) - start
    else:
        vector = np.asarray(direction, dtype=float)

    if normalize_direction:
        norm = float(np.linalg.norm(vector))
        if norm == 0.0:
            raise ValueError('Cannot normalize a zero vector')
        vector = vector / norm

    if length is not None:
        norm = float(np.linalg.norm(vector))
        if norm == 0.0:
            raise ValueError('Cannot assign a length to a zero vector')
        vector = (vector / norm) * float(length)

    return vector


def bounding_box_from_points(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    *,
    pad_fraction: float = 0.0,
) -> BoundingBox:
    """Build a bounding box from sampled coordinates, ignoring NaNs."""

    xmin = float(np.nanmin(x))
    xmax = float(np.nanmax(x))
    ymin = float(np.nanmin(y))
    ymax = float(np.nanmax(y))
    zmin = float(np.nanmin(z))
    zmax = float(np.nanmax(z))

    xpad = (xmax - xmin) * pad_fraction
    ypad = (ymax - ymin) * pad_fraction
    zpad = (zmax - zmin) * pad_fraction
    return BoundingBox(
        xmin=xmin - xpad,
        xmax=xmax + xpad,
        ymin=ymin - ypad,
        ymax=ymax + ypad,
        zmin=zmin - zpad,
        zmax=zmax + zpad,
    )


def angular_grid(
    *,
    theta_samples: int = DEFAULT_MESH_RESOLUTION.theta_samples,
    phi_samples: int = DEFAULT_MESH_RESOLUTION.phi_samples,
) -> tuple[np.ndarray, np.ndarray]:
    theta = np.linspace(0.0, np.pi, theta_samples)
    phi = np.linspace(0.0, 2.0 * np.pi, phi_samples)
    return np.meshgrid(theta, phi)


def sphere_shell_coordinates(
    radius: float | np.ndarray,
    *,
    theta: np.ndarray | None = None,
    phi: np.ndarray | None = None,
    theta_samples: int = DEFAULT_MESH_RESOLUTION.theta_samples,
    phi_samples: int = DEFAULT_MESH_RESOLUTION.phi_samples,
    pole_axis: str = 'x',
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return sampled coordinates for a spherical shell.

    `pole_axis='x'` preserves the shell-family convention already in use for the
    Foundations shell figure.
    """

    if theta is None or phi is None:
        theta, phi = angular_grid(theta_samples=theta_samples, phi_samples=phi_samples)

    radius_array = np.broadcast_to(np.asarray(radius, dtype=float), theta.shape)

    if pole_axis == 'x':
        x = radius_array * np.cos(theta)
        y = radius_array * np.sin(theta) * np.cos(phi)
        z = radius_array * np.sin(theta) * np.sin(phi)
    elif pole_axis == 'y':
        x = radius_array * np.sin(theta) * np.cos(phi)
        y = radius_array * np.cos(theta)
        z = radius_array * np.sin(theta) * np.sin(phi)
    elif pole_axis == 'z':
        x = radius_array * np.sin(theta) * np.cos(phi)
        y = radius_array * np.sin(theta) * np.sin(phi)
        z = radius_array * np.cos(theta)
    else:
        raise ValueError(f'Unsupported sphere pole axis: {pole_axis!r}')

    if mask is not None:
        x = np.where(mask, x, np.nan)
        y = np.where(mask, y, np.nan)
        z = np.where(mask, z, np.nan)

    return x, y, z


def half_space_mask(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    *,
    axis: str = 'y',
    keep: str = 'positive',
    include_boundary: bool = True,
) -> np.ndarray:
    """Return a mask that keeps one half-space of sampled coordinates."""

    axis_values = {'x': x, 'y': y, 'z': z}.get(axis)
    if axis_values is None:
        raise ValueError(f'Unsupported half-space axis: {axis!r}')

    if keep == 'positive':
        return axis_values >= 0.0 if include_boundary else axis_values > 0.0
    if keep == 'negative':
        return axis_values <= 0.0 if include_boundary else axis_values < 0.0
    raise ValueError(f'Unsupported half-space direction: {keep!r}')


def sampled_surface_and_wireframe(
    object_id_prefix: str,
    *,
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    fill_color_key: str | None = None,
    fill_alpha: float | None = None,
    wire_color_key: str,
    wire_alpha: float | None,
    wire_linewidth: float,
    face_scalar_field: np.ndarray | None = None,
    colormap: str | None = None,
    shade: bool = True,
    surface_zsort: str = 'average',
    fill_zorder: int | None = None,
    wire_zorder: int | None = None,
    wire_rstride: int = DEFAULT_MESH_RESOLUTION.wire_rstride,
    wire_cstride: int = DEFAULT_MESH_RESOLUTION.wire_cstride,
) -> list[SceneObject]:
    surface_params = {
        'x': x,
        'y': y,
        'z': z,
        'linewidth': 0,
        'edgecolor': 'none',
        'antialiased': True,
        'shade': shade,
        'zsort': surface_zsort,
        'zorder': fill_zorder,
    }
    if fill_color_key is not None:
        surface_params['color_key'] = fill_color_key
    if fill_alpha is not None:
        surface_params['alpha'] = fill_alpha
    if face_scalar_field is not None:
        surface_params['scalar_field'] = face_scalar_field
    if colormap is not None:
        surface_params['colormap'] = colormap

    return [
        SceneObject(
            object_id=f'{object_id_prefix}-surface',
            kind='sampled_surface',
            params=surface_params,
        ),
        SceneObject(
            object_id=f'{object_id_prefix}-wireframe',
            kind='sampled_wireframe',
            params={
                'x': x,
                'y': y,
                'z': z,
                'rstride': wire_rstride,
                'cstride': wire_cstride,
                'color_key': wire_color_key,
                'alpha': wire_alpha,
                'linewidth': wire_linewidth,
                'zorder': wire_zorder,
            },
        ),
    ]


def sphere_shell_objects(
    object_id_prefix: str,
    *,
    radius: float | np.ndarray,
    theta: np.ndarray | None = None,
    phi: np.ndarray | None = None,
    theta_samples: int = DEFAULT_MESH_RESOLUTION.theta_samples,
    phi_samples: int = DEFAULT_MESH_RESOLUTION.phi_samples,
    pole_axis: str = 'x',
    mask: np.ndarray | None = None,
    fill_color_key: str | None = None,
    fill_alpha: float | None = None,
    wire_color_key: str,
    wire_alpha: float | None,
    wire_linewidth: float,
    face_scalar_field: np.ndarray | None = None,
    colormap: str | None = None,
    shade: bool = True,
    surface_zsort: str = 'average',
    fill_zorder: int | None = None,
    wire_zorder: int | None = None,
    wire_rstride: int = DEFAULT_MESH_RESOLUTION.wire_rstride,
    wire_cstride: int = DEFAULT_MESH_RESOLUTION.wire_cstride,
) -> list[SceneObject]:
    x, y, z = sphere_shell_coordinates(
        radius,
        theta=theta,
        phi=phi,
        theta_samples=theta_samples,
        phi_samples=phi_samples,
        pole_axis=pole_axis,
        mask=mask,
    )
    return sampled_surface_and_wireframe(
        object_id_prefix,
        x=x,
        y=y,
        z=z,
        fill_color_key=fill_color_key,
        fill_alpha=fill_alpha,
        wire_color_key=wire_color_key,
        wire_alpha=wire_alpha,
        wire_linewidth=wire_linewidth,
        face_scalar_field=face_scalar_field,
        colormap=colormap,
        shade=shade,
        surface_zsort=surface_zsort,
        fill_zorder=fill_zorder,
        wire_zorder=wire_zorder,
        wire_rstride=wire_rstride,
        wire_cstride=wire_cstride,
    )


def half_sphere_shell_objects(
    object_id_prefix: str,
    *,
    radius: float | np.ndarray,
    theta: np.ndarray | None = None,
    phi: np.ndarray | None = None,
    theta_samples: int = DEFAULT_MESH_RESOLUTION.theta_samples,
    phi_samples: int = DEFAULT_MESH_RESOLUTION.phi_samples,
    pole_axis: str = 'x',
    cut_axis: str = 'y',
    keep: str = 'positive',
    extra_mask: np.ndarray | None = None,
    fill_color_key: str | None = None,
    fill_alpha: float | None = None,
    wire_color_key: str,
    wire_alpha: float | None,
    wire_linewidth: float,
    face_scalar_field: np.ndarray | None = None,
    colormap: str | None = None,
    shade: bool = True,
    surface_zsort: str = 'average',
    fill_zorder: int | None = None,
    wire_zorder: int | None = None,
    wire_rstride: int = DEFAULT_MESH_RESOLUTION.wire_rstride,
    wire_cstride: int = DEFAULT_MESH_RESOLUTION.wire_cstride,
) -> list[SceneObject]:
    x, y, z = sphere_shell_coordinates(
        radius,
        theta=theta,
        phi=phi,
        theta_samples=theta_samples,
        phi_samples=phi_samples,
        pole_axis=pole_axis,
    )
    mask = half_space_mask(x, y, z, axis=cut_axis, keep=keep)
    if extra_mask is not None:
        mask = mask & extra_mask
    x = np.where(mask, x, np.nan)
    y = np.where(mask, y, np.nan)
    z = np.where(mask, z, np.nan)
    return sampled_surface_and_wireframe(
        object_id_prefix,
        x=x,
        y=y,
        z=z,
        fill_color_key=fill_color_key,
        fill_alpha=fill_alpha,
        wire_color_key=wire_color_key,
        wire_alpha=wire_alpha,
        wire_linewidth=wire_linewidth,
        face_scalar_field=face_scalar_field,
        colormap=colormap,
        shade=shade,
        surface_zsort=surface_zsort,
        fill_zorder=fill_zorder,
        wire_zorder=wire_zorder,
        wire_rstride=wire_rstride,
        wire_cstride=wire_cstride,
    )


def coordinate_system_components(
    object_id_prefix: str,
    *,
    origin: tuple[float, float, float] = (0.0, 0.0, 0.0),
    lengths: float | tuple[float, float, float] | dict[str, float] = 1.0,
    axes: tuple[str, ...] = ('x', 'y', 'z'),
    axis_colors: dict[str, str] | None = None,
    axis_labels: dict[str, str] | None = None,
    linewidth: float = 2.2,
    arrow_length_ratio: float = 0.18,
    label_offset_scale: float = 1.08,
    include_origin_marker: bool = True,
    origin_color: str = '#ffffff',
    origin_size: float = 28.0,
    include_negative_axes: bool = False,
    zorder: int | None = None,
) -> tuple[list[SceneObject], list['SceneAnnotation']]:
    """Build a simple coordinate-system triad from shared scene objects.

    This helper stays backend-neutral by emitting the existing shared object and
    annotation kinds instead of introducing renderer-specific axis objects.
    """

    from .scene_spec import SceneAnnotation

    origin_array = np.asarray(origin, dtype=float)
    length_by_axis = _length_map(lengths)
    colors = {'x': '#ef4444', 'y': '#22c55e', 'z': '#60a5fa'}
    if axis_colors:
        colors.update(axis_colors)
    labels = {'x': 'x', 'y': 'y', 'z': 'z'}
    if axis_labels:
        labels.update(axis_labels)

    objects: list[SceneObject] = []
    annotations: list[SceneAnnotation] = []

    if include_origin_marker:
        objects.append(
            SceneObject(
                object_id=f'{object_id_prefix}-origin',
                kind='point_markers',
                params={
                    'x': np.array([origin_array[0]]),
                    'y': np.array([origin_array[1]]),
                    'z': np.array([origin_array[2]]),
                    'color': origin_color,
                    'size': origin_size,
                    'zorder': zorder,
                },
            )
        )

    for axis in axes:
        direction = _axis_vector(axis)
        length = length_by_axis[axis]
        tip = origin_array + length * direction
        objects.append(
            SceneObject(
                object_id=f'{object_id_prefix}-{axis}-axis',
                kind='vector_set',
                params={
                    'x': np.array([origin_array[0]]),
                    'y': np.array([origin_array[1]]),
                    'z': np.array([origin_array[2]]),
                    'u': np.array([length * direction[0]]),
                    'v': np.array([length * direction[1]]),
                    'w': np.array([length * direction[2]]),
                    'color': colors[axis],
                    'linewidth': linewidth,
                    'arrow_length_ratio': arrow_length_ratio,
                    'zorder': zorder,
                },
            )
        )
        label_point = origin_array + label_offset_scale * length * direction
        annotations.append(
            SceneAnnotation(
                annotation_id=f'{object_id_prefix}-{axis}-label',
                kind='text3d',
                text=labels[axis],
                params={
                    'x': float(label_point[0]),
                    'y': float(label_point[1]),
                    'z': float(label_point[2]),
                    'color': colors[axis],
                    'fontsize': 12,
                },
            )
        )

        if include_negative_axes:
            negative_tip = origin_array - length * direction
            objects.append(
                SceneObject(
                    object_id=f'{object_id_prefix}-{axis}-axis-negative',
                    kind='vector_set',
                    params={
                        'x': np.array([origin_array[0]]),
                        'y': np.array([origin_array[1]]),
                        'z': np.array([origin_array[2]]),
                        'u': np.array([-length * direction[0]]),
                        'v': np.array([-length * direction[1]]),
                        'w': np.array([-length * direction[2]]),
                        'color': colors[axis],
                        'linewidth': linewidth * 0.8,
                        'arrow_length_ratio': arrow_length_ratio,
                        'alpha': 0.45,
                        'zorder': zorder,
                    },
                )
            )
            negative_label_point = origin_array - label_offset_scale * length * direction
            annotations.append(
                SceneAnnotation(
                    annotation_id=f'{object_id_prefix}-{axis}-label-negative',
                    kind='text3d',
                    text=f'-{labels[axis]}',
                    params={
                        'x': float(negative_label_point[0]),
                        'y': float(negative_label_point[1]),
                        'z': float(negative_label_point[2]),
                        'color': colors[axis],
                        'fontsize': 11,
                    },
                )
            )

    return objects, annotations


def vector_object(
    object_id: str,
    *,
    start: tuple[float, float, float] = (0.0, 0.0, 0.0),
    direction: tuple[float, float, float] | np.ndarray | None = None,
    end: tuple[float, float, float] | np.ndarray | None = None,
    length: float | None = None,
    normalize_direction: bool = False,
    color: str = '#ffffff',
    color_key: str | None = None,
    linewidth: float = 2.0,
    arrow_length_ratio: float = 0.18,
    alpha: float = 1.0,
    zorder: int | None = None,
) -> SceneObject:
    """Build one backend-neutral vector object using the shared `vector_set` kind."""

    start_array = np.asarray(start, dtype=float)
    vector = _resolve_vector_direction(
        start=start_array,
        direction=direction,
        end=end,
        length=length,
        normalize_direction=normalize_direction,
    )

    params = {
        'x': np.array([start_array[0]]),
        'y': np.array([start_array[1]]),
        'z': np.array([start_array[2]]),
        'u': np.array([vector[0]]),
        'v': np.array([vector[1]]),
        'w': np.array([vector[2]]),
        'linewidth': linewidth,
        'arrow_length_ratio': arrow_length_ratio,
        'alpha': alpha,
        'zorder': zorder,
    }
    if color_key is not None:
        params['color_key'] = color_key
    else:
        params['color'] = color

    return SceneObject(
        object_id=object_id,
        kind='vector_set',
        params=params,
    )


def vector_components(
    object_id_prefix: str,
    *,
    start: tuple[float, float, float] = (0.0, 0.0, 0.0),
    direction: tuple[float, float, float] | np.ndarray | None = None,
    end: tuple[float, float, float] | np.ndarray | None = None,
    length: float | None = None,
    normalize_direction: bool = False,
    color: str = '#ffffff',
    color_key: str | None = None,
    linewidth: float = 2.0,
    arrow_length_ratio: float = 0.18,
    alpha: float = 1.0,
    zorder: int | None = None,
    label: str | None = None,
    label_color: str | None = None,
    label_offset_scale: float = 1.08,
    label_fontsize: float = 12.0,
) -> tuple[list[SceneObject], list['SceneAnnotation']]:
    """Build a vector plus optional label annotation from shared scene pieces."""

    from .scene_spec import SceneAnnotation

    start_array = np.asarray(start, dtype=float)
    vector = _resolve_vector_direction(
        start=start_array,
        direction=direction,
        end=end,
        length=length,
        normalize_direction=normalize_direction,
    )

    objects = [
        vector_object(
            f'{object_id_prefix}-vector',
            start=start,
            direction=tuple(vector.tolist()),
            color=color,
            color_key=color_key,
            linewidth=linewidth,
            arrow_length_ratio=arrow_length_ratio,
            alpha=alpha,
            zorder=zorder,
        )
    ]
    annotations: list[SceneAnnotation] = []

    if label is not None:
        label_point = start_array + label_offset_scale * vector
        annotations.append(
            SceneAnnotation(
                annotation_id=f'{object_id_prefix}-label',
                kind='text3d',
                text=label,
                params={
                    'x': float(label_point[0]),
                    'y': float(label_point[1]),
                    'z': float(label_point[2]),
                    'color': label_color or color,
                    'fontsize': label_fontsize,
                },
            )
        )

    return objects, annotations


def bounding_box_coordinate_system_components(
    object_id_prefix: str,
    *,
    bounds: BoundingBox,
    anchor_corner: tuple[str, str, str] = ('min', 'min', 'min'),
    depth_placement: str | None = None,
    axis_labels: dict[str, str] | None = None,
    axis_color: str | None = None,
    axis_colors: dict[str, str] | None = None,
    linewidth: float = 2.2,
    arrow_length_ratio: float = 0.18,
    label_offset_scale: float = 1.06,
    include_origin_marker: bool = True,
    origin_color: str = '#ffffff',
    origin_size: float = 28.0,
    zorder: int | None = None,
) -> tuple[list[SceneObject], list['SceneAnnotation']]:
    """Build a coordinate system anchored to one corner of a bounding box.

    `depth_placement` is a convenience option for moving the coordinate system
    between the front and back y-face of the box without manually changing the
    full `anchor_corner` tuple.
    """

    from .scene_spec import SceneAnnotation

    if depth_placement is not None:
        if depth_placement == 'front':
            anchor_corner = (anchor_corner[0], 'min', anchor_corner[2])
        elif depth_placement == 'back':
            anchor_corner = (anchor_corner[0], 'max', anchor_corner[2])
        else:
            raise ValueError("depth_placement must be 'front', 'back', or None")

    sides = dict(zip(('x', 'y', 'z'), anchor_corner, strict=True))
    origin = np.array([
        _corner_coordinate(bounds, 'x', sides['x']),
        _corner_coordinate(bounds, 'y', sides['y']),
        _corner_coordinate(bounds, 'z', sides['z']),
    ], dtype=float)

    colors = {'x': '#ef4444', 'y': '#22c55e', 'z': '#60a5fa'}
    if axis_color is not None:
        colors = {axis: axis_color for axis in ('x', 'y', 'z')}
    if axis_colors:
        colors.update(axis_colors)
    labels = {'x': 'x', 'y': 'y', 'z': 'z'}
    if axis_labels:
        labels.update(axis_labels)

    objects: list[SceneObject] = []
    annotations: list[SceneAnnotation] = []

    if include_origin_marker:
        objects.append(
            SceneObject(
                object_id=f'{object_id_prefix}-origin',
                kind='point_markers',
                params={
                    'x': np.array([origin[0]]),
                    'y': np.array([origin[1]]),
                    'z': np.array([origin[2]]),
                    'color': origin_color,
                    'size': origin_size,
                    'zorder': zorder,
                },
            )
        )

    for axis in ('x', 'y', 'z'):
        direction = _axis_vector(axis)
        sign = 1.0 if sides[axis] == 'min' else -1.0
        length = _axis_span(bounds, axis)
        objects.append(
            SceneObject(
                object_id=f'{object_id_prefix}-{axis}-axis',
                kind='vector_set',
                params={
                    'x': np.array([origin[0]]),
                    'y': np.array([origin[1]]),
                    'z': np.array([origin[2]]),
                    'u': np.array([sign * length * direction[0]]),
                    'v': np.array([sign * length * direction[1]]),
                    'w': np.array([sign * length * direction[2]]),
                    'color': colors[axis],
                    'linewidth': linewidth,
                    'arrow_length_ratio': arrow_length_ratio,
                    'zorder': zorder,
                },
            )
        )
        label_point = origin + sign * label_offset_scale * length * direction
        annotations.append(
            SceneAnnotation(
                annotation_id=f'{object_id_prefix}-{axis}-label',
                kind='text3d',
                text=labels[axis],
                params={
                    'x': float(label_point[0]),
                    'y': float(label_point[1]),
                    'z': float(label_point[2]),
                    'color': colors[axis],
                    'fontsize': 12,
                },
            )
        )

    return objects, annotations
