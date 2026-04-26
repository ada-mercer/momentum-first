# Legacy figure review

Purpose: decide what to do with older figure assets under `book/dev/figures` now that `momentum-first/figures/` is the canonical stack.

## Current canonical state
Canonical figure assets now live under:
- `momentum-first/figures/src/`
- `momentum-first/figures/build/`
- `momentum-first/figures/lib/`
- `momentum-first/figures/scripts/`
- `momentum-first/figures/figures.yml`

The current canonical registry covers four Foundations figures.

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
  - recommendation: leave in `book/dev/figures` unless a chapter or validation appendix clearly adopts them

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
- it is exactly the kind of asset worth redoing canonically rather than leaving stranded in `book/dev/figures`
