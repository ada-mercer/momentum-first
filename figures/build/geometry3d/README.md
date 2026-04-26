# geometry3d build outputs

This folder is the canonical build root for generated native 3D geometry assets.

Intended layout:
- `build/geometry3d/<family>/preview/` for fast review renders
- `build/geometry3d/<family>/canonical/` for manuscript-facing outputs
- `build/geometry3d/<family>/interactive/` for HTML inspection assets when enabled
- `build/geometry3d/<family>/frames/` for animation-ready frame sequences when later phases need them

Phase 1 note:
The build tree is scaffolded now so future sessions have a fixed destination before renderer internals land.
Subdirectories should be created on first real render rather than guessed too early.
