# Quickstart

## What this system is
`figures/geometry3d` is the native 3D figure stack for manuscript-facing static renders, geometry-native review renders, and later animation-ready scene definitions.

## Current implemented scope
Real today:
- one implemented family: `foundations-shells`
- two working backends: `matplotlib3d` and `pyvista3d`
- shared primitives for:
  - full spheres
  - half-spheres
  - simple coordinate systems
  - bounding-box based coordinate systems
  - reusable vectors
- manifest-backed rendering
- backend comparison workflow

Still not implemented:
- `plotly3d`
- torus-family migration
- generalized backend-perfect camera parity

## Working commands
Run from `momentum-first/`.

### Render one scene
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells`
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells --backend matplotlib3d`
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells --backend pyvista3d`

Rule: no `--backend` means use the family runtime default from the manifest.

### Render one family
- `.venv/bin/python figures/scripts/render_geometry3d_family.py foundations-shells`
- `.venv/bin/python figures/scripts/render_geometry3d_family.py foundations-shells --backend pyvista3d`

### Render all implemented families
- `.venv/bin/python figures/scripts/render_geometry3d_all.py`

### Smoke check
- `.venv/bin/python figures/scripts/check_geometry3d_smoke.py --backend matplotlib3d`
- `.venv/bin/python figures/scripts/check_geometry3d_smoke.py --backend pyvista3d`

### Preserve comparison copies across backends
- `.venv/bin/python figures/scripts/compare_geometry3d_backends.py --family foundations-shells --scene foundations-shells`

That writes preserved review copies to:
- `figures/build/geometry3d/<family>/review/<scene>-matplotlib3d.png`
- `figures/build/geometry3d/<family>/review/<scene>-pyvista3d.png`

Important: a direct `render_geometry3d.py --backend ...` override still renders to the normal scene output path. Use the compare script when you want preserved side-by-side backend artifacts.

## Where things live
- `figures/src/geometry3d/<family>/` — family-local scene logic
- `figures/lib/geometry3d/scene_spec.py` — shared scene contract
- `figures/lib/geometry3d/primitives.py` — shared geometry helpers
- `figures/lib/geometry3d/cameras.py` — shared camera presets and calibration knobs
- `figures/lib/geometry3d/backends/` — backend implementations
- `figures/manifests/geometry3d.yml` — manifest and family defaults
- `figures/build/geometry3d/` — geometry3d outputs

## Backend policy right now
- system policy center: `pyvista3d`
- preserved fallback / legacy / simple-static path: `matplotlib3d`
- planned interactive inspection path: `plotly3d`
- current explicit family exception: `foundations-shells` still defaults to `matplotlib3d` for canonical continuity
- current explicit scene exception: `foundations-shells-split` uses `pyvista3d` as its scene-level manuscript default inside that family

## Important workflow note
If you compare backends, force matched output resolution.
For the demo work here, we got cleaner comparisons by using:
- the same `figsize`
- the same `dpi`
- `bbox_inches=None` in the comparison scene, so matplotlib does not crop tighter than PyVista

If a task is about primitive authoring rather than manuscript output, it is reasonable to build a small demo scene under `figures/build/geometry3d/test-renders/` first, then promote the helper into family code only after the scene pieces are behaving.

## Current camera reality
The shared camera contract is stronger than before, but perfect cross-backend equality is still approximate:
- PyVista is the stronger camera model
- matplotlib is the approximation layer
- orthographic matching may require matplotlib-specific calibration via the camera preset

See `CAMERA_GUIDE.md` before trying to align renderers.

## When to read what next
- use `AUTHORING_GUIDE.md` if you are adding or extending shared primitives
- use `CAMERA_GUIDE.md` if you are tuning framing or backend parity
- use `BACKENDS.md` if you are deciding which renderer should own a task or how a family should declare canonical/fallback/inspection roles
