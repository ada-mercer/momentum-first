# Family index

## Implemented family

### foundations-shells
- status: migrated and actively used as the backend-comparison test family
- purpose: reader-facing shell figure for Foundations and current geometry3d proving ground
- scene file: `figures/src/geometry3d/foundations-shells/family.py`
- canonical scene id: `foundations-shells-split`
- canonical backend: `matplotlib3d`
- runtime default backend: `matplotlib3d`
- fallback backend: `matplotlib3d` (continuity-first temporary state)
- inspection backend: `pyvista3d`
- scene-level manuscript backend for `foundations-shells-split`: `pyvista3d`
- default camera: `shell-manuscript`
- default style: `shell-dark-manuscript`
- canonical geometry3d output: `figures/build/geometry3d/foundations-shells/canonical/foundations-shells-split.png`
- legacy canonical mirror: `figures/build/foundations/foundations-shells.png`
- manuscript target: `chapters/01-tier-1-foundations/02-foundations/01-core-terms-and-variables.qmd`
- note: this family remains the explicit continuity-first exception to the PyVista-primary system policy, but its manuscript split scene is now a deliberate scene-level PyVista exception

### comparison/demo work now available
The current geometry3d system also supports a small demo workflow used during backend calibration and primitive development:
- spheres and half-spheres through shared primitive helpers
- simple coordinate systems through `coordinate_system_components(...)`
- bounding-box anchored coordinate systems through `bounding_box_coordinate_system_components(...)`
- reusable vectors through `vector_object(...)` and `vector_components(...)`
- backend comparison renders under `figures/build/geometry3d/test-renders/`
- preserved family review copies under `figures/build/geometry3d/<family>/review/`

That comparison work is not yet a canonical manuscript family, but it is useful session-to-session reference material for camera and backend behavior.

## Planned families

### torus-cycle
- status: planned adaptation
- purpose: likely next family that should stress-test the shared geometry/native-camera layer more seriously
- intended canonical backend: `pyvista3d`
- intended fallback backend: `matplotlib3d`
- intended inspection backend: `plotly3d`
- current state: no implemented scenes yet

### torus-gravity-transfer
- status: seed planned
- purpose: future gravity-transfer storyboard family
- intended canonical backend: `pyvista3d`
- intended fallback backend: `matplotlib3d`
- intended inspection backend: `plotly3d`
- current state: no implemented scenes yet

## Current architecture note
Only one family is fully canonical so far.
That is still deliberate.
The next useful pressure test is torus-family adaptation, but now with the benefit of:
- shared sphere/half-sphere primitives
- shared coordinate-system support, including box-anchored variants
- shared vector helpers
- shared mesh defaults
- clearer backend roles, including canonical/fallback/inspection guidance
- better understood backend/camera differences
