# Backends

## Consolidated backend policy
- `pyvista3d` is the primary geometry-native backend for the geometry3d system
- `matplotlib3d` is explicitly preserved as a supported fallback backend, a legacy continuity backend, and an AI-friendly/simple-static implementation path
- `plotly3d` is the planned interactive inspection backend, not a canonical manuscript backend
- family manifests should record backend intent explicitly through `canonical_backend`, `fallback_backend`, and `inspection_backend`
- scene manifests may also declare backend intent when one scene is a deliberate exception inside an otherwise continuity-first family
- `default_backend` is the runtime default when no CLI override is given, and should usually match `canonical_backend`

Current explicit exception:
- `foundations-shells` remains a deliberate continuity-first family whose canonical and runtime-default backend is still `matplotlib3d`

## `matplotlib3d`
Status: implemented

Use it for:
- fallback rendering when PyVista is unavailable or unnecessary
- legacy continuity for already-working matplotlib-backed families
- simple static families where the geometry/camera demands do not justify PyVista yet
- quick smoke checks and AI-assisted maintenance work

Important behavior:
- honors shared surface sampling and shared wireframe stride
- now uses isotropic data aspect rather than stretching x/y/z via layout box-aspect metadata
- still approximates the shared camera contract rather than fully instantiating it

## `pyvista3d`
Status: implemented

Use it for:
- new native 3D families by default
- richer surfaces and stronger depth cues
- explicit camera/framing-sensitive work
- families that are likely to grow toward animation-adjacent or geometry-heavy scenes

Important behavior:
- follows the stronger camera model more directly
- uses explicit orthographic framing via `parallel_scale`
- now honors shared wireframe stride instead of always drawing the full structured-grid wireframe
- emits a non-fatal VTK/X warning in the current off-screen environment

## `plotly3d`
Status: stub only

Planned role:
- browser inspection
- interactive camera checks
- exploratory scene inspection
- optional debugging/review aid, not part of the canonical build-critical path

## How family authors should choose
Use this rule set:
1. choose `pyvista3d` as `canonical_backend` for a new family unless there is a strong continuity or simplicity reason not to
2. keep `matplotlib3d` as `fallback_backend` whenever the family can be represented there without distorting the concept
3. use `plotly3d` only as `inspection_backend`, never as the canonical manuscript path
4. if a family is inherited from an existing matplotlib figure and continuity matters more than geometry-native rendering right now, it may keep `matplotlib3d` as both `canonical_backend` and `default_backend` temporarily
5. document exceptions explicitly in the family notes instead of letting them become invisible convention

## Default behavior in manifest and runtime
- system-level manifest policy now names `primary_backend`, `fallback_backend`, and `inspection_backend`
- family-level manifest entries now name `canonical_backend`, `fallback_backend`, and `inspection_backend`
- runtime resolution is: CLI override -> scene `default_backend` -> scene `canonical_backend` -> family `default_backend` -> family `canonical_backend` -> manifest default
- practical meaning: a family can preserve a continuity-first runtime default without changing the system-wide policy center

## Backend comparison workflow
When comparing renderers, use:
- the same scene
- the same camera preset
- the same `figsize`
- the same `dpi`
- `bbox_inches=None` for the comparison scene if matplotlib would otherwise crop tighter

Useful command:
- `.venv/bin/python figures/scripts/compare_geometry3d_backends.py --family foundations-shells --scene foundations-shells`

Current output convention:
- direct scene renders, including `--backend` overrides, still write to the normal scene output location
- preserved backend review copies go to `figures/build/geometry3d/<family>/review/<scene>-<backend>.png`
- ad hoc primitive/demo renders can live under `figures/build/geometry3d/test-renders/`

Practical rule: if you need to keep both backend results, use the comparison workflow instead of two plain render calls.

## Environment and headless note
Use the repo figure interpreter:
- `momentum-first/.venv/bin/python`

PyVista path requires:
- `pyvista`
- `vtk`

Current observed headless behavior:
- off-screen PyVista rendering works
- VTK emits `bad X server connection. DISPLAY=` in this environment
- the warning is noisy but not currently fatal
