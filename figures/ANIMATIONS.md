# Animation readiness

Purpose: prepare figure work so future animations can be added cleanly without inventing the logic from scratch.

## Use animation only when motion is the argument
Good reasons:
- accumulation or propagation over time
- staged transport or transfer
- rotating or phase-dependent relationships
- deformation where the change itself matters

Weak reasons:
- making a static point feel more exciting
- hiding an unclear structure behind motion

## Prepare these before choosing a toolchain
1. one-sentence animation claim
2. storyboard with 3-7 key beats
3. invariant layers
4. changing layers
5. frame-count or timing logic
6. preview target: storyboard strip, GIF, MP4, or frame sequence
7. fallback static figure if animation is not worth it

## Suggested canonical layout
- source scripts: `figures/src/animations/<slug>/`
- committed frames: `figures/build/animations/<slug>/frames/`
- rendered outputs: `figures/build/animations/<slug>/renders/`
- notes/storyboard: `tmp/<slug>/notes.md` or a nearby dev note until the family stabilizes

## First implementation rule
For the first animation in a figure family:
- make the storyboard and static frame strip first
- verify the conceptual sequence with the user
- only then add the render pipeline
