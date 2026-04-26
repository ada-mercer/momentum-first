# Foundations shells split-figure handover (2026-04-18)

## Scope
This note summarizes the current state of the split-shell review figure in `foundations-shells`, focusing on the white-background PyVista review path for:
- Panel A: `p_f -> M`
- Panel B: `M -> p_{\hat n}(\theta)`

Primary implementation file:
- `momentum-first/figures/src/geometry3d/foundations-shells/family.py`

Related backend file:
- `momentum-first/figures/lib/geometry3d/backends/pyvista3d.py`

## Durable family/backend state
- `foundations-shells` is now a fresh geometry3d-native family rebuild, not a thin migration wrapper.
- Family policy still treats `matplotlib3d` as canonical/default and `pyvista3d` as the richer inspection/review backend.
- For the current white-background split-panel review work, PyVista is presently producing the cleaner results faster.

## Figure concept
The figure is currently being developed as a two-stage split concept:
1. Panel A: outward step from fermic shell `p_f` to core shell `M`
2. Panel B: directional deformation from `M` to `p_{\hat n}(\theta)`

This split concept is useful visually and pedagogically, but it is stronger than a purely neutral shell snapshot. It tells a staged story.

## Panel A current state
Panel A has been substantially revised.

### Current visual state
- Arrow placement was reworked from the failed latitude/longitude-like look to a camera-aware spacing on the actual visible cutaway patch.
- The previous failed equal-area attempt was removed because it used asymmetric clipping and produced visibly biased support.
- The arrows now span the full visible gap between the two half-shells rather than only a local portion of the annulus.
- Arrow density was increased by about 50% relative to the previous accepted sparse version.
- Arrowheads were enlarged.
- The cone base radius of the arrowheads was also enlarged, and that wider cone base was promoted into the PyVista vector default.

### What Panel A currently communicates well
- A clear radial separation between the fermic half-shell and the core half-shell.
- A visually coherent outward field across the visible annular gap.
- A cleaner explanatory graphic than the earlier patchy arrow distributions.

### Remaining conceptual tension in Panel A
Panel A still visually suggests a fairly literal outward generative process. That may be too strong if the intended framework meaning is only structural, representational, or bookkeeping-based.

## Panel B current state
Panel B has also been substantially revised.

### Current visual state
- The directional shell is now scalar-colored and rendered more opaquely.
- The directional-shell wireframe was softened so it competes less with the deformation cues.
- The core-shell wireframe was strengthened and made more self-lit so it remains visible through the outer shell.
- Dipole arrows were made thicker, more self-lit, and given a soft underlay to improve contrast.
- The `\pm p/2` labels were moved lower.

### What Panel B currently communicates well
- The deformation away from the core shell is clearer than in earlier versions.
- The core shell remains readable as a reference geometry.
- The directional/dipole structure is more legible than in the earlier high-opacity/low-contrast intermediate versions.

### Remaining conceptual tension in Panel B
Panel B combines several semantic channels at once:
- shell deformation,
- signed scalar coloring,
- dipole arrows,
- axial arrow overlays,
- and the retained core-shell reference.

That makes it effective as an explanatory picture, but somewhat overloaded if the framework wants one clean semantic claim per panel.

## Main conflicts with the current framework

### 1. The figure may overstate process where the framework has only locked structure
Both panels, but especially Panel A, can read as if the framework asserts a literal staged mechanism:
- first `p_f -> M`, then
- `M -> p_{\hat n}(\theta)`.

If the framework only intends these as structural relations or equivalent descriptive packagings, the figure is stronger than the formal wording.

### 2. Arrow semantics are not yet canonically defined
The arrows currently do useful explanatory work, but their meaning is not fully locked.
They could be interpreted as:
- transport,
- growth,
- generative mapping,
- displacement,
- or bookkeeping relation.

Without a stated convention, the visuals risk overclaiming.

### 3. The split two-stage story is visually ahead of the formal framework
The figure now strongly encourages the reading that the shell logic is naturally decomposed into two successive conceptual stages.
That may be a good exposition strategy, but it should be explicitly endorsed by the framework if it is to become stable.

### 4. Panel B may be carrying too many explanatory burdens at once
The framework might want to separate:
- pure geometric shell relation,
- directional sign structure,
- and axial annotation of `\pm p/2`,
into distinct views or clearer hierarchy.

## Where the framework could support this figure better

### A. Explicitly classify Panel A
The framework should state whether Panel A is meant as:
- a literal generative process,
- a geometric construction,
- a bookkeeping decomposition,
- or a pedagogical visual metaphor.

### B. Define arrow meaning once
A short framework-side convention would help, for example:
- arrows indicate a constructive mapping between shell descriptions,
- not a dynamical time process.

Or, if a dynamical reading is intended, say that explicitly instead.

### C. Canonically bless or reject the two-stage reading
The framework should decide whether the split figure’s logic is canonically:
1. `p_f -> M`
2. `M -> p_{\hat n}(\theta)`

If yes, it deserves a short official statement in framework prose.
If no, the figure should be toned down or reframed.

### D. Provide figure-specific notation hierarchy
The framework could better support the figure by specifying what should be foregrounded in each panel:
- shell names,
- algebraic labels,
- directional sign encoding,
- and whether `\pm p/2` is primary or secondary.

### E. Separate structural geometry from causal interpretation
A stronger framework note distinguishing:
- what is geometry/packaging,
- what is mechanism,
- and what is merely pedagogical,
would make this figure much safer and more useful.

## Recommended handover summary
- The split-shell review figure is now visually much stronger than earlier iterations, especially in PyVista on white background.
- Panel A now has camera-aware, full-gap, denser arrows with larger arrowheads and a wider cone base.
- Panel B now has a clearer hierarchy between core-shell reference, directional shell, and dipole arrows.
- The main unresolved issue is no longer purely rendering. It is framework alignment: the figure currently tells a stronger staged/process story than the framework has explicitly locked.

## Suggested next decisions
1. Decide whether the split-panel story is only pedagogical or canonically structural.
2. Decide what arrows mean in the framework.
3. Decide whether Panel B should remain multi-channel or be simplified.
4. If this split figure is retained, add one short framework-side prose lock that matches the visual logic.
