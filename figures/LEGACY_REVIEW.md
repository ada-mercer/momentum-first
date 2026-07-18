# Legacy figure review

Purpose: record how older figure assets retained in the wider M1 project archive
should be treated now that `figures/` is the canonical manuscript figure stack.

The archived source set now lives outside this repository under
`theory/archive/legacy-book-2026-07/dev/figures/`. Paths below name files from
that retained historical set; they are not active manuscript dependencies.

## Current canonical state
Canonical figure assets now live under:
- `figures/src/`
- `figures/build/`
- `figures/lib/`
- `figures/scripts/`
- `figures/figures.yml`

The current canonical set is defined by `figures/figures.yml`, active manuscript
references, and `figures/manifests/geometry3d.yml`.

## Legacy files reviewed
- `core_geometry_torus_3d_v3.svg`
- `core_momentum_geometry_time_dilation_v1.png`
- `core_momentum_geometry_time_dilation_v1.svg`
- `internal_fit_errors_v1.svg`
- `internal_geometry_transition_graph_v1.svg`
- `torus_3d_winding_v2.svg`
- `torus_gravity_transfer_sequence_v1.svg`
- `torus_winding_admc_v1.svg`

## Recommended classification

### A. High-value migration candidates
These look like plausible future canonical figures once tied to stable chapter use and regenerated reproducibly.

- `torus_gravity_transfer_sequence_v1.svg`
  - reason: directly relevant to future gravity-transfer / non-stationary / possible animation work
  - recommendation: treat as a seed for a future storyboard or canonical figure family, not as final artwork

- `core_momentum_geometry_time_dilation_v1.svg`
- `torus_winding_admc_v1.svg`
- `torus_3d_winding_v2.svg`
- `core_geometry_torus_3d_v3.svg`
  - reason: likely conceptually important if the geometry program becomes more reader-facing
  - recommendation: migrate only when there is a current manuscript or dev-note target and a reproducible source path is created

### B. Keep as dev/support only for now
- `internal_fit_errors_v1.svg`
- `internal_geometry_transition_graph_v1.svg`
  - reason: these read more like internal diagnostics or exploratory support than reader-facing canonical figures
  - recommendation: leave in the shared legacy archive unless a chapter or validation appendix clearly adopts them

## Practical policy
- Do not bulk-migrate legacy figures just because they exist.
- Migrate a legacy figure only when all three are true:
  1. it has a live target chapter/note,
  2. it still reflects current notation and locks,
  3. it gets a reproducible generator or at least a clean canonical source path.
- If a legacy figure is conceptually useful but visually obsolete, remake it instead of copying it forward unchanged.

## Next recommended legacy action
The strongest next candidate is:
- `torus_gravity_transfer_sequence_v1.svg`

Why:
- it connects to the active non-stationary gravity thread
- it could become either:
  - a static transfer storyboard, or
  - the seed of a later animation family
- it is exactly the kind of asset worth redoing canonically rather than leaving
  only in the shared legacy archive
