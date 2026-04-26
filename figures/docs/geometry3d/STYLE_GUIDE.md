# Style guide

## Goal
Make 3D figure families feel like one system, while only abstracting what the implemented family actually needs.

## Real implemented presets
Defined in `figures/lib/geometry3d/styles.py`:
- `shell-dark-manuscript` — current canonical shell-family style
- `dark-inspection` — reserved generic darker preview style
- `light-manuscript` — reserved generic light style

## What a style preset contains now
A `StylePreset` records:
- background color
- named palette entries
- axis label color
- tick color
- title color
- pane color
- a short note

## Shell-family usage rule
The migrated shell family uses shared palette keys such as:
- `core_fill`
- `core_wire`
- `fermic_fill`
- `fermic_wire`
- `directional_plus`
- `directional_minus`
- `radial_arrow`

The family code should reference these via `color_key` when possible.

## How to modify shell-family styling
1. open `figures/lib/geometry3d/styles.py`
2. edit `shell-dark-manuscript`
3. rerun:
   - `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells`

## Current boundary rule
If a color or label treatment is part of the shared figure language, keep it in `styles.py`.
If it is specific to one scene’s geometry math or object grouping, keep it in family code.
