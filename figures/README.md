# Figures

- `src/` holds canonical figure and animation sources.
- `*.prompt.md` files under `src/` are canonical sources for AI-generated static figures; the checked image artifact lives under `build/` and Quarto captions supply the manuscript title/caption.
- Prompt files for committed manuscript figures belong under `figures/src/...`, not in a root-level `prompts/` folder.
- `src/geometry3d/` holds family-level scene definitions and entrypoints for the native 3D geometry system.
- `data/` holds figure inputs.
- `build/` holds generated assets referenced by the manuscript.
- Commit PNG manuscript assets by default. Generated PDF/SVG companions stay out of release commits unless explicitly promoted by a manifest, README, or release decision.
- `build/geometry3d/` holds generated 3D geometry outputs and per-family render folders.
- `lib/` holds reusable helper code once it is genuinely shared.
- `lib/geometry3d/` holds the shared 3D scene, primitive, camera, style, exporter, and backend support layer.
- `scripts/` holds orchestration such as generate-all pipelines.
- `scripts/render_geometry3d.py`, `render_geometry3d_family.py`, and `render_geometry3d_all.py` are the geometry3d CLI entrypoints.
- `scripts/check_geometry3d_smoke.py` is the minimal validation path.
- `scripts/compare_geometry3d_backends.py` preserves comparison copies across backends.
- `figures.yml` is the canonical 2D/current figure registry. Prompt-backed AI figures should list the prompt file as `source`, the checked image as `output`, and the model under `generator` when known.
- `manifests/geometry3d.yml` is the family registry scaffold for the native 3D geometry system.
- `docs/geometry3d/` is the docs-first entrypoint for architecture, primitives, cameras, styles, backend policy, and migration notes.
- `ANIMATIONS.md` records animation-readiness structure and rules.
- `LEGACY_REVIEW.md` records what to do with older `book/dev/figures` assets.
- `GEOMETRY3D_CONSTRUCTION_PLAN.md` is the handoff-ready build plan for native 3D geometry support.
- `requirements-python.txt` records the current Python dependency needed by Python-backed canonical figure scripts.

Useful commands:
- `python3 figures/scripts/generate_all.py`
- `FIGURES_PYTHON=/path/to/venv/bin/python python3 figures/scripts/generate_all.py`
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells`
- `.venv/bin/python figures/scripts/render_geometry3d.py --family foundations-shells --scene foundations-shells --backend pyvista3d`
- `.venv/bin/python figures/scripts/render_geometry3d_family.py foundations-shells --backend pyvista3d`
- `.venv/bin/python figures/scripts/render_geometry3d_all.py`
- `.venv/bin/python figures/scripts/check_geometry3d_smoke.py --backend pyvista3d`
- `.venv/bin/python figures/scripts/compare_geometry3d_backends.py --family foundations-shells --scene foundations-shells`

Comparison outputs:
- canonical family renders stay in their normal build locations
- preserved backend comparison copies go under `build/geometry3d/<family>/review/`
- ad hoc demo renders can go under `build/geometry3d/test-renders/`
- `Rscript ../skills/r-figures/scripts/check_r_figure_env.R`

Geometry3d backend policy:
1. `pyvista3d` is the primary geometry-native backend for the system.
2. `matplotlib3d` is explicitly preserved as a fallback backend, a legacy continuity backend, and an AI-friendly path for simpler or inherited figures.
3. `plotly3d` is reserved for interactive inspection and is not part of the canonical manuscript path.
4. Family manifests should declare `canonical_backend`, `fallback_backend`, and `inspection_backend` explicitly.
5. `default_backend` is the runtime default when no CLI override is given, and usually matches the canonical backend.
6. `foundations-shells` is the current explicit continuity-first exception and still defaults to `matplotlib3d`.
7. Backend-neutral scene definitions live under `lib/geometry3d/` and family-specific meaning lives under `src/geometry3d/<family>/`.

Geometry3d functionality now available:
- shared sphere helpers
- shared half-sphere helpers
- shared coordinate-system helper
- shared bounding-box coordinate-system helper
- shared vector helpers
- shared mesh-resolution defaults
- shared camera presets with orthographic calibration support

Python interpreter selection for `generate_all.py`:
1. use `FIGURES_PYTHON` if set
2. otherwise use the repo-local default: `momentum-first/.venv/bin/python`
3. otherwise fall back to the current interpreter
