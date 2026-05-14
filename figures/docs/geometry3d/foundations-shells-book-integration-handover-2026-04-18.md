# Foundations shells book-integration handover (2026-04-18)

## Purpose
This note is the handoff for the next session working on the `foundations-shells` figure family.

The next session should do three linked things:
1. bring the current split-shell work fully into the canonical `momentum-first/figures` structure,
2. update the shared `geometry3d` core framework only where this figure exposed genuinely reusable needs,
3. update the book to use a manuscript-ready two-panel figure with `(a)` and `(b)` labels, plus aligned caption and surrounding text.

## Current status
Primary prior handover:
- `momentum-first/figures/docs/geometry3d/foundations-shells-handover-2026-04-18.md`

Current family implementation:
- `momentum-first/figures/src/geometry3d/foundations-shells/family.py`

Current manuscript insertion point:
- `chapters/01-tier-1-foundations/02-foundations/01-core-terms-and-variables.qmd`

Geometry3d entry docs:
- `momentum-first/figures/docs/geometry3d/README.md`
- `momentum-first/figures/docs/geometry3d/QUICKSTART.md`
- `momentum-first/figures/docs/geometry3d/AUTHORING_GUIDE.md`
- `momentum-first/figures/docs/geometry3d/BACKENDS.md`
- `momentum-first/figures/docs/geometry3d/CAMERA_GUIDE.md`

## Visual/figure state coming in
The split figure currently reads as a two-stage story:
- Panel (A): `p_f -> M`
- Panel (B): `M -> p_{\hat n}(\theta)`

The latest review state is visually much stronger than earlier iterations.

### Panel A improvements already achieved
- full-gap arrow coverage across the visible annular region
- more even camera-aware spacing
- roughly 50% higher arrow density than the previously accepted sparse version
- larger arrowheads
- wider cone base, promoted into the PyVista vector default

### Panel B improvements already achieved
- clearer directional shell
- softer directional wireframe
- stronger core-shell reference
- more legible dipole arrows
- better lowered `\pm p/2` labeling

## Main unresolved issue
The main unresolved issue is now conceptual, not merely graphical.

The split figure currently tells a stronger staged/process story than the framework has explicitly locked.

The three main open questions are:
1. Is the split figure canonical or pedagogical?
2. What do the arrows mean?
3. Should Panel B keep multiple semantic channels, or be simplified?

## Recommended interpretive stance for the next session
Default recommendation unless the framework text strongly points elsewhere:
- treat the split figure as a **canonical pedagogically-staged manuscript figure**
- interpret the arrows as **constructive/representational relations** between shell descriptions, not literal temporal dynamics
- keep Panel B only if its hierarchy is made explicit enough that one semantic claim remains primary

This is a recommendation, not yet a formal lock.

## Required goals for the next session

### 1. Canonical figure integration
Bring the split figure fully into the canonical figure structure.
That means:
- it should live cleanly inside the `foundations-shells` family,
- outputs should be stable and manuscript-facing,
- manifest registration/output intent should be explicit,
- the scene should no longer be just a review-path artifact.

### 2. Shared framework updates
Update `lib/geometry3d/` only where the split figure exposed genuinely reusable needs.

Examples of acceptable shared-core promotion:
- reusable panel-label support `(a)` / `(b)`
- reusable multi-panel 3D layout support
- reusable white-background style improvements
- reusable vector defaults / label-placement improvements
- reusable backend/layout support needed beyond this one family

Do not move shell-specific semantics into common code.

### 3. Book integration
Update the chapter so the book uses the two-panel figure.
That includes:
- the correct figure reference/path
- visible `(a)` and `(b)` panel labels
- a caption aligned with the actual framework stance
- surrounding text that does not overclaim process/mechanism

## Backend policy context
System policy:
- `pyvista3d` is the primary geometry-native backend
- `matplotlib3d` is preserved for fallback / legacy continuity / simple static work
- `plotly3d` is inspection-only

Current family exception:
- `foundations-shells` still treats `matplotlib3d` as canonical/default
- `pyvista3d` is currently the richer inspection/review backend

Important practical fact from current review work:
- for the white-background split figure, PyVista is currently producing cleaner results faster

The next session should assess explicitly whether:
- the family remains continuity-first as-is,
- the split scene should become PyVista-primary,
- or scene/family policy needs clearer separation.

Do not change backend policy casually. Make any change explicit.

## Specific decisions the next session should make
1. figure status:
   - canonical structural,
   - pedagogical only,
   - or canonical pedagogically-staged
2. arrow semantics:
   - constructive mapping,
   - bookkeeping relation,
   - geometric construction,
   - or something stronger
3. Panel B policy:
   - keep multi-channel with tighter hierarchy,
   - or simplify into a cleaner single-claim panel
4. backend recommendation for this manuscript figure

## Work order recommendation
1. read the prior handover and current geometry3d docs
2. inspect current `foundations-shells` family code
3. inspect the chapter insertion point and current figure/caption usage
4. make the interpretation decision needed for safe manuscript use
5. cleanly land the split figure as a canonical artifact in the family/manifest structure
6. promote any truly reusable rendering/layout improvements into the shared core
7. render the manuscript-ready output
8. update chapter figure reference, caption, and prose
9. verify outputs and report remaining unresolved issues separately from rendering issues

## Constraints
- do not do a broad framework refactor unless required by clear reuse
- do not silently drift backend policy
- do not move shell-specific meaning into common code
- do not leave the manuscript using a figure whose caption/text overclaims the framework

## Desired end state
By the end of the next session, we ideally want:
- a canonical two-panel `foundations-shells` figure inside the current figure structure,
- reusable framework improvements promoted where justified,
- the book updated to use the new figure,
- caption and surrounding prose aligned with the chosen interpretation,
- and an explicit backend recommendation for this figure.
