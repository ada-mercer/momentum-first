# foundations-shells family

Status: implemented in Phase 2

Purpose:
- provide the first real migrated geometry3d family
- preserve the conceptual job of the canonical Foundations shell figure
- prove the shared scene/camera/style/backend path on one reader-facing figure before broader family work starts

Key files:
- `family.py` — scene definition plus legacy-output compatibility hook
- `figures/lib/geometry3d/scene_spec.py` — backend-neutral scene contract used here
- `figures/lib/geometry3d/backends/matplotlib3d.py` — first working backend
- `figures/manifests/geometry3d.yml` — manifest entry and defaults

Canonical scene:
- `foundations-shells`

Canonical geometry3d output:
- `figures/build/geometry3d/foundations-shells/canonical/foundations-shells.png`

Compatibility mirror:
- `figures/build/foundations/foundations-shells.png`

Current defaults:
- backend: `matplotlib3d`
- camera: `shell-manuscript`
- style: `shell-dark-manuscript`
