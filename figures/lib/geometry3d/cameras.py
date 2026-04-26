"""Central camera presets for geometry3d."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CameraPreset:
    name: str
    azimuth_deg: float
    elevation_deg: float
    projection_mode: str = 'perspective'
    view_angle_deg: float = 28.0
    orthographic_scale: float | None = None
    matplotlib_limit_scale: tuple[float, float, float] | None = None
    zoom: float = 1.0
    distance_scale: float = 1.0
    view_up: tuple[float, float, float] = (0.0, 0.0, 1.0)
    xlim: tuple[float, float] | None = None
    ylim: tuple[float, float] | None = None
    zlim: tuple[float, float] | None = None
    box_aspect: tuple[float, float, float] | None = None
    framing: str = 'auto'
    note: str = ''


CAMERA_PRESETS: dict[str, CameraPreset] = {
    'shell-manuscript': CameraPreset(
        name='shell-manuscript',
        azimuth_deg=-70.0,
        elevation_deg=20.0,
        zoom=1.0,
        distance_scale=1.35,
        xlim=(-2.2, 2.8),
        ylim=(-2.0, 2.0),
        zlim=(-2.0, 2.0),
        box_aspect=(1.52, 1.1, 1.1),
        framing='tight',
        note='Canonical foundations-shells manuscript view, matched to the current published composition.',
    ),
    'shell-inspection-top': CameraPreset(
        name='shell-inspection-top',
        azimuth_deg=0.0,
        elevation_deg=90.0,
        zoom=1.0,
        distance_scale=1.2,
        xlim=(-2.0, 2.0),
        ylim=(-2.0, 2.0),
        zlim=(-2.0, 2.0),
        box_aspect=(1.0, 1.0, 1.0),
        framing='wide',
        note='Top-down shell inspection view for geometry sanity checks.',
    ),
    'manuscript-3q': CameraPreset(
        name='manuscript-3q',
        azimuth_deg=35.0,
        elevation_deg=24.0,
        zoom=1.0,
        distance_scale=1.3,
        framing='tight',
        note='Generic quarter-view manuscript preset reserved for later families.',
    ),
    'inspection-top': CameraPreset(
        name='inspection-top',
        azimuth_deg=0.0,
        elevation_deg=90.0,
        zoom=1.0,
        distance_scale=1.2,
        framing='wide',
        note='Generic top-down inspection preset reserved for later families.',
    ),
    'hero-cutaway': CameraPreset(
        name='hero-cutaway',
        azimuth_deg=48.0,
        elevation_deg=28.0,
        zoom=1.12,
        distance_scale=1.25,
        framing='presentational',
        note='Reserved for richer future cutaway and hero views.',
    ),
    'demo-front-cutaway': CameraPreset(
        name='demo-front-cutaway',
        azimuth_deg=-72.0,
        elevation_deg=16.0,
        projection_mode='orthographic',
        view_angle_deg=20.0,
        orthographic_scale=1.55,
        matplotlib_limit_scale=(0.50, 0.50, 0.50),
        zoom=1.0,
        distance_scale=1.42,
        xlim=(-1.55, 1.9),
        ylim=(-1.55, 1.55),
        zlim=(-1.45, 1.45),
        box_aspect=(1.3, 1.0, 1.0),
        framing='demo',
        note='Front-facing cutaway demo view for hollow shells and simple coordinate-system examples.',
    ),
}


def get_camera_preset(name: str) -> CameraPreset:
    try:
        return CAMERA_PRESETS[name]
    except KeyError as exc:
        raise KeyError(f'Unknown geometry3d camera preset: {name}') from exc


def list_camera_presets() -> list[str]:
    return sorted(CAMERA_PRESETS)
