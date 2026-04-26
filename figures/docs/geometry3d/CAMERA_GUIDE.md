# Camera guide

## Why cameras are centralized
3D figures get unstable fast when each family hides ad hoc camera choices inside renderer code.
Shared presets keep camera intent explicit and make backend comparison possible.

## Current reality
The camera layer is shared, but the backends do not have equally strong camera models.
Right now:
- PyVista is the stronger, more explicit camera model
- matplotlib is the approximation layer

That matters most in orthographic mode.

## What a `CameraPreset` can currently carry
- azimuth
- elevation
- `projection_mode` (`perspective` or `orthographic`)
- `view_angle_deg` for perspective views
- `orthographic_scale` for explicit orthographic framing
- `matplotlib_limit_scale` for matplotlib-only orthographic calibration when needed
- zoom
- x/y/z limits
- `distance_scale`
- `view_up`
- box aspect metadata
- framing note

## Important interpretation rule
Use the shared preset as the canonical camera intent.
Then expect:
- PyVista to follow it more directly
- matplotlib to approximate it using view angles plus data-box limits

So if cross-backend comparison matters, you may need a calibration pass instead of assuming equality.

## Orthographic mode
In orthographic rendering, apparent framing is not really about perspective FOV anymore.
It is mostly about:
- PyVista `parallel_scale`
- matplotlib effective data-box framing

That is why `orthographic_scale` and `matplotlib_limit_scale` both exist.

## Matplotlib isotropy rule
For the current setup, matplotlib now neutralizes custom `box_aspect` stretching and derives an isotropic data aspect from the effective x/y/z spans.
That means:
- only overall framing/scaling should change
- x/y/z should not be stretched differently just because layout metadata requested a non-isotropic box aspect

## Demo comparison lessons worth keeping
For close backend comparisons, use all of these:
- same `figsize`
- same `dpi`
- `bbox_inches=None` so matplotlib does not crop tighter than PyVista
- explicit camera preset
- explicit note if the preset uses `matplotlib_limit_scale`

## Current diagnostic camera
The half-sphere comparison work used `demo-front-cutaway`.
That preset now carries:
- orthographic projection
- explicit orthographic scale
- a matplotlib calibration scale

It is a useful reference if a future session needs to keep working on cross-backend camera parity.

## How to tune a camera
1. edit `figures/lib/geometry3d/cameras.py`
2. rerender both backends for the same scene
3. compare at matched output resolution
4. only then decide whether a calibration change actually helped

## What should stay out of family code
Do not hide renderer-specific camera compensation inside family scene builders.
If calibration is necessary, put it in the shared camera/backend layer so later sessions can find it.
