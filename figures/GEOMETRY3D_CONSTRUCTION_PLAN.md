# Native 3D Geometry Support — Construction Plan

> Historical construction plan. The implemented system is governed by
> [`figures/README.md`](README.md),
> [`figures/manifests/geometry3d.yml`](manifests/geometry3d.yml), and
> [`figures/docs/geometry3d/`](docs/geometry3d/README.md). References below to
> `book/dev/figures` describe the former location of assets now retained in the
> wider M1 project archive.

Purpose: define the full build plan for native 3D geometry support inside `momentum-first/figures/`, adapted from the strongest architectural ideas in `torus-cycle-renderer` while fitting the canonical figure system already in use for the manuscript.

This plan is written as a **handoff-ready execution artifact** for future sessions.
A new session should be able to follow it without reverse-engineering prior chat context.

---

## 0. Executive summary

### Objective
Build a **native 3D geometry figure system** inside `momentum-first/figures/` that supports:
- static 3D manuscript figures,
- interactive inspection views,
- future animation-ready scene definitions,
- centralized settings and reusable geometry/render infrastructure,
- clean documentation so later sessions can use the system without deep code dives.

### Strategic choice
Adopt the **architecture** of `torus-cycle-renderer`, not a wholesale repo merge.

Keep:
- scene/render separation,
- renderer backends,
- config-driven cameras/styles,
- export discipline,
- CLI/script orchestration,
- tests.

Do **not** make the whole system depend on:
- particle-cycle semantics,
- torus-cycle-specific assumptions,
- loop-time physics abstractions,
- domain-specific output/archive clutter.

### Primary design goals
1. **Centralized settings**
2. **Reusable geometry and rendering functionality**
3. **Expandability across figure families**
4. **Clear static vs interactive vs animation workflows**
5. **Strong documentation and handoff ergonomics**

---

## 1. Scope and non-goals

## In scope
- native 3D geometry support under `momentum-first/figures/`
- shared library layer for geometry primitives, scene specs, cameras, styles, and backend wrappers
- canonical render/orchestration scripts
- migration of the existing shell plot to the new structure
- adaptation path for torus-cycle functionality into the shared framework
- documentation sufficient for future sessions to use the system without deep code reading
- test and validation baseline
- preview/review workflow for rendered outputs

## Explicitly out of scope for v1
- full merge of `torus-cycle-renderer` into the main repo
- immediate migration of every legacy 3D figure
- a fully generalized physics engine for all future geometry ideas
- production-grade animation authoring for every family from day one
- forcing R to be the native 3D backend

---

## 2. Design principles

1. **Scene first, backend second**
   - figure meaning should be defined in backend-independent scene objects/configs

2. **Family logic separate from core renderer**
   - shell-specific or torus-specific physics logic should not leak into generic rendering helpers

3. **One canonical render path per published artifact**
   - many dev views are allowed, but each canonical figure should have one named camera/render target

4. **Static output remains the default**
   - animation and interaction should extend a stable static scene definition

5. **Documentation is part of the system, not an afterthought**
   - a new session should be able to use the system from docs first, code second

6. **Centralize only what is genuinely reused**
   - do not over-abstract before at least two figure families need the same thing

---

## 3. Target architecture

## Canonical repo layout

```text
momentum-first/figures/
  src/
    geometry3d/
      foundations-shells/
      torus-cycle/
      torus-gravity-transfer/
  build/
    geometry3d/
  lib/
    geometry3d/
      __init__.py
      scene_spec.py
      primitives.py
      cameras.py
      styles.py
      exporters.py
      backends/
        __init__.py
        matplotlib3d.py
        pyvista3d.py
        plotly3d.py
  scripts/
    render_geometry3d.py
    render_geometry3d_family.py
    render_geometry3d_all.py
  manifests/
    geometry3d.yml
  docs/
    geometry3d/
      QUICKSTART.md
      AUTHORING_GUIDE.md
      CAMERA_GUIDE.md
      STYLE_GUIDE.md
      BACKENDS.md
      MIGRATION_GUIDE.md
      FAMILY_INDEX.md
```

## Notes on structure
- `src/geometry3d/<family>/` = family-level scene definitions and canonical render entrypoints
- `lib/geometry3d/` = reusable implementation layer
- `build/geometry3d/` = generated outputs
- `scripts/` = orchestration and generate-all entrypoints
- `manifests/geometry3d.yml` = registry for family outputs and metadata
- `docs/geometry3d/` = the main user-facing operational docs for future sessions

---

## 4. Core abstractions to build

## 4.1 Scene specification layer
Create a backend-neutral scene model capable of describing:
- spherical shell
- directional shell
- core shell
- torus surface
- deformed torus
- loop/path/trajectory
- arrows/vector bundles
- markers / labelled points
- cut planes / cut discs / cutaway policies
- overlay text blocks / title blocks / legends
- axis visibility and framing policy

### Desired outcome
A family should define **what exists in the scene**, not how matplotlib/PyVista/Plotly specifically draw it.

## 4.2 Camera system
Centralize camera definitions:
- preset names
- azimuth / elevation
- zoom
- aspect ratio
- bounding extents
- axis framing
- cutaway-facing view presets
- manuscript view vs inspection view vs hero view

### Required feature
Every canonical 3D artifact should record the exact camera preset used.

## 4.3 Style system
Centralize:
- dark / light presets
- shell palette rules
- torus palette rules
- wireframe opacity/width
- vector arrow styling
- label and overlay styling
- transparency defaults
- manuscript-safe typography rules

### Required feature
Different 3D figure families should look like part of the same visual system.

## 4.4 Backend wrappers
Support three backend classes:

### A. Matplotlib 3D
Default static backend for:
- canonical manuscript PNGs
- lightweight reproducible previews
- CI-friendly static rendering

### B. PyVista
High-quality geometry backend for:
- richer surfaces
- better depth/readability for complex tori
- future hero renders
- animation-friendly geometry scenes

### C. Plotly
Interactive inspection backend for:
- HTML/browser review
- dev-facing camera checks
- exploratory scene inspection

### Backend rule
Backends should share the same scene/camera/style inputs as much as practical.

## 4.5 Export layer
Standardize output handling for:
- preview PNG
- canonical PNG
- optional PDF when meaningful
- optional SVG only when output remains meaningful as vector
- interactive HTML
- frame sequences
- GIF/MP4 stitching later
- optional geometry exports (`npz`, `obj`) where useful

---

## 5. Workstreams

This system should be built through six parallel but ordered workstreams.

## Workstream A — Library foundation
Build the reusable 3D library skeleton.

### Deliverables
- `lib/geometry3d/scene_spec.py`
- `lib/geometry3d/primitives.py`
- `lib/geometry3d/cameras.py`
- `lib/geometry3d/styles.py`
- `lib/geometry3d/exporters.py`
- `lib/geometry3d/backends/*.py`

### Acceptance criteria
- at least one shell scene and one torus scene can be represented without figure-family-specific plotting code in the backend layer
- camera presets are loadable from one central source
- style presets are reusable across at least two scene families

## Workstream B — Foundations shell migration
Refactor the current shell figure into the new system.

### Initial target
- current canonical source: `momentum-first/figures/src/foundations/foundations_shells.py`

### Goals
- preserve current conceptual job and visual quality
- move scene logic into shared geometry3d helpers where sensible
- keep a family-level file that is readable and not overloaded with backend internals

### Deliverables
- new `src/geometry3d/foundations-shells/` family
- canonical render script for the shell family
- camera preset(s) for shell figure
- manifest entry
- updated build outputs

### Acceptance criteria
- resulting figure matches or exceeds current readability
- source is less monolithic than the old one-off script
- the family can render using the canonical default backend

## Workstream C — Torus-cycle adaptation
Adapt torus-cycle functionality into the shared geometry3d system.

### Strategy
Port and adapt selected structures from `torus-cycle-renderer`:
- config-driven cameras
- backend separation
- scene sampling pattern
- export handling
- CLI style

### Do not port blindly
Keep particle/cycle-specific logic family-local.

### Deliverables
- `src/geometry3d/torus-cycle/` family
- shared torus primitives in `lib/geometry3d/primitives.py`
- one canonical static torus-cycle preview path
- one interactive inspection path

### Acceptance criteria
- torus family uses shared cameras/styles/export logic
- no unnecessary dependence on cycle repo output layout

## Workstream D — Gravity-transfer family readiness
Prepare the geometry path most likely to matter next.

### First candidate
- legacy seed: `book/dev/figures/torus_gravity_transfer_sequence_v1.svg`

### Goal
Make it a family, not just a legacy file.

### Deliverables
- `src/geometry3d/torus-gravity-transfer/`
- static storyboard-ready scene definition
- optional animation-readiness note within the family

### Acceptance criteria
- the family can produce a static canonical figure first
- future animation can extend the same scene definition cleanly

## Workstream E — Orchestration and manifest support
Build the user-facing execution path.

### Deliverables
- `scripts/render_geometry3d.py`
- `scripts/render_geometry3d_family.py`
- `scripts/render_geometry3d_all.py`
- `manifests/geometry3d.yml`

### Required features
- render one scene by family/name
- render one whole family
- render all canonical geometry3d outputs
- choose backend explicitly or use default
- choose camera preset explicitly or use family default

### Acceptance criteria
- new sessions can render without browsing internals
- commands are documented and predictable

## Workstream F — Documentation and onboarding
This is mandatory, not optional.

### Deliverables
- `docs/geometry3d/QUICKSTART.md`
- `docs/geometry3d/AUTHORING_GUIDE.md`
- `docs/geometry3d/CAMERA_GUIDE.md`
- `docs/geometry3d/STYLE_GUIDE.md`
- `docs/geometry3d/BACKENDS.md`
- `docs/geometry3d/MIGRATION_GUIDE.md`
- `docs/geometry3d/FAMILY_INDEX.md`

### Acceptance criteria
A new session should be able to:
- understand the architecture,
- choose a backend,
- render an existing family,
- add a new camera preset,
- understand where new family code belongs,
without deep-diving into backend implementation files.

---

## 6. Documentation specification

Documentation is a core construction requirement.
The functionality should not be considered complete until this documentation exists.

## 6.1 QUICKSTART.md
Must answer:
- What is the 3D geometry system?
- Where are source files, builds, manifests, and docs?
- How do I render one canonical geometry figure?
- How do I render all geometry figures?
- How do I preview a family quickly?

## 6.2 AUTHORING_GUIDE.md
Must answer:
- How do I create a new 3D geometry family?
- What belongs in family-level files vs shared library files?
- How do I define a scene?
- How do I choose a backend?
- How do I export preview and canonical artifacts?

## 6.3 CAMERA_GUIDE.md
Must answer:
- How are camera presets defined?
- How do I create a new preset?
- How do I choose manuscript vs inspection vs hero views?
- What conventions should be followed for axes and cutaways?

## 6.4 STYLE_GUIDE.md
Must answer:
- Which colors/transparency rules are canonical?
- How should shells, tori, loops, and arrows be styled?
- When should dark vs light backgrounds be used?
- How should overlays and labels be handled?

## 6.5 BACKENDS.md
Must answer:
- When should I use matplotlib vs PyVista vs Plotly?
- What environment/dependency requirements exist for each?
- What outputs are supported by each backend?
- What are the headless rendering caveats?

## 6.6 MIGRATION_GUIDE.md
Must answer:
- How do I migrate a legacy 3D figure or script into the new system?
- When should I remake vs wrap vs deprecate an old artifact?
- How should legacy `book/dev/figures` files be treated?

## 6.7 FAMILY_INDEX.md
Must answer:
- What geometry3d families currently exist?
- What each family is for
- What canonical outputs exist
- What manuscript/dev-note targets they support
- What still remains exploratory

---

## 7. Phased execution plan

## Phase 0 — Grounding and freeze
Goal: stabilize the design target before coding spreads.

### Tasks
- confirm canonical target layout
- confirm backend policy
- confirm first migration targets
- confirm documentation set
- capture this plan as the governing artifact

### Exit condition
No major architecture ambiguity remains.

## Phase 1 — Skeleton and docs-first scaffolding
Goal: create the filesystem, skeleton modules, and documentation placeholders.

### Tasks
- create `lib/geometry3d/`
- create `src/geometry3d/`
- create `manifests/geometry3d.yml`
- create `docs/geometry3d/` stubs with high-level navigation
- add top-level references from `momentum-first/figures/README.md`

### Exit condition
A new session can see the intended structure immediately.

## Phase 2 — Shared core implementation
Goal: implement the backend-neutral support layer.

### Tasks
- implement scene spec primitives
- implement camera presets
- implement style presets
- implement export helpers
- implement at least one backend wrapper cleanly

### Exit condition
Shared layer is real enough to carry a first family migration.

## Phase 3 — Foundations shell family migration
Goal: prove the shared layer works on a real canonical figure.

### Tasks
- move shell-specific scene logic into family files + shared helpers
- define shell camera preset(s)
- render canonical output
- compare against old output
- document the family in `FAMILY_INDEX.md`

### Exit condition
The shell family uses the new system and remains visually strong.

## Phase 4 — Torus family adaptation
Goal: adapt the strongest torus renderer patterns into the native framework.

### Tasks
- identify what to port from `torus-cycle-renderer`
- wrap/adapt torus primitives and scene logic
- create first torus family under `src/geometry3d/torus-cycle/`
- support static preview and optional interactive output

### Exit condition
There is one working torus family that shares the common geometry3d layer.

## Phase 5 — Gravity-transfer family seed
Goal: make the highest-value future family ready.

### Tasks
- review `torus_gravity_transfer_sequence_v1.svg`
- define the family scene/model target
- produce static canonical v1
- record animation-readiness hooks, but do not overbuild motion logic

### Exit condition
A meaningful next-use family exists for gravity-transfer work.

## Phase 6 — Orchestration and generate-all
Goal: make the system easy to use operationally.

### Tasks
- implement render-one / render-family / render-all scripts
- connect to manifest
- document commands in QUICKSTART
- define backend override behavior and defaults

### Exit condition
A new session can render without touching low-level code.

## Phase 7 — Validation and hardening
Goal: reduce fragility.

### Tasks
- add smoke tests
- add backend-availability checks
- test headless operation where relevant
- verify preview/canonical output conventions
- validate docs by following them in a fresh test pass

### Exit condition
System is reliable enough for repeated use by future sessions.

---

## 8. Dependencies and environment plan

## Python
The native 3D geometry path should be **Python-first**.

### Required baseline
- `numpy`
- `matplotlib`

### Optional/advanced
- `pyvista`
- `plotly`
- `kaleido`
- any runtime support required by PyVista headless rendering

## Backend dependency policy
- matplotlib backend should be considered the minimum viable canonical backend
- PyVista and Plotly should be treated as optional but supported
- environment requirements must be documented in `BACKENDS.md`

## Runtime requirement
Interpreter selection should follow the same discipline already established for figure pipelines:
- explicit environment if needed
- repo-local venv preferred where practical
- clear documented override path

---

## 9. Testing and validation

## Minimum test set
- one smoke test for shared geometry primitives
- one smoke test for shell-family render
- one smoke test for torus-family render
- one camera-preset test
- one manifest/render-all test
- one backend availability check for optional backends

## Output validation
For canonical outputs, verify:
- file exists
- file is non-empty
- expected dimensions are respected
- expected backend was used
- scene/camera configuration is reproducible

## Documentation validation
Before calling the system complete, run a docs-driven validation pass:
- use only `QUICKSTART.md` and `AUTHORING_GUIDE.md`
- render one existing family
- add one small camera preset
- confirm that this can be done without deep backend code reading

---

## 10. Migration policy for old assets and repos

## Legacy `book/dev/figures`
Keep the earlier policy:
- do not bulk migrate
- migrate only when a figure has a live target and a reproducible path

## `torus-cycle-renderer`
Treat as:
- source of architectural patterns,
- source of reusable ideas,
- possible source of selective ported/adapted code,
not as the canonical location for the final manuscript 3D system.

## Migration priority order
1. `foundations_shells.py`
2. torus-cycle family adaptation
3. gravity-transfer family
4. other legacy torus figures as current manuscript/dev-note demand justifies

---

## 11. Session handoff protocol

This plan is intended to be handed to a fresh session.
That session should not have to reconstruct hidden assumptions.

## Startup instruction for the next session
A new session working this plan should begin by reading:
1. `momentum-first/figures/GEOMETRY3D_CONSTRUCTION_PLAN.md`
2. `momentum-first/figures/README.md`
3. `momentum-first/figures/ANIMATIONS.md`
4. `momentum-first/figures/LEGACY_REVIEW.md`
5. the current shell source and the selected torus-cycle-renderer files relevant to the current phase

## Required startup summary
The session should explicitly state:
- current phase,
- immediate deliverable,
- smallest next implementation win,
- any unresolved architecture risk.

## Session rule
Each implementation session should complete one of:
- one new shared library component,
- one family migration step,
- one orchestration step,
- one documentation block,
- one validation step.

Avoid broad partial progress with no stabilized artifact.

---

## 12. Suggested implementation milestones

### Milestone M1 — Skeleton in place
- layout exists
- docs stubs exist
- manifest exists

### Milestone M2 — Shared core usable
- cameras/styles/primitives are real
- default backend wrapper works

### Milestone M3 — Shell family migrated
- shell figure moved onto the new support layer
- output accepted
- docs updated

### Milestone M4 — Torus family adapted
- one torus family uses shared layer
- static + optional interactive path works

### Milestone M5 — Gravity-transfer family seeded
- legacy seed converted into a clean family target

### Milestone M6 — Operational usability achieved
- render scripts work
- docs are sufficient
- tests pass

---

## 13. Immediate next actions

The next implementation session should do **Phase 1 only** unless a clear reason appears to combine it with a very small Phase 2 step.

### Concrete recommended next session objective
Create the geometry3d skeleton and the docs-first scaffolding:
- directory structure
- manifest stub
- docs stubs
- top-level README linkage
- explicit backend policy note

### Why this first
It makes the architecture visible and reduces future session drift before deeper code work begins.

---

## 14. Success definition

This functionality should be considered successfully constructed when:
- 3D geometry figures live in a native canonical structure under `momentum-first/figures/`
- at least two figure families share common 3D infrastructure
- static rendering is easy and reproducible
- future animation can extend the same scene definitions cleanly
- backend selection is documented and predictable
- future sessions can use the system from docs first, not code archaeology first

---

## 15. Final recommendation

Use this plan as the governing build artifact.
Do not start by overbuilding animation or porting the full torus repo.
Build the shared geometry3d layer, migrate the shell family first, then adapt torus functionality into the same structure.

That sequence gives the cleanest path to centralized settings, reusability, expandability, and durable session-to-session usability.
