# Authoring guide

## Goal
Add new 3D figure families without mixing family semantics and renderer internals.

## Current shared modules
Use `figures/lib/geometry3d/` for shared machinery:
- `scene_spec.py` — backend-neutral scene contract
- `primitives.py` — shared geometry helpers
- `cameras.py` — shared camera presets and calibration knobs
- `styles.py` — shared style presets
- `exporters.py` — output path helpers
- `manifest.py` — manifest loading
- `runtime.py` — render dispatch
- `backends/matplotlib3d.py` — stable baseline backend
- `backends/pyvista3d.py` — geometry-native backend

## Family-local code
Put family meaning in `figures/src/geometry3d/<family>/`.
For the current shell family:
- `figures/src/geometry3d/foundations-shells/family.py`

Family code should own:
- scene-building math
- family-specific object construction
- family defaults when they are genuinely family-specific
- optional post-render compatibility behavior

## Shared primitive helpers you can use now
`figures/lib/geometry3d/primitives.py` currently provides reusable helpers for:
- full spherical shells
- half-spherical shells
- shared sampled surface + wireframe construction
- simple coordinate systems
- bounding-box based coordinate systems
- reusable vector helpers

Important helpers:
- `sphere_shell_objects(...)`
- `half_sphere_shell_objects(...)`
- `coordinate_system_components(...)`
- `bounding_box_from_points(...)`
- `bounding_box_coordinate_system_components(...)`
- `vector_object(...)`
- `vector_components(...)`
- `sampled_surface_and_wireframe(...)`

## Shared default mesh setting
The primitive layer owns the default sphere/half-sphere mesh profile through `DEFAULT_MESH_RESOLUTION`.
That means both renderers inherit the same default surface sampling and wireframe stride unless a family explicitly overrides them.

Current default profile:
- `theta_samples = 240`
- `phi_samples = 240`
- `wire_rstride = 8`
- `wire_cstride = 8`

PyVista wireframes now honor the same shared stride settings instead of drawing the full grid unconditionally.

## Shared simple coordinate systems
Use `coordinate_system_components(...)` when you need a clean local coordinate triad.
It emits backend-neutral scene pieces using:
- `vector_set` axis arrows
- optional origin marker
- `text3d` axis labels

That is better than hand-writing axis arrows in each family.

## Shared box coordinate systems
Use `bounding_box_coordinate_system_components(...)` when the coordinate system should be anchored to an object's bounding box instead of an arbitrary origin/scale.

Typical workflow:
1. compute a box with `bounding_box_from_points(x, y, z)`
2. build the box-based coordinate system from that box
3. add the returned objects/annotations to the scene

The box-based helper uses the box spans as the axis lengths, so the resulting coordinate frame is explicitly tied to the object's enclosing dimensions.

Useful options now include:
- `depth_placement='front' | 'back'` for moving the box coordinate system between the front and back y-face of the box
- `axis_color='...'` for one shared color across all axes
- `axis_colors={'x': ..., 'y': ..., 'z': ...}` for per-axis color control

## Shared vector helpers
Use `vector_object(...)` when you want one clean backend-neutral vector object.
Use `vector_components(...)` when you also want an optional label.

Supported vector options now include:
- `start=(x, y, z)`
- `direction=(dx, dy, dz)` or `end=(x, y, z)`
- `length=...`
- `normalize_direction=True | False`
- `color` or `color_key`
- `linewidth`
- `arrow_length_ratio`
- `alpha`
- `zorder`
- optional `label`, `label_color`, `label_offset_scale`, and `label_fontsize`

Practical rule:
- prefer `vector_object(...)` or `vector_components(...)` in family code
- only hand-build raw `vector_set` params when you truly need batch/vector-array construction that the helper does not cover yet

## Scene contract
A working `SceneSpec` should include:
- `family`
- `scene_id`
- `default_camera`
- `default_style`
- `layout`
- `outputs`
- `objects`
- `annotations`

## Current object kinds
Implemented object kinds:
- `sampled_surface`
- `sampled_wireframe`
- `vector_set`
- `point_markers`

The shared helper layer deliberately wraps some of these low-level kinds now, so new family code should usually consume helpers rather than constructing all object params by hand.

Implemented annotation kinds:
- `text2d`
- `text3d`

Keep it tight until the torus family truly forces a broader contract.

## Camera guidance for new work
Treat the shared camera preset as canonical input.
In practice right now:
- PyVista is closest to the canonical camera model
- matplotlib is the approximation layer
- orthographic comparisons may require a matplotlib-specific calibration knob in the camera preset

If you need cross-backend comparisons, prefer:
- matched `figsize`
- matched `dpi`
- `bbox_inches=None` in the comparison scene
- explicit notes when a preset uses matplotlib-specific calibration

## Current backend usage rule
- author scenes once in backend-neutral form
- choose backend in the manifest or CLI
- if one manuscript scene needs a stronger backend than the rest of its family, use an explicit scene-level backend override in the manifest instead of silently changing family-local geometry logic
- do not hide backend-specific geometry assumptions in family code
- backend-specific camera approximation belongs in the shared camera/backend layer, not in family-local geometry logic

## Minimal recipe for a new family
1. create `figures/src/geometry3d/<family>/family.py`
2. return a real `SceneSpec` from one or more builder functions
3. add family and scene entries in `figures/manifests/geometry3d.yml`
4. render first with `matplotlib3d` or `pyvista3d`, depending on the job
5. document canonical vs review backend choice explicitly

## Useful working commands
From `momentum-first/`:
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells --backend matplotlib3d`
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells --backend pyvista3d`
- `.venv/bin/python figures/scripts/compare_geometry3d_backends.py --family foundations-shells --scene foundations-shells`

## What not to do yet
- do not start porting torus-cycle into shared abstractions prematurely
- do not broaden the primitive vocabulary without a second real family forcing it
- do not assume camera parity across backends unless you checked it visually
- do not turn every demo convenience into a new object kind if an existing helper over `vector_set`, `point_markers`, or sampled geometry is enough
