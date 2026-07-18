# geometry3d families

This tree holds family-level scene definitions and render entrypoints for native 3D geometry work.

Rules:
- Put figure-family meaning here.
- Keep backend-neutral shared logic in `figures/lib/geometry3d/`.
- Add a new family as `src/geometry3d/<family>/` with a short README, canonical scene names, and clear manuscript/dev-note targets.
- Prefer one family per conceptual cluster, not one folder per one-off render.

Current families:
- `foundations-shells/` — implemented continuity-first family and current
  manuscript figure source
- `torus-cycle/` — planned adaptation from the separate renderer architecture
- `torus-gravity-transfer/` — planned gravity-transfer/static-storyboard seed
  family

[`../../manifests/geometry3d.yml`](../../manifests/geometry3d.yml) is the
authority for family status, scenes, outputs, and backend policy.
