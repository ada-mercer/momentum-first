"""Style presets for geometry3d.

Constraint: Phase 2 only makes the shell-family styling real.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class StylePreset:
    name: str
    background: str
    palette: dict[str, str] = field(default_factory=dict)
    axis_label_color: str = '#9cb5d6'
    tick_color: str = '#8ea8cc'
    title_color: str = '#e5f0ff'
    pane_rgba: tuple[float, float, float, float] = (0.07, 0.10, 0.18, 0.08)
    frame_color: str | None = None
    note: str = ''


STYLE_PRESETS: dict[str, StylePreset] = {
    'shell-dark-manuscript': StylePreset(
        name='shell-dark-manuscript',
        background='#0b1020',
        palette={
            'core_fill': '#3cf4ef',
            'core_wire': '#99fff5',
            'fermic_fill': '#fff0d1',
            'fermic_wire': '#fff0d1',
            'fermic_cap_fill': '#f4b9b7',
            'fermic_cap_wire': '#ffd6d6',
            'directional_fill_plus': '#94a3ff',
            'directional_fill_minus': '#39d6d2',
            'directional_wire_plus': '#dfe8ff',
            'directional_wire_minus': '#b8fff8',
            'directional_plus': '#60a5fa',
            'directional_minus': '#ef4444',
            'directional_plus_soft': '#eaf2ff',
            'directional_minus_soft': '#ffe8e8',
            'radial_arrow': '#22d3ee',
            'text_primary': '#dbeafe',
            'text_secondary': '#ffd29b',
            'text_core': '#8ef1f3',
            'text_directional': '#c9d4ff',
            'text_note': '#a5b4fc',
            'label_plus': '#bfdbfe',
            'label_minus': '#fecaca',
        },
        frame_color='#415a77',
        note='Canonical dark preset for the migrated foundations-shells render.',
    ),
    'dark-inspection': StylePreset(
        name='dark-inspection',
        background='#111111',
        palette={
            'accent': '#72B7B2',
        },
        note='Generic darker preview preset reserved for later inspection scenes.',
    ),
    'shell-light-manuscript': StylePreset(
        name='shell-light-manuscript',
        background='white',
        palette={
            'core_fill': '#56d7d1',
            'core_wire': '#0f766e',
            'fermic_fill': '#efe3c4',
            'fermic_wire': '#8b6f47',
            'fermic_cap_fill': '#e8b7b2',
            'fermic_cap_wire': '#a85d57',
            'directional_fill_plus': '#c7d2fe',
            'directional_fill_minus': '#c7f3ef',
            'directional_wire_plus': '#4f46e5',
            'directional_wire_minus': '#0f766e',
            'directional_plus': '#2563eb',
            'directional_minus': '#dc2626',
            'directional_plus_soft': '#bfdbfe',
            'directional_minus_soft': '#fecaca',
            'dipole_plus': '#2563eb',
            'dipole_minus': '#dc2626',
            'radial_arrow': '#0891b2',
            'text_primary': '#111827',
            'text_secondary': '#7c5a2b',
            'text_core': '#0f766e',
            'text_directional': '#3730a3',
            'text_note': '#4b5563',
            'label_plus': '#1d4ed8',
            'label_minus': '#b91c1c',
        },
        axis_label_color='#374151',
        tick_color='#4b5563',
        title_color='#111827',
        pane_rgba=(0.96, 0.97, 0.99, 0.035),
        frame_color='#c7d2da',
        note='Light manuscript preset tuned for the foundations-shells family on a white background.',
    ),
    'light-manuscript': StylePreset(
        name='light-manuscript',
        background='white',
        palette={
            'accent': '#4C78A8',
        },
        axis_label_color='#333333',
        tick_color='#444444',
        title_color='#222222',
        pane_rgba=(0.97, 0.97, 0.97, 0.03),
        frame_color='#d1d5db',
        note='Generic light preset reserved for later families.',
    ),
}


def get_style_preset(name: str) -> StylePreset:
    try:
        return STYLE_PRESETS[name]
    except KeyError as exc:
        raise KeyError(f'Unknown geometry3d style preset: {name}') from exc


def list_style_presets() -> list[str]:
    return sorted(STYLE_PRESETS)
