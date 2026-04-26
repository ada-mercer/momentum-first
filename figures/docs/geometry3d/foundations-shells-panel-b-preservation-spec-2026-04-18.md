# Foundations shells panel B preservation spec (2026-04-18)

## Status
Active working spec for restoring panel B to be **extremely close to the original reviewed PyVista render**.

Primary visual reference:
- `figures/build/geometry3d/foundations-shells/review/foundations-shells-panel-b-pyvista3d-v17.png`

Secondary nearby references:
- `figures/build/geometry3d/foundations-shells/review/foundations-shells-panel-b-pyvista3d-v16.png`
- `figures/build/geometry3d/foundations-shells/review/foundations-shells-panel-b-pyvista3d-v15.png`

## Governing rule
For the next reconstruction pass, panel B is a **preservation job, not a redesign job**.

Default rule:
- if a choice would make panel B cleaner but less like `...panel-b-pyvista3d-v17.png`, do **not** take it
- preserve the original semantic layering, object hierarchy, and visual balance first
- only make changes that are required for canonical integration, framing stability, or label clarity

## Canonical target interpretation
Panel B should preserve the original reviewed multi-channel reading:
1. inner **core shell** `M` as the reference geometry
2. outer **directional shell** `p_{\hat n}(\theta)` as a direction-dependent deformation of that reference shell
3. continuous **signed scalar coloring** across the directional shell
4. distributed **dipole deformation arrows** across the shell
5. stronger axial arrows and endpoint markers highlighting the chosen axis
6. lowered `\pm p/2` labels as axis-specific annotations, not whole-panel titles

## Must-preserve visible elements

### A. Core-shell reference
Keep all of these:
- inner core shell at radius `M`
- visible wireframe on the core shell
- enough lighting/self-lit strength that the core shell remains legible through the outer shell
- core shell should read as the reference geometry, not disappear into the background

Do not:
- remove the core shell
- flatten it into a faint afterthought
- swap it for a radically different reference form

### B. Directional shell
Keep all of these:
- outer directional shell as the main deformed shell
- continuous scalar-colored surface, not merely split plus/minus shell halves
- visible but softened directional-shell wireframe
- shell should remain translucent enough that the core-shell reference is still readable

Do not:
- replace the scalar-colored directional shell with the simpler split-shell-plus-channel composition
- collapse the surface into a single-color shell
- make the directional wireframe dominant

### C. Signed scalar coloring
Keep all of these:
- warm/cool signed color contrast across the directional shell
- smooth transition across the shell, not hard segmentation
- color should visibly support the directional/dipole reading

Do not:
- convert the shell back to only cyan/blue half-shell fills
- make the scalar field so faint that the signed structure disappears
- change the palette logic casually

### D. Distributed dipole arrows
Keep all of these:
- many distributed arrows over the shell, on both positive and negative sides
- arrows should clearly read as local deformation/displacement cues
- soft underlay behind the main arrows for contrast should remain if needed to preserve the original read
- arrow density should remain close to the original reviewed panel

Do not:
- delete the distributed dipole arrows
- reduce the panel to only two large axis arrows
- make the distributed arrows so thick/dense that they overwhelm the shell surfaces

### E. Axial arrows and endpoints
Keep all of these:
- strong axial arrow on each side along the chosen direction
- soft underlay axial arrows if needed to match the original emphasis
- endpoint markers at the arrow termini
- axial arrows should remain stronger than the distributed shell arrows, but not cartoonishly dominant

Do not:
- remove the axial arrows
- replace them with a different channel metaphor
- make them massively thicker than the original review state

### F. `\pm p/2` labels
Keep all of these:
- one lowered label on each side
- labels should be associated with the axis arrows, not float as titles for whole hemispheres
- relative placement should remain close to the reviewed render
- labels should be clearly legible, but not oversized

Do not:
- move labels back upward into clutter
- enlarge labels so much that they dominate the panel
- replace them with `p_{\hat n^+}` / `p_{\hat n^-}` in the restored original-style panel unless explicitly requested

## Relative hierarchy to preserve
The panel should read in this order:
1. directional shell as the main outer structure
2. core shell as the visible internal reference
3. distributed dipole arrows as the local deformation field
4. axial arrows as the emphasized chosen-axis special case
5. `\pm p/2` labels as annotations of that axis case

If any adjustment breaks this hierarchy, reject it.

## Layout preservation constraints
The next pass may adjust layout, but only within tight preservation bounds.

Allowed:
- modest reframing to avoid clipping
- modest scale normalization so panel B can coexist with panel A in the split figure
- small text placement corrections
- small canvas adjustments for manuscript fit

Not allowed:
- re-composing panel B into a different scene concept
- changing the camera enough that the panel reads as a different object
- changing object scale relationships enough that the original balance is lost
- removing channels merely to simplify the picture

## Camera and framing lock
Preserve as closely as possible:
- same camera family/view as the reviewed PyVista panel-B render
- same cutaway orientation
- same left/right directional reading
- same sense of nested shell overlap

Any camera change should be justified only by manuscript-fit necessity.

## Semantic cautions
The preserved panel may still be conceptually overloaded. That is known.
For this pass, that is **not** a reason to simplify it.
The objective is preservation of the original reviewed visual semantics.

Interpretation guidance for accompanying prose/caption:
- describe arrows as constructive/representational or deformation cues
- do not overclaim literal time-process mechanism
- do not let caption simplification drive visual redesign in this pass

## Practical rebuild checklist
Before accepting a rebuilt panel B, confirm all of the following against `...panel-b-pyvista3d-v17.png`:
- scalar-colored outer directional shell present
- inner core-shell reference clearly visible
- distributed dipole arrows present on both sides
- thick axial arrows present on both sides
- endpoint markers present
- lowered `\pm p/2` labels present
- no oversized replacement labels
- no fallback to the simpler shell-plus-channel composition
- no major camera drift
- no major color-logic drift
- no major spacing drift that changes the panel’s feel

## Approval rule
A new panel B should not be promoted into the split figure unless it is judged:
- visually extremely close to `foundations-shells-panel-b-pyvista3d-v17.png`
- semantically equivalent in all major channels
- different only where needed for stability, framing, or minor readability cleanup

## Summary in one line
Restore panel B as a near-preservation of the original reviewed PyVista multi-channel panel, not as a cleaned-up reinterpretation.
