# Part III — Gravity and Structured Spacetime: Author Notes

## Fresh-start status

The previous Part III draft has been quarantined in `_old/`.
Do not patch that prose forward.
Write this part fresh from the current planning architecture and reference packets.

## Authoring objective

Part III should read as the first major developed engine of the book.
It should:
- establish gravity in M1 cleanly,
- make the stationary package feel achieved and trustworthy,
- give the nonstationary package explicit bounded room,
- and close with honest spacetime lessons plus visible open boundaries.

## Current chapter spine

1. `03-01-gravity-in-m1.qmd`
2. `03-02-gravity-side-core-terms-and-variables.qmd`
3. `03-03-gravitational-sources.qmd`
4. `03-04-the-stationary-gravitational-field.qmd`
5. `03-05-local-gravity-and-observer-bookkeeping.qmd`
6. `03-06-stationary-classical-correspondence.qmd`
7. `03-07-nonstationary-gravity-extension-track.qmd`
8. `03-08-spacetime-lessons-and-open-boundaries.qmd`


## Structural review pass — 2026-05-03

Current judgment: the eight-chapter spine is sound. The next prose pass should not collapse the correspondence chapter or restart the part. The active problem is burden drift inside otherwise correct chapter jobs.

### Chapter burden locks

1. **3.1 — physical-first philosophical approach**
   Establish the primitive route: momentum content -> relational/spatial stress or deformation -> altered local clock/path/transport conditions. Mention propagation only with stationary/nonstationary boundaries clear.
2. **3.2 — concept/symbol gateway**
   Keep the working route explicit: source -> field -> observer. Field variables represent relational/spatial deformation; GR comparison stays downstream, not a fourth or fifth primitive layer.
3. **3.3 — source construction**
   Own `J_k^±`, `M_k`, and `P_k`. Do not force 3.4 to rederive the source split.
4. **3.4 — stationary field representation**
   Start from the source packages already earned and build the scalar-well/shift map. Keep classical density/current comparison out.
5. **3.5 — local observer bookkeeping**
   Give clocks, transported momentum, local/asymptotic distinction, and frame-drag-like readout enough physical texture that the observer layer feels earned.
6. **3.6 — stationary classical correspondence**
   Preserve as the collection point for density/current calibration, Newtonian limit, metric dictionary, lapse/shift, Kerr/proper-time comparison.
7. **3.7 — bounded nonstationary extension**
   Present a maturity ladder: locked linear baseline -> conditional nonlinear family -> tensor/radiative slot -> open completion.
8. **3.8 — spacetime lessons and open boundaries**
   Reduce recap. Answer the structural question: what has gravity forced M1 to say about spacetime, and what remains unearned?

### Cleanup note

There are unrendered `* copy.qmd` files in this directory. They clutter structural inspection and should be archived or removed in a cleanup pass after confirming they are not intentional backups.


## Current restructuring decision — opening chapters

The opening should be split by burden, not polished as one overloaded chapter.

### 3.1 — philosophical approach

`03-01-gravity-in-m1.qmd` should make the reader understand the physical M1 gravity claim before any machinery appears.

Primary burden:
- momentum is primary physical content;
- gravity begins when momentum content changes the relational/spatial conditions in which other momentum is expressed;
- the first description is physical: stress, deformation, structuring of the relational stage, altered local conditions;
- clocks, paths, and transported momentum are local readouts of that altered condition;
- fields and GR geometry are later descriptions/compressions, not the primitive phenomenon.

Avoid in 3.1:
- heavy equations;
- early symbolic machinery (`J_k^±`, `M_k`, `P_k`) except as a light forward pointer;
- scalar-well/shift details except as a deferred promise;
- making the route sound like field theory first or GR geometry first.

Preferred physical spine:

```text
momentum content -> relational/spatial stress or deformation -> altered local clock/path/transport conditions
```

Then hand off to 3.2 for the vocabulary needed to make this precise.

### 3.2 — core concepts, source-field-observer route, and symbols

`03-02-gravity-side-core-terms-and-variables.qmd` should become the disciplined concept and notation gateway.

Primary burden:
- define the source -> field -> observer route;
- keep physical deformation, M1 field representation, and GR comparison conceptually distinct without turning them into five route layers;
- introduce source symbols `J_k^+`, `J_k^-`, `M_k`, and `P_k`;
- introduce scalar-well/depth and directional/shift language as mathematical representation of deformation modes;
- prepare the reader for the source, stationary-field, local-readout, and nonstationary chapters.

### Layer discipline

Keep these categories visibly distinct:

- **Physical layer:** stress, deformation, structuring, relational/spatial stage, altered local clock/path/transport conditions.
- **M1 mathematical layer:** source variables, field variables, scalar-well sector, shift/directional sector, stationary field package.
- **GR comparison layer:** metric, curvature, lapse/shift, Kerr pullback, stationary dictionary, correspondence/calibration/geometric compression.

Do not write as though “field/background” is the primitive physical phenomenon. Field variables are the mathematical description introduced after the physical deformation claim is clear.


## Stationary correspondence split

`03-06-stationary-classical-correspondence.qmd` is an intentional collection chapter.

Its job is to keep classical density/current/metric-facing comparison out of the native construction chapters as much as possible:

- `03-03` should build the source layer in M1 terms.
- `03-04` should build the stationary field representation in M1 terms.
- `03-05` should build local observer bookkeeping in M1 terms.
- `03-06` should then collect calibration and comparison: source-density mapping, Newtonian scalar limit, shift-current comparison, metric-facing dictionary, and local clock/transport comparison.

This split protects the philosophical order of Part III. Native construction comes first; classical and GR-readable correspondence comes afterward as calibration/compression, not as the primitive explanation.

## Mainline discipline

Keep central:
- stationary-first scope,
- source -> field -> observer grammar,
- bounded correspondence language,
- local bookkeeping discipline,
- explicit maturity labels,
- nonstationary gravity as a real extension track but not full completion.

Keep out of the mainline:
- long derivation sprawl,
- coefficient/gauge audit tables,
- reduced-model teaching math beyond what the prose truly needs,
- speculative torus or deep-geometry takeover,
- BFSS/string grounding,
- Part IV QM/Dirac spillover,
- divergence hunting as a chapter backbone.

## Appendix rule

Be aggressive about moving derivation-heavy material to appendices.
Main text should answer:
- what the object is,
- why it is introduced,
- what job it does,
- what regime it holds in,
- and what the reader should carry forward.

Appendices should answer:
- how the algebra closes,
- why the signs/coefficients are trustworthy,
- which alternatives were checked or demoted,
- and where the technical trust layer lives.

## Appendix map

Current rendered Part III support appendices:
- `appendices/derivations/03-04A-stationary-source-to-field-map.qmd` — native primitive `J_k^±` source-to-field map, including integral and differential forms.
- `appendices/derivations/03-05A-local-observer-bookkeeping.qmd` — local scalar dressing, shift-dressed transport momentum, packaged local magnitude, and generator/readout distinction.
- `appendices/derivations/03-06A-stationary-correspondence-calibration.qmd` — density/current/Newtonian/metric-facing stationary calibration.
- `appendices/derivations/03-07A-nonstationary-linear-baseline.qmd` — locked linear scalar+shift baseline, retarded solutions, stationary recovery, and benchmark verdict.
- `appendices/derivations/03-07B-nonstationary-completion-ladder.qmd` — promoted nonlinear family, tensor slot, radiative/backreaction status, rotating-source closure ladder, and completion checklist.

Completion posture:
- the stationary appendix set protects 3.4–3.6 from derivation sprawl while preserving trust-layer detail;
- the nonstationary appendix pair makes 3.7 completion-ready without letting the chapter overclaim;
- exact native rotating-source/Kerr closure and full nonlinear radiative completion remain open, but their target ladder is now localized rather than vague.

## Key reference stack before drafting

For the stationary backbone:
- `book/dev/M1_GR_STATIONARY_REFERENCE_PACKET_V1.md`
- `book/tiers/T1_foundations/GR_MINIMAL_CORRESPONDENCE_SKELETON_V1.md`
- `book/tiers/T1_foundations/GR_CONVENTION_LOCKS.md`

For the nonstationary extension track:
- `book/dev/M1_NONSTATIONARY_PACKET_PLANNER_HANDOFF_V1.md`
- `book/dev/M1_NONSTATIONARY_LINEAR_BASELINE_REFERENCE_V1.md`
- `book/dev/M1_NONSTATIONARY_BASELINE_BENCHMARKS_V1.md`
- `book/dev/M1_NONSTATIONARY_COMPLETION_STATUS_MATRIX_V1.md`

For planning boundaries:
- `momentum-first/BOOK_STRUCTURE_PLAN.md`
- `book/dev/PART_III_AUTHOR_HANDOFF_2026-04-11.md`

## Local tone target

This part should feel:
- firmer and more concrete than Foundations,
- more physically explanatory than purely formal,
- disciplined about claim boundaries,
- and refreshingly free of internal-planning noise.

The reader should feel that gravity is a real program here, not a placeholder, but also not a bluff.
