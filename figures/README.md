# Figures

This is the entrypoint for figure authors and maintainers. Figure meaning stays
close to its source; registries and manifests determine which outputs are
canonical; generated assets used by the manuscript live under `build/`.

## Choose a route

| Task | Start here |
|---|---|
| Find or rebuild a current 2D, scripted, or prompt-backed figure | [`figures.yml`](figures.yml) |
| Author or render a native 3D family | [`docs/geometry3d/QUICKSTART.md`](docs/geometry3d/QUICKSTART.md) |
| Check geometry3d family and backend policy | [`manifests/geometry3d.yml`](manifests/geometry3d.yml) and [`docs/geometry3d/BACKENDS.md`](docs/geometry3d/BACKENDS.md) |
| Review animation readiness | [`ANIMATIONS.md`](ANIMATIONS.md) |
| Classify older assets | [`LEGACY_REVIEW.md`](LEGACY_REVIEW.md) |

The complete native 3D documentation route begins at
[`docs/geometry3d/README.md`](docs/geometry3d/README.md). Family-specific rules
stay beside each family under [`src/geometry3d/`](src/geometry3d/README.md).

## Source and output model

- `src/` holds canonical scripted, prompt-backed, and geometry3d family sources.
- `*.prompt.md` files are canonical sources for AI-generated static figures;
  their checked PNG outputs live under `build/`.
- `data/` is created only when figure-owned inputs exist.
- `lib/` contains genuinely reusable helpers; family-specific physics and
  manuscript meaning remain in `src/`.
- `scripts/` contains generation, rendering, smoke-check, and comparison
  entrypoints.
- `build/` contains generated assets referenced by the manuscript or explicitly
  retained as canonical or review outputs.
- `figures.yml` is the registry for current non-geometry3d figures.
- `manifests/geometry3d.yml` is the registry and backend policy for native 3D
  families.

A manuscript figure is canonical when it is referenced by active manuscript
source, registered in `figures.yml`, or declared canonical in the geometry3d
manifest. Commit PNG manuscript assets by default. PDF and SVG companions,
ad hoc renders, and backend comparisons are not canonical unless a manifest or
review record explicitly promotes them.

## Common commands

Generate the registered figure set:

```bash
python3 figures/scripts/generate_all.py
```

Set `FIGURES_PYTHON` when generation should use a particular interpreter. The
generator otherwise prefers the repository `.venv` and then the current Python
interpreter.

Render or check native 3D families:

```bash
.venv/bin/python figures/scripts/render_geometry3d.py \
  --family foundations-shells --scene foundations-shells
.venv/bin/python figures/scripts/render_geometry3d_family.py foundations-shells
.venv/bin/python figures/scripts/render_geometry3d_all.py
.venv/bin/python figures/scripts/check_geometry3d_smoke.py --backend pyvista3d
```

Use `compare_geometry3d_backends.py` only when a backend comparison is the
actual review task. Preserve accepted comparisons under
`build/geometry3d/<family>/review/`; put disposable demonstrations under
`build/geometry3d/test-renders/`.

## Geometry3d boundary

The system-level policy is PyVista-primary, with Matplotlib retained as a
fallback and continuity backend and Plotly reserved for interactive inspection.
Individual family manifests may declare explicit exceptions; `foundations-shells`
currently remains Matplotlib-first for continuity.

Shared backend-neutral scene, primitive, camera, style, and export behavior
belongs in [`lib/geometry3d/`](lib/geometry3d/README.md). Family meaning and
scene composition belong in [`src/geometry3d/<family>/`](src/geometry3d/README.md).
Do not move one-off family logic into the shared layer prematurely.

Project-wide figure and generated-output policy lives in
[`../docs/STANDARDS.md`](../docs/STANDARDS.md). Dependency setup lives in
[`../docs/DEPENDENCIES.md`](../docs/DEPENDENCIES.md).
