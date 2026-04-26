from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np

from geometry3d.cameras import get_camera_preset
from geometry3d.primitives import (
    DEFAULT_MESH_RESOLUTION,
    angular_grid,
    half_space_mask,
    half_sphere_shell_objects,
    sampled_surface_and_wireframe,
    sphere_shell_coordinates,
    sphere_shell_objects,
    vector_object,
)
from geometry3d.scene_spec import FigureLayout, OutputTarget, SceneAnnotation, SceneObject, SceneSpec


OBJECT_TRANSLATABLE_KEYS = {
    'sampled_surface': ('x', 'y', 'z'),
    'sampled_wireframe': ('x', 'y', 'z'),
    'vector_set': ('x', 'y', 'z'),
    'point_markers': ('x', 'y', 'z'),
}

P_F = 1.0
P = P_F
M = float(np.sqrt(P_F**2 + P**2))

THETA_GRID, PHI_GRID = angular_grid(
    theta_samples=DEFAULT_MESH_RESOLUTION.theta_samples,
    phi_samples=DEFAULT_MESH_RESOLUTION.phi_samples,
)
UNIT_X, UNIT_Y, UNIT_Z = sphere_shell_coordinates(1.0, theta=THETA_GRID, phi=PHI_GRID)
CUTAWAY_MASK = half_space_mask(UNIT_X, UNIT_Y, UNIT_Z, axis='y', keep='positive')
PLUS_CHANNEL_MASK = CUTAWAY_MASK & (UNIT_X >= 0.0)
MINUS_CHANNEL_MASK = CUTAWAY_MASK & (UNIT_X <= 0.0)
FERMIC_CAP_MASK = CUTAWAY_MASK & (UNIT_X <= -0.68)
FERMIC_BODY_MASK = CUTAWAY_MASK & ~FERMIC_CAP_MASK
SHELL_MANUSCRIPT_CAMERA = get_camera_preset('shell-manuscript')


def _camera_basis(camera_name: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    camera = get_camera_preset(camera_name)
    az = np.deg2rad(camera.azimuth_deg)
    el = np.deg2rad(camera.elevation_deg)
    camera_dir = np.array([
        np.cos(el) * np.cos(az),
        np.cos(el) * np.sin(az),
        np.sin(el),
    ])
    camera_dir = camera_dir / np.linalg.norm(camera_dir)
    view_up = np.array(camera.view_up, dtype=float)
    right = np.cross(view_up, camera_dir)
    right = right / np.linalg.norm(right)
    screen_up = np.cross(camera_dir, right)
    screen_up = screen_up / np.linalg.norm(screen_up)
    return camera_dir, right, screen_up


def _uniform_panel_a_arrow_directions(target_count: int = 63) -> np.ndarray:
    _, right, screen_up = _camera_basis('shell-manuscript')

    candidates = np.column_stack([
        UNIT_X[CUTAWAY_MASK],
        UNIT_Y[CUTAWAY_MASK],
        UNIT_Z[CUTAWAY_MASK],
    ])
    # Keep the actual cutaway hemisphere, but do not asymmetrically throw away one side.
    # We only trim the extreme seam so the arrows can span the full visible annulus.
    candidates = candidates[candidates[:, 1] > 0.02]

    projected = np.column_stack([candidates @ right, candidates @ screen_up])
    centroid = projected.mean(axis=0)
    seed_idx = int(np.argmin(np.sum((projected - centroid) ** 2, axis=1)))
    selected_indices = [seed_idx]
    min_dist2 = np.sum((projected - projected[seed_idx]) ** 2, axis=1)

    while len(selected_indices) < min(target_count, len(candidates)):
        next_idx = int(np.argmax(min_dist2))
        selected_indices.append(next_idx)
        dist2 = np.sum((projected - projected[next_idx]) ** 2, axis=1)
        min_dist2 = np.minimum(min_dist2, dist2)

    selected = candidates[selected_indices]
    order = np.lexsort((projected[selected_indices, 1], projected[selected_indices, 0]))
    return selected[order]


def _directional_radius() -> np.ndarray:
    return M + 0.5 * P * np.cos(THETA_GRID)


def _directional_shell_objects(*, scalar_colored: bool = False) -> list[SceneObject]:
    directional_radius = _directional_radius()

    if scalar_colored:
        directional_x, directional_y, directional_z = sphere_shell_coordinates(
            directional_radius,
            theta=THETA_GRID,
            phi=PHI_GRID,
            mask=CUTAWAY_MASK,
        )
        dipole_scalar = np.where(CUTAWAY_MASK, np.cos(THETA_GRID), np.nan)
        return sampled_surface_and_wireframe(
            'directional-shell',
            x=directional_x,
            y=directional_y,
            z=directional_z,
            fill_color_key=None,
            fill_alpha=0.85,
            wire_color_key='directional_wire_plus',
            wire_alpha=0.12,
            wire_linewidth=0.34,
            face_scalar_field=dipole_scalar,
            colormap='coolwarm_r',
            shade=True,
            fill_zorder=6,
            wire_zorder=7,
        )

    plus_x, plus_y, plus_z = sphere_shell_coordinates(
        directional_radius,
        theta=THETA_GRID,
        phi=PHI_GRID,
        mask=PLUS_CHANNEL_MASK,
    )
    minus_x, minus_y, minus_z = sphere_shell_coordinates(
        directional_radius,
        theta=THETA_GRID,
        phi=PHI_GRID,
        mask=MINUS_CHANNEL_MASK,
    )

    objects: list[SceneObject] = []
    objects.extend(
        sampled_surface_and_wireframe(
            'directional-shell-plus',
            x=plus_x,
            y=plus_y,
            z=plus_z,
            fill_color_key='directional_fill_plus',
            fill_alpha=0.22,
            wire_color_key='directional_wire_plus',
            wire_alpha=0.34,
            wire_linewidth=0.45,
            shade=True,
            fill_zorder=6,
            wire_zorder=7,
        )
    )
    objects.extend(
        sampled_surface_and_wireframe(
            'directional-shell-minus',
            x=minus_x,
            y=minus_y,
            z=minus_z,
            fill_color_key='directional_fill_minus',
            fill_alpha=0.24,
            wire_color_key='directional_wire_minus',
            wire_alpha=0.30,
            wire_linewidth=0.42,
            shade=True,
            fill_zorder=6,
            wire_zorder=7,
        )
    )
    return objects


def _fermic_shell_objects(*, split_cap: bool = True, fill_alpha: float = 0.70, wire_alpha: float = 0.56) -> list[SceneObject]:
    if not split_cap:
        return sphere_shell_objects(
            'fermic-shell',
            radius=P_F,
            theta=THETA_GRID,
            phi=PHI_GRID,
            mask=CUTAWAY_MASK,
            fill_color_key='fermic_fill',
            fill_alpha=fill_alpha,
            wire_color_key='fermic_wire',
            wire_alpha=wire_alpha,
            wire_linewidth=0.58,
            shade=True,
            surface_zsort='max',
            fill_zorder=10,
            wire_zorder=11,
        )

    objects: list[SceneObject] = []
    objects.extend(
        sphere_shell_objects(
            'fermic-shell-cap',
            radius=P_F,
            theta=THETA_GRID,
            phi=PHI_GRID,
            mask=FERMIC_CAP_MASK,
            fill_color_key='fermic_cap_fill',
            fill_alpha=0.76,
            wire_color_key='fermic_cap_wire',
            wire_alpha=0.44,
            wire_linewidth=0.44,
            shade=True,
            surface_zsort='max',
            fill_zorder=8,
            wire_zorder=9,
        )
    )
    objects.extend(
        sphere_shell_objects(
            'fermic-shell-body',
            radius=P_F,
            theta=THETA_GRID,
            phi=PHI_GRID,
            mask=FERMIC_BODY_MASK,
            fill_color_key='fermic_fill',
            fill_alpha=fill_alpha,
            wire_color_key='fermic_wire',
            wire_alpha=wire_alpha,
            wire_linewidth=0.54,
            shade=True,
            surface_zsort='max',
            fill_zorder=10,
            wire_zorder=11,
        )
    )
    return objects


def _core_shell_objects(*, radius: float = M) -> list[SceneObject]:
    return half_sphere_shell_objects(
        'core-shell',
        radius=radius,
        theta=THETA_GRID,
        phi=PHI_GRID,
        cut_axis='y',
        keep='positive',
        fill_color_key='core_fill',
        fill_alpha=0.30,
        wire_color_key='core_wire',
        wire_alpha=0.44,
        wire_linewidth=0.50,
        shade=True,
        fill_zorder=2,
        wire_zorder=3,
    )


def _radial_arrow_groups(*, systematic: bool = False, linewidth: float | None = None, alpha: float | None = None) -> list[SceneObject]:
    radial_gap = M - P_F

    if systematic:
        directions = _uniform_panel_a_arrow_directions()
        starts = P_F * directions
        deltas = radial_gap * directions

        return [
            SceneObject(
                object_id='radial-arrows-systematic',
                kind='vector_set',
                params={
                    'x': starts[:, 0],
                    'y': starts[:, 1],
                    'z': starts[:, 2],
                    'u': deltas[:, 0],
                    'v': deltas[:, 1],
                    'w': deltas[:, 2],
                    'color_key': 'radial_arrow',
                    'linewidth': linewidth if linewidth is not None else 1.2,
                    'arrow_length_ratio': 0.24,
                    'alpha': alpha if alpha is not None else 0.64,
                    'ambient': 0.36,
                    'diffuse': 0.66,
                    'specular': 0.02,
                    'specular_power': 4.0,
                    'zorder': 20,
                },
            )
        ]

    theta_samples = np.deg2rad(np.arange(20, 161, 20))
    phi_samples = np.deg2rad(np.arange(0, 360, 18))
    groups = {
        'outer': {'x': [], 'y': [], 'z': [], 'u': [], 'v': [], 'w': [], 'linewidth': 1.9, 'alpha': 0.86},
        'mid': {'x': [], 'y': [], 'z': [], 'u': [], 'v': [], 'w': [], 'linewidth': 1.35, 'alpha': 0.62},
        'inner': {'x': [], 'y': [], 'z': [], 'u': [], 'v': [], 'w': [], 'linewidth': 0.92, 'alpha': 0.42},
    }

    for ti, theta0 in enumerate(theta_samples):
        for pi, phi0 in enumerate(phi_samples):
            nx = np.cos(theta0)
            ny = np.sin(theta0) * np.cos(phi0)
            nz = np.sin(theta0) * np.sin(phi0)
            if ny < 0.0:
                continue

            rim_weight = 1.0 - np.clip(abs(ny), 0.0, 1.0)
            x_weight = 0.5 * (1.0 + nx)
            if rim_weight < 0.22 and x_weight < 0.55:
                continue

            if x_weight > 0.72:
                if (ti + pi) % 3 != 0:
                    continue
                bucket = 'outer'
            elif x_weight > 0.42:
                if (ti + pi) % 2 != 0:
                    continue
                bucket = 'mid'
            else:
                bucket = 'inner'

            start = P_F * np.array([nx, ny, nz])
            delta = radial_gap * np.array([nx, ny, nz])
            groups[bucket]['x'].append(start[0])
            groups[bucket]['y'].append(start[1])
            groups[bucket]['z'].append(start[2])
            groups[bucket]['u'].append(delta[0])
            groups[bucket]['v'].append(delta[1])
            groups[bucket]['w'].append(delta[2])

    objects: list[SceneObject] = []
    for bucket, payload in groups.items():
        objects.append(
            SceneObject(
                object_id=f'radial-arrows-{bucket}',
                kind='vector_set',
                params={
                    'x': np.asarray(payload['x']),
                    'y': np.asarray(payload['y']),
                    'z': np.asarray(payload['z']),
                    'u': np.asarray(payload['u']),
                    'v': np.asarray(payload['v']),
                    'w': np.asarray(payload['w']),
                    'color_key': 'radial_arrow',
                    'linewidth': payload['linewidth'],
                    'arrow_length_ratio': 0.18,
                    'alpha': payload['alpha'],
                    'zorder': 20,
                },
            )
        )
    return objects


def _directional_channel_objects() -> list[SceneObject]:
    x_core_plus, x_core_minus = M, -M
    x_dir_plus, x_dir_minus = M + 0.5 * P, -(M - 0.5 * P)

    objects: list[SceneObject] = [
        vector_object(
            'directional-channel-plus-soft',
            start=(x_core_plus, 0.0, 0.0),
            end=(x_dir_plus, 0.0, 0.0),
            color='#dbeafe',
            linewidth=6.0,
            arrow_length_ratio=0.33,
            alpha=0.38,
            zorder=30,
        ),
        vector_object(
            'directional-channel-minus-soft',
            start=(x_core_minus, 0.0, 0.0),
            end=(x_dir_minus, 0.0, 0.0),
            color='#ffe4e6',
            linewidth=6.0,
            arrow_length_ratio=0.33,
            alpha=0.42,
            zorder=30,
        ),
        vector_object(
            'directional-channel-plus',
            start=(x_core_plus, 0.0, 0.0),
            end=(x_dir_plus, 0.0, 0.0),
            color_key='directional_plus',
            linewidth=3.8,
            arrow_length_ratio=0.38,
            alpha=1.0,
            zorder=31,
        ),
        vector_object(
            'directional-channel-minus',
            start=(x_core_minus, 0.0, 0.0),
            end=(x_dir_minus, 0.0, 0.0),
            color_key='directional_minus',
            linewidth=3.8,
            arrow_length_ratio=0.38,
            alpha=1.0,
            zorder=31,
        ),
        SceneObject(
            object_id='directional-channel-points',
            kind='point_markers',
            params={
                'x': np.array([x_dir_plus, x_dir_minus]),
                'y': np.array([0.0, 0.0]),
                'z': np.array([0.0, 0.0]),
                'color': ['#60a5fa', '#ef4444'],
                'size': 46,
                'zorder': 32,
            },
        ),
    ]
    return objects


def _dipole_deformation_objects() -> list[SceneObject]:
    theta_samples = np.deg2rad([24, 42, 60, 78, 102, 120, 138, 156])
    phi_samples = np.deg2rad([-72, -42, -12, 18, 48, 78])

    plus = {'x': [], 'y': [], 'z': [], 'u': [], 'v': [], 'w': []}
    minus = {'x': [], 'y': [], 'z': [], 'u': [], 'v': [], 'w': []}

    for theta0 in theta_samples:
        for phi0 in phi_samples:
            nx = np.cos(theta0)
            ny = np.sin(theta0) * np.cos(phi0)
            nz = np.sin(theta0) * np.sin(phi0)
            if ny < 0.0:
                continue
            if abs(nx) < 0.24:
                continue

            amplitude = 0.5 * P * abs(nx)
            start = M * np.array([nx, ny, nz])
            direction = amplitude * np.array([nx, ny, nz])

            target = plus if nx > 0.0 else minus
            target['x'].append(start[0])
            target['y'].append(start[1])
            target['z'].append(start[2])
            if nx > 0.0:
                target['u'].append(direction[0])
                target['v'].append(direction[1])
                target['w'].append(direction[2])
            else:
                target['u'].append(-direction[0])
                target['v'].append(-direction[1])
                target['w'].append(-direction[2])

    return [
        SceneObject(
            object_id='dipole-plus-arrows-underlay',
            kind='vector_set',
            params={
                'x': np.asarray(plus['x']),
                'y': np.asarray(plus['y']),
                'z': np.asarray(plus['z']),
                'u': np.asarray(plus['u']),
                'v': np.asarray(plus['v']),
                'w': np.asarray(plus['w']),
                'color_key': 'directional_plus_soft',
                'linewidth': 3.0,
                'arrow_length_ratio': 0.17,
                'alpha': 0.28,
                'ambient': 0.55,
                'diffuse': 0.45,
                'specular': 0.01,
                'specular_power': 3.0,
                'zorder': 25,
            },
        ),
        SceneObject(
            object_id='dipole-minus-arrows-underlay',
            kind='vector_set',
            params={
                'x': np.asarray(minus['x']),
                'y': np.asarray(minus['y']),
                'z': np.asarray(minus['z']),
                'u': np.asarray(minus['u']),
                'v': np.asarray(minus['v']),
                'w': np.asarray(minus['w']),
                'color_key': 'directional_minus_soft',
                'linewidth': 3.0,
                'arrow_length_ratio': 0.17,
                'alpha': 0.30,
                'ambient': 0.55,
                'diffuse': 0.45,
                'specular': 0.01,
                'specular_power': 3.0,
                'zorder': 25,
            },
        ),
        SceneObject(
            object_id='dipole-plus-arrows',
            kind='vector_set',
            params={
                'x': np.asarray(plus['x']),
                'y': np.asarray(plus['y']),
                'z': np.asarray(plus['z']),
                'u': np.asarray(plus['u']),
                'v': np.asarray(plus['v']),
                'w': np.asarray(plus['w']),
                'color_key': 'dipole_plus',
                'linewidth': 2.15,
                'arrow_length_ratio': 0.17,
                'alpha': 0.82,
                'ambient': 0.42,
                'diffuse': 0.62,
                'specular': 0.02,
                'specular_power': 4.0,
                'zorder': 26,
            },
        ),
        SceneObject(
            object_id='dipole-minus-arrows',
            kind='vector_set',
            params={
                'x': np.asarray(minus['x']),
                'y': np.asarray(minus['y']),
                'z': np.asarray(minus['z']),
                'u': np.asarray(minus['u']),
                'v': np.asarray(minus['v']),
                'w': np.asarray(minus['w']),
                'color_key': 'dipole_minus',
                'linewidth': 2.15,
                'arrow_length_ratio': 0.17,
                'alpha': 0.82,
                'ambient': 0.42,
                'diffuse': 0.62,
                'specular': 0.02,
                'specular_power': 4.0,
                'zorder': 26,
            },
        ),
        vector_object(
            'dipole-plus-axis-soft',
            start=(M, 0.0, 0.0),
            end=(M + 0.5 * P, 0.0, 0.0),
            color_key='directional_plus_soft',
            linewidth=7.8,
            arrow_length_ratio=0.34,
            alpha=0.55,
            zorder=29,
        ),
        vector_object(
            'dipole-minus-axis-soft',
            start=(-M, 0.0, 0.0),
            end=(-(M - 0.5 * P), 0.0, 0.0),
            color_key='directional_minus_soft',
            linewidth=7.8,
            arrow_length_ratio=0.34,
            alpha=0.58,
            zorder=29,
        ),
        vector_object(
            'dipole-plus-axis',
            start=(M, 0.0, 0.0),
            end=(M + 0.5 * P, 0.0, 0.0),
            color_key='dipole_plus',
            linewidth=6.2,
            arrow_length_ratio=0.38,
            alpha=0.98,
            zorder=30,
        ),
        vector_object(
            'dipole-minus-axis',
            start=(-M, 0.0, 0.0),
            end=(-(M - 0.5 * P), 0.0, 0.0),
            color_key='dipole_minus',
            linewidth=6.2,
            arrow_length_ratio=0.38,
            alpha=0.98,
            zorder=30,
        ),
        SceneObject(
            object_id='dipole-axis-points',
            kind='point_markers',
            params={
                'x': np.array([M + 0.5 * P, -(M - 0.5 * P)]),
                'y': np.array([0.0, 0.0]),
                'z': np.array([0.0, 0.0]),
                'color': ['#2563eb', '#dc2626'],
                'size': 54,
                'zorder': 31,
            },
        ),
    ]


def _copy_object(
    obj: SceneObject,
    *,
    object_id_prefix: str | None = None,
    param_overrides: dict | None = None,
) -> SceneObject:
    params = dict(obj.params)
    if param_overrides:
        params.update(param_overrides)
    return SceneObject(
        object_id=f'{object_id_prefix}{obj.object_id}' if object_id_prefix else obj.object_id,
        kind=obj.kind,
        params=params,
        style=obj.style,
        backend_hints=dict(obj.backend_hints),
    )


def _translate_object(obj: SceneObject, *, dx: float = 0.0, dy: float = 0.0, dz: float = 0.0, object_id_prefix: str | None = None) -> SceneObject:
    params = dict(obj.params)
    for key in OBJECT_TRANSLATABLE_KEYS.get(obj.kind, ()):
        params[key] = np.asarray(params[key]) + {'x': dx, 'y': dy, 'z': dz}[key]
    return SceneObject(
        object_id=f'{object_id_prefix}{obj.object_id}' if object_id_prefix else obj.object_id,
        kind=obj.kind,
        params=params,
        style=obj.style,
        backend_hints=dict(obj.backend_hints),
    )


def _translate_annotation(
    ann: SceneAnnotation,
    *,
    dx: float = 0.0,
    dy: float = 0.0,
    dz: float = 0.0,
    annotation_id_prefix: str | None = None,
) -> SceneAnnotation:
    params = dict(ann.params)
    if ann.kind == 'text3d':
        params['x'] = float(params['x']) + dx
        params['y'] = float(params['y']) + dy
        params['z'] = float(params['z']) + dz
    return SceneAnnotation(
        annotation_id=f'{annotation_id_prefix}{ann.annotation_id}' if annotation_id_prefix else ann.annotation_id,
        kind=ann.kind,
        text=ann.text,
        params=params,
    )


def _annotations() -> list[SceneAnnotation]:
    x_dir_plus = M + 0.5 * P
    x_dir_minus = -(M - 0.5 * P)
    return [
        SceneAnnotation(
            annotation_id='label-plus',
            kind='text3d',
            text=r'$p_{\hat n^+}$',
            params={'x': x_dir_plus + 0.07, 'y': 0.14, 'z': 0.04, 'fontsize': 13, 'color_key': 'label_plus'},
        ),
        SceneAnnotation(
            annotation_id='label-minus',
            kind='text3d',
            text=r'$p_{\hat n^-}$',
            params={'x': x_dir_minus - 0.55, 'y': -0.18, 'z': 0.04, 'fontsize': 13, 'color_key': 'label_minus'},
        ),
        SceneAnnotation(
            annotation_id='formula',
            kind='text2d',
            text=r'$p_{\hat n}(\theta)=M+\frac{1}{2}p\cos\theta$',
            params={'x': 0.02, 'y': 0.945, 'fontsize': 12, 'color_key': 'text_primary'},
        ),
        SceneAnnotation(
            annotation_id='fermic-shell-note',
            kind='text2d',
            text=r'fermic shell ($p_f$)',
            params={'x': 0.02, 'y': 0.885, 'fontsize': 11, 'color_key': 'text_secondary'},
        ),
        SceneAnnotation(
            annotation_id='core-shell-note',
            kind='text2d',
            text=r'core shell ($M$)',
            params={'x': 0.02, 'y': 0.858, 'fontsize': 11, 'color_key': 'text_core'},
        ),
        SceneAnnotation(
            annotation_id='directional-shell-note',
            kind='text2d',
            text=r'directional shell ($p_{\hat n}$)',
            params={'x': 0.02, 'y': 0.831, 'fontsize': 11, 'color_key': 'text_directional'},
        ),
        SceneAnnotation(
            annotation_id='axis-note',
            kind='text2d',
            text=r'Here the chosen direction $\hat n$ is drawn along the $x$-axis.',
            params={'x': 0.02, 'y': 0.801, 'fontsize': 10, 'color_key': 'text_note'},
        ),
    ]


def _panel_label(annotation_id: str, text: str, x: float, y: float) -> SceneAnnotation:
    return SceneAnnotation(
        annotation_id=annotation_id,
        kind='text2d',
        text=text,
        params={'x': x, 'y': y, 'fontsize': 15, 'color_key': 'text_primary'},
    )


def _panel_a_annotations() -> list[SceneAnnotation]:
    return [
        SceneAnnotation(
            annotation_id='panel-a-fermic-label',
            kind='text3d',
            text=r'$p_f$',
            params={'x': -0.62, 'y': -0.16, 'z': 0.02, 'fontsize': 14, 'color_key': 'text_secondary'},
        ),
        SceneAnnotation(
            annotation_id='panel-a-core-label',
            kind='text3d',
            text=r'$M$',
            params={'x': 1.76, 'y': 0.62, 'z': 0.88, 'fontsize': 14, 'color_key': 'text_core'},
        ),
    ]


def _panel_b_annotations() -> list[SceneAnnotation]:
    return [
        SceneAnnotation(
            annotation_id='panel-b-plus-half-label',
            kind='text2d',
            text=r'$+\,\frac{p}{2}$',
            params={'x': 0.918, 'y': 0.402, 'fontsize': 39, 'color_key': 'dipole_plus'},
        ),
        SceneAnnotation(
            annotation_id='panel-b-minus-half-label',
            kind='text2d',
            text=r'$-\,\frac{p}{2}$',
            params={'x': 0.030, 'y': 0.520, 'fontsize': 39, 'color_key': 'dipole_minus'},
        ),
    ]



def _panel_a_objects() -> list[SceneObject]:
    objects: list[SceneObject] = []
    objects.extend(
        _copy_object(obj, object_id_prefix='panel-a-', param_overrides={'alpha': 0.32} if obj.kind == 'sampled_surface' and obj.object_id.startswith('core-shell') else {'alpha': 0.44, 'linewidth': 0.56} if obj.kind == 'sampled_wireframe' and obj.object_id.startswith('core-shell') else None)
        for obj in _core_shell_objects()
    )
    objects.extend(
        _copy_object(
            obj,
            object_id_prefix='panel-a-',
            param_overrides=(
                {'alpha': 1.0} if obj.kind == 'sampled_surface' else {'alpha': 0.92, 'linewidth': 0.68} if obj.kind == 'sampled_wireframe' else None
            ),
        )
        for obj in _fermic_shell_objects(split_cap=False, fill_alpha=1.0, wire_alpha=0.92)
    )
    objects.extend(
        _copy_object(obj, object_id_prefix='panel-a-')
        for obj in _radial_arrow_groups(systematic=True, linewidth=2.35, alpha=0.82)
    )
    return objects



def _panel_b_objects() -> list[SceneObject]:
    objects: list[SceneObject] = []
    objects.extend(
        _copy_object(obj, object_id_prefix='panel-b-', param_overrides={'alpha': 0.22, 'ambient': 0.30, 'diffuse': 0.66, 'specular': 0.02} if obj.kind == 'sampled_surface' and obj.object_id.startswith('core-shell') else {'alpha': 0.48, 'linewidth': 0.62, 'ambient': 0.52, 'diffuse': 0.46, 'specular': 0.01, 'specular_power': 3.0} if obj.kind == 'sampled_wireframe' and obj.object_id.startswith('core-shell') else None)
        for obj in _core_shell_objects(radius=M)
    )
    objects.extend(
        _copy_object(
            obj,
            object_id_prefix='panel-b-',
            param_overrides=(
                None if obj.kind == 'sampled_surface' else
                {'alpha': 0.18, 'linewidth': 0.30, 'ambient': 0.26, 'diffuse': 0.50, 'specular': 0.01, 'specular_power': 3.0} if obj.kind == 'sampled_wireframe' else None
            ),
        )
        for obj in _directional_shell_objects(scalar_colored=True)
    )
    objects.extend(
        _copy_object(obj, object_id_prefix='panel-b-')
        for obj in _dipole_deformation_objects()
    )
    return objects



def build_foundations_shells_scene() -> SceneSpec:
    assert abs(M - np.sqrt(2) * P_F) < 1e-12

    objects: list[SceneObject] = []
    objects.extend(_core_shell_objects())
    objects.extend(_directional_shell_objects())
    objects.extend(_fermic_shell_objects())
    objects.extend(_directional_channel_objects())
    objects.extend(_radial_arrow_groups())

    return SceneSpec(
        family='foundations-shells',
        scene_id='foundations-shells',
        default_camera='shell-manuscript',
        default_style='shell-dark-manuscript',
        layout=FigureLayout(
            figsize=(13.5, 9.0),
            dpi=220,
            axis_labels=('x', 'y', 'z'),
            show_axes=True,
            show_grid=False,
            title='Fermic / Core / directional shells',
            bbox_inches='tight',
        ),
        outputs=[
            OutputTarget(
                output_id='canonical_png',
                kind='canonical_png',
                filename='foundations-shells.png',
                subdir='canonical',
            )
        ],
        objects=objects,
        annotations=_annotations(),
        metadata={
            'conceptual_job': 'Show fermic, core, and directional shells with the directional channels along a chosen x-axis cutaway view.',
            'migration_source': 'figures/src/foundations/foundations_shells.py',
            'scene_strategy': 'Fresh family-local rebuild from shell primitives, cutaway masks, and explicit channel geometry.',
        },
    )


def build_foundations_shells_panel_a_scene() -> SceneSpec:
    assert abs(M - np.sqrt(2) * P_F) < 1e-12

    return SceneSpec(
        family='foundations-shells',
        scene_id='foundations-shells-panel-a',
        default_camera='shell-manuscript',
        default_style='shell-light-manuscript',
        layout=FigureLayout(
            figsize=(8.0, 7.4),
            dpi=220,
            xlim=(-1.9, 2.2),
            ylim=(-1.7, 1.7),
            zlim=(-1.7, 1.7),
            axis_labels=('x', 'y', 'z'),
            show_axes=False,
            show_grid=False,
            title=None,
            bbox_inches='tight',
        ),
        outputs=[
            OutputTarget(
                output_id='canonical_png',
                kind='canonical_png',
                filename='foundations-shells-panel-a.png',
                subdir='canonical',
            )
        ],
        objects=_panel_a_objects(),
        annotations=_panel_a_annotations(),
        metadata={
            'conceptual_job': 'Separate panel showing the shell-language relation between the fermic shell and the core shell.',
        },
    )



def build_foundations_shells_panel_b_scene() -> SceneSpec:
    assert abs(M - np.sqrt(2) * P_F) < 1e-12

    return SceneSpec(
        family='foundations-shells',
        scene_id='foundations-shells-panel-b',
        default_camera='shell-manuscript',
        default_style='shell-light-manuscript',
        layout=FigureLayout(
            figsize=(8.0, 7.4),
            dpi=220,
            xlim=(-2.65, 2.90),
            ylim=(-1.95, 1.70),
            zlim=(-1.75, 1.75),
            axis_labels=('x', 'y', 'z'),
            show_axes=False,
            show_grid=False,
            title=None,
            bbox_inches='tight',
        ),
        outputs=[
            OutputTarget(
                output_id='canonical_png',
                kind='canonical_png',
                filename='foundations-shells-panel-b.png',
                subdir='canonical',
            )
        ],
        objects=_panel_b_objects(),
        annotations=_panel_b_annotations(),
        metadata={
            'conceptual_job': 'Separate panel showing the directional shell relative to the core shell for a chosen direction.',
        },
    )



def build_foundations_shells_split_scene() -> SceneSpec:
    assert abs(M - np.sqrt(2) * P_F) < 1e-12

    left_shift = -2.20
    right_shift = 2.30

    left_objects: list[SceneObject] = []
    left_objects.extend(
        _translate_object(obj, dx=left_shift, object_id_prefix='left-')
        for obj in _panel_a_objects()
    )

    right_objects: list[SceneObject] = []
    right_objects.extend(
        _translate_object(obj, dx=right_shift, object_id_prefix='right-')
        for obj in _panel_b_objects()
    )

    objects = list(left_objects) + list(right_objects)

    annotations: list[SceneAnnotation] = [
        _panel_label('panel-a', '(a)', 0.07, 0.92),
        _panel_label('panel-b', '(b)', 0.56, 0.92),
        SceneAnnotation(
            annotation_id='left-note',
            kind='text2d',
            text=r'fermic shell and core shell',
            params={'x': 0.13, 'y': 0.865, 'fontsize': 12.5, 'color_key': 'text_primary'},
        ),
        SceneAnnotation(
            annotation_id='right-note',
            kind='text2d',
            text=r'core shell and directional shell',
            params={'x': 0.58, 'y': 0.865, 'fontsize': 12.5, 'color_key': 'text_primary'},
        ),
    ]
    annotations.extend(
        _translate_annotation(ann, dx=left_shift, annotation_id_prefix='left-')
        for ann in _panel_a_annotations()
    )
    annotations.extend(
        ann
        for ann in [
            SceneAnnotation(
                annotation_id='right-plus-half-label',
                kind='text2d',
                text=r'$+\,\frac{p}{2}$',
                params={'x': 0.93, 'y': 0.40, 'fontsize': 28, 'color_key': 'dipole_plus'},
            ),
            SceneAnnotation(
                annotation_id='right-minus-half-label',
                kind='text2d',
                text=r'$-\,\frac{p}{2}$',
                params={'x': 0.54, 'y': 0.47, 'fontsize': 28, 'color_key': 'dipole_minus'},
            ),
        ]
    )

    return SceneSpec(
        family='foundations-shells',
        scene_id='foundations-shells-split',
        default_camera='shell-manuscript',
        default_style='shell-light-manuscript',
        layout=FigureLayout(
            figsize=(16.2, 8.6),
            dpi=220,
            xlim=(-4.55, 6.25),
            ylim=(-2.25, 2.0),
            zlim=(-2.0, 2.0),
            axis_labels=('x', 'y', 'z'),
            show_axes=False,
            show_grid=False,
            title=None,
            bbox_inches=None,
        ),
        outputs=[
            OutputTarget(
                output_id='canonical_png',
                kind='canonical_png',
                filename='foundations-shells-split.png',
                subdir='canonical',
            )
        ],
        objects=objects,
        annotations=annotations,
        metadata={
            'conceptual_job': 'Pedagogically staged two-panel shell figure showing the relation of the fermic and core shells, then the directional shell relative to the core shell.',
            'arrow_semantics': 'Arrows indicate constructive shell-language relations between descriptions, not literal temporal dynamics.',
            'scene_strategy': 'Two translated manuscript-ready panel assemblies in one figure so the family keeps both the inherited single-view scene and the staged two-panel scene.',
        },
    )



def post_render(*, scene: SceneSpec, output_path: Path, manifest, family, backend_name: str, camera_name: str, style_name: str) -> None:
    canonical_backend = getattr(family, 'canonical_backend', None) or family.default_backend
    if backend_name != canonical_backend or scene.scene_id != 'foundations-shells':
        return
    legacy_output = manifest.project_root / 'figures' / 'build' / 'foundations' / 'foundations-shells.png'
    legacy_output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(output_path, legacy_output)
