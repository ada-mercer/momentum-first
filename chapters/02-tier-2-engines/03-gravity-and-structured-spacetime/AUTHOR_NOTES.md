# Tier 2 / Gravity - Author Notes

Status: active chapter authoring map
Updated: 2026-07-09
Mode stack: `roles/book-prose + topics/m1/gravity-and-structured-spacetime + artifacts/manuscript + styles/book-mainline + audiences/broad-technical`

Historical July 2026 source-law evolution is archived at `book/dev/planning/GRAVITY_AUTHOR_NOTES_HISTORY_2026-07-09.md`.
This file records the active state only. Do not treat the archived presentation-rule or null-route planning blocks as current authoring guidance.

## Chapter Burden

Chapter 3 should make gravity the first developed Tier 2 engine of the book.

It should:
- establish gravity in M1's physical-first order;
- make the stationary source-to-field-to-observer pipeline feel achieved;
- present the carrier source map as the active M1-native source identification;
- keep GR/classical language downstream as correspondence and calibration;
- give nonstationary gravity bounded room without claiming completion;
- close with honest spacetime lessons and visible open derivation targets.

The chapter should feel firmer and more concrete than Foundations, but still disciplined about claim boundaries.

## Active Section Spine

Rendered wrapper:
`index.qmd`

Included sections:
1. `01-gravity-in-m1.qmd`
2. `02-core-terms-and-variables.qmd`
3. `03-gravitational-sources.qmd`
4. `04-the-stationary-gravitational-field.qmd`
5. `05-local-gravity-and-observer-bookkeeping.qmd`
6. `06-stationary-classical-correspondence.qmd`
7. `07-nonstationary-gravity-extension-track.qmd`
8. `08-spacetime-lessons-and-open-boundaries.qmd`

## Section Jobs

### 3.1 - Gravity in M1

Job: establish the physical claim before machinery appears.

Keep central:
- momentum content changes relational/spatial conditions;
- local clocks, paths, and transported momentum read those altered conditions;
- the primitive route is physical before mathematical.

Avoid:
- heavy equations;
- early source-symbol machinery except as a light forward pointer;
- making gravity sound field-theory-first or GR-geometry-first.

### 3.2 - Core Terms and Variables

Job: act as the concept and notation gateway.

Keep central:
- source -> field -> local readout;
- calligraphic source variables as source packages, not carrier variables;
- scalar-well/depth, shift/directional structure, and local readout variables.

Avoid:
- importing classical stress-tensor notation as primitive;
- turning GR comparison into a fourth primitive layer.

### 3.3 - Gravitational Sources

Job: establish the carrier source map.

Active source law:

```text
mathcal J_k^pm = density of (M pm p_k/2)
mathcal M_k = mathcal M = varrho
mathcal P_k = j_k
```

Keep central:
- the source identification (SI) is a named postulate;
- full `M` appears on every axis, with no `M/3` or axis-share source law;
- `C_ij` is the second transport moment for full momentum accounting, not a third active scalar/shift field source;
- pressure, stress, and radiation do not add separate M1 well weight;
- classical pressure/radiation weights are subsystem apportioning handled in 3.6 and Appendix 3.3A.

Avoid:
- reviving the superseded presentation rule;
- using `T_munu`, Komar weight, radiation factor two, or `varrho/3` as M1 source targets;
- treating the source map as fully micro-derived.

### 3.4 - The Stationary Gravitational Field

Job: build the stationary field representation from the already-earned source packages.

Keep central:
- scalar well from the direction-blind even package;
- directional/shift field from the odd package;
- independent `C_ij` contributions are neglected in the achieved minimal stationary scalar-plus-shift construction;
- two aspects of deformation: clock depth and weak-field spatial stretch;
- `kappa_A=4` as a derived packaging value whose chain is summarized later in 3.6.

Avoid:
- rederiving the source split;
- pulling density/current calibration into the native field-construction section.

### 3.5 - Local Gravity and Observer Bookkeeping

Job: show how local clocks, transported momentum, packaged local magnitude, and stationary generator are read once the field is present.

Keep central:
- `p_{f,c}=p_f G` as contextual clock-scale readout;
- `Pi_i` as shift-dressed transport momentum;
- `M_{g,loc}` as packaged local magnitude, distinct from `H_{g,stat}`;
- observer bookkeeping as readout, not source or field construction.

Avoid:
- calling `M_{g,loc}` simple local energy in the mainline;
- letting quantum/operator material take over. That belongs to Chapter 4.

### 3.6 - Stationary Classical Correspondence

Job: collect downstream classical and GR-facing comparison.

Keep central:
- static density calibration `mathcal M <-> c rho`;
- momentum-form correspondence matrix `P^{mu nu} = [[M, P_j], [P_i, C_ij]]` with `T^{mu nu}=c P^{mu nu}`;
- Newtonian scalar limit;
- shift-current comparison;
- derived `kappa_A=4` chain: SI -> `P_i=j_i`, P2 -> `sigma=1`, boost consistency -> `kappa_A=4`;
- PPN gamma, light bending, Shapiro, and frame-drag endpoint as stationary weak-field checks;
- pressure/radiation reconciliation: total/monopole agreement for isolated stationary systems, spherical exterior agreement, aspherical stress-multipole divergence.

Avoid:
- using correspondence equations as primitive source-law definitions;
- saying dense-star maximum-mass predictions are already delivered. They require an M1 TOV-analogue.

### 3.7 - Nonstationary Gravity Extension Track

Job: present bounded time-dependent gravity.

Keep central:
- locked scalar+shift linear baseline;
- retarded solutions and exact stationary recovery;
- completion ladder for nonlinear, tensor, radiative, and rotating-source work.

Avoid:
- claiming full nonlinear/radiative completion;
- letting nonstationary speculation blur the achieved stationary backbone.

### 3.8 - Spacetime Lessons and Open Boundaries

Job: close the chapter by naming what gravity has forced M1 to say about spacetime and what remains unearned.

Keep central:
- structured spacetime is now a real physical layer in M1;
- stationary gravity is the achieved backbone;
- nonstationary gravity is a bounded extension track;
- `kappa_A` is no longer an open calibration debt;
- SI and P2 are the named hardening targets;
- compact-star structure is a Tier 3 derivation target, not a completed prediction set.

Avoid:
- triumphal closure;
- hiding open nonlinear, rotating-source, tensor, radiative, SI, or P2 burdens.

## Layer Discipline

Keep the three layers visibly distinct:

```text
physical layer -> M1 mathematical layer -> GR/classical correspondence layer
```

- Physical layer: momentum content changes relational/spatial conditions.
- M1 mathematical layer: carrier source map, scalar well, shift, local readout.
- GR/classical correspondence layer: density/current calibration, metric-facing dictionary, standard tests, Kerr/frame-drag comparison.

Do not let `T_munu`, pressure/radiation active weight, lapse/shift vocabulary, or metric notation become the native source law. They are allowed only as comparison, calibration, or appendix-facing audit language.

## Current Source-Law Status

Active source law: carrier source map.

```text
mathcal J_k^pm = density of (M pm p_k/2)
mathcal M_k = mathcal M = varrho
mathcal P_k = j_k
```

Status:
- SI is a named source-identification postulate.
- Given SI, `mathcal M=varrho`, `mathcal P_k=j_k`, and positivity are exact consequences.
- P2 is comoving-cycle readout / depth=stretch, giving weak-field `sigma=1`.
- `kappa_A=4` is derived conditional on SI and P2, with frame drag as endpoint audit.
- Pressure, stress, and radiation enhancements are not M1 source weights. They are classical subsystem apportioning that cancels in total over isolated stationary systems.
- The full momentum-transport accounting includes `C_ij` as a second transport moment; Chapter 3.4 neglects independent `C_ij` field contributions to preserve the minimal stationary scalar-plus-shift construction.
- The deliberate divergence remains in local apportioning, aspherical stress multipoles, compact-star structure, and cosmology handoff.

## Appendix Support Map

Current rendered gravity support appendices:

- `03-03A-carrier-source-map.qmd` - SI, carrier map consequences, pressure/radiation reconciliation.
- `03-03B-null-probe-diagnostic.qmd` - rejected null-route diagnostic and no-go containment.
- `03-03C-momentum-manifestations.qmd` - source-manifestation lookup table.
- `03-04A-stationary-source-to-field-map.qmd` - native source-to-field map.
- `03-04B-depth-equals-stretch.qmd` - P2, weak-field spatial trace, `sigma=1`.
- `03-05A-local-observer-bookkeeping.qmd` - local readout support.
- `03-06A-stationary-correspondence-calibration.qmd` - downstream density/current/Newtonian/metric-facing calibration.
- `03-06B-frame-drag-coefficient-audit.qmd` - endpoint audit of `kappa_A=4`.
- `03-06C-boost-consistency-shift-coefficient.qmd` - boost relation `kappa_A=2(1+sigma)/eta`.
- `03-07A-nonstationary-linear-baseline.qmd` - scalar/shift retarded baseline and stationary recovery.
- `03-07B-nonstationary-completion-ladder.qmd` - nonlinear/tensor/radiative completion ladder.

Appendices should carry algebra, coefficient audits, sign checks, no-go routes, and benchmark detail. Mainline sections should carry the physical object, its job, its regime, and what the reader should take forward.

## Current Open Work

Short active queue:

1. Relabel or de-tautologize `check_carrier_source_map.py` and `check_depth_stretch_pipeline.py` so they are not overread as independent proof of SI.
2. Align Appendix 3.6B wording: "local energy" -> "packaged local magnitude" if still present.
3. Derive the M1 hydrostatic-equilibrium / TOV-analogue before making dense-star maximum-mass, radius, or tidal-deformability predictions.
4. Harden SI with a micro-model of why stage deformation couples to the carrier split.
5. Harden P2 with an equilibrium-size defense for comoving-cycle readout.
6. Continue longer-range gravity work: nonlinear `gamma_ij` dynamics, exact native rotating-source closure, tensor/radiative completion.

Do not keep old completed July repair items as active work. They live in the archive and reviews.

## Verification Expectations

For gravity manuscript or appendix edits, use the relevant subset:

- `python3 scripts/check_crossrefs.py`
- `python3 scripts/check_carrier_source_map.py`
- `python3 scripts/check_depth_stretch_pipeline.py`
- `python3 scripts/audit_frame_drag_coefficient.py`
- `quarto render --profile pdf` when rendered `.qmd` files change.

Treat the two new source/depth scripts as regression and coherence guards unless they are independently strengthened.

## Key Context Pointers

Active/current:
- `book/dev/reviews/GRAVITY_APPENDIX_REPAIR_AND_AUTHOR_NOTES_PLAN_2026-07-09.md`
- `book/dev/reviews/GRAVITY_APPENDICES_INDEPENDENT_REVIEW_2026-07-09.md`
- `book/dev/reviews/GRAVITY_CHAPTER_CARRIER_MAP_REVIEW_2026-07-07_second-pass.md`
- `book/dev/reviews/GRAVITY_CHAPTER_CARRIER_MAP_REVIEW_2026-07-06.md`
- `book/dev/planning/GRAVITY_AUTHOR_NOTES_FULL_REWRITE_PLAN_2026-07-09.md`

Historical:
- `book/dev/planning/GRAVITY_AUTHOR_NOTES_HISTORY_2026-07-09.md`

The old gravity draft remains quarantined in `_old/`. Do not patch it forward.
