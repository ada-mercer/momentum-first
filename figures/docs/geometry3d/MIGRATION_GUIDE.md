# Migration guide

## Purpose
Move legacy or one-off 3D assets into the native geometry3d system without dragging old structure forward blindly.

## Migration decision rule
For any old asset, choose one of:
- remake
- wrap temporarily
- leave as legacy/dev-only
- deprecate

## When to migrate
Migrate only when all three are true:
1. the asset has a live manuscript or dev-note target
2. the concept still matches current notation and locks
3. the new system can represent it reproducibly

## Current migration path
### First migration target
- `figures/src/foundations/foundations_shells.py`
- status: migrated in Phase 2
- real family scene file: `figures/src/geometry3d/foundations-shells/family.py`
- reason: it was already canonical, conceptually stable, and the cleanest proof that the shared layer works
- backend stance: keep `matplotlib3d` as the canonical continuity backend for now, while using `pyvista3d` as the inspection/review backend

### Next adaptation target
- torus-cycle family
- reason: strong reusable architecture ideas exist, but they should be adapted rather than imported wholesale

### Legacy high-value seed
- `book/dev/figures/torus_gravity_transfer_sequence_v1.svg`
- reason: likely future gravity-transfer/static-storyboard family and possible animation bridge

## Backend migration stance for legacy matplotlib families
Do not treat existing matplotlib-backed 3D figures as problems that must be converted immediately.
Use this rule:
- preserve working matplotlib families when they already satisfy continuity, reproducibility, and maintenance needs
- add a PyVista path when geometry-native camera/surface control materially improves the family
- switch canonical ownership to PyVista only when the family has actually earned that switch

Practical backend choices during migration:
- continuity-first migration: `canonical_backend = matplotlib3d`, `default_backend = matplotlib3d`, `inspection_backend = pyvista3d` if useful
- geometry-first migration: `canonical_backend = pyvista3d`, `fallback_backend = matplotlib3d`, `inspection_backend = plotly3d` when it exists
- simple inherited/static migration: keep matplotlib as both canonical and fallback until there is a concrete PyVista gain

## Remake vs wrap vs deprecate
### Remake
Choose remake when the concept matters but the current file is visually or structurally obsolete.

### Wrap temporarily
Choose wrap only if a quick compatibility bridge helps a live migration without freezing bad architecture.

### Leave as legacy/dev-only
Use for diagnostic or exploratory figures that do not yet deserve canonical status.

### Deprecate
Use when the figure no longer matches the framework, notation, or architecture.

## Practical rule for `book/dev/figures`
Do not bulk migrate. Migrate only when a live figure family needs it.

## What not to do
- do not force a PyVista rewrite just because PyVista is the new system-level policy center
- do not leave backend intent implicit when migrating a family
- do not remove a functioning matplotlib path before the PyVista replacement is clearly better for that family
