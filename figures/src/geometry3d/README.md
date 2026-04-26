# geometry3d families

This tree holds family-level scene definitions and render entrypoints for native 3D geometry work.

Rules:
- Put figure-family meaning here.
- Keep backend-neutral shared logic in `figures/lib/geometry3d/`.
- Add a new family as `src/geometry3d/<family>/` with a short README, canonical scene names, and clear manuscript/dev-note targets.
- Prefer one family per conceptual cluster, not one folder per one-off render.

Current planned families:
- `foundations-shells/` — first migration target from the existing canonical shell figure
- `torus-cycle/` — shared torus family adapted from the separate renderer architecture
- `torus-gravity-transfer/` — future gravity-transfer/static-storyboard seed family
