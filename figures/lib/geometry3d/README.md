# geometry3d shared library

This package is the reusable implementation layer for native 3D geometry figures.

Planned responsibilities:
- backend-neutral scene specifications
- reusable primitive categories
- camera presets
- style presets
- output/export path conventions
- backend capability wrappers

Boundary rule:
Keep family-specific physics or manuscript semantics out of this package unless at least two figure families genuinely share them.
