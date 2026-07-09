# Tier 2 / Gravity — Gravity and Structured Spacetime: Author Notes

## Fresh-start status

The previous gravity draft has been quarantined in `_old/`.
Do not patch that prose forward.
Write this chapter fresh from the current planning architecture and reference packets.

## Authoring objective

The gravity chapter should read as the first major developed engine of the book.
It should:
- establish gravity in M1 cleanly,
- make the stationary package feel achieved and trustworthy,
- give the nonstationary package explicit bounded room,
- and close with honest spacetime lessons plus visible open boundaries.

## Current section spine

1. `01-gravity-in-m1.qmd`
2. `02-core-terms-and-variables.qmd`
3. `03-gravitational-sources.qmd`
4. `04-the-stationary-gravitational-field.qmd`
5. `05-local-gravity-and-observer-bookkeeping.qmd`
6. `06-stationary-classical-correspondence.qmd`
7. `07-nonstationary-gravity-extension-track.qmd`
8. `08-spacetime-lessons-and-open-boundaries.qmd`


## Structural review pass — 2026-05-03

Current judgment: the eight-section spine is sound. The next prose pass should not collapse the correspondence section or restart the chapter. The active problem is burden drift inside otherwise correct section jobs.

### Section burden locks

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

`01-gravity-in-m1.qmd` should make the reader understand the physical M1 gravity claim before any machinery appears.

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

`02-core-terms-and-variables.qmd` should become the disciplined concept and notation gateway.

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

`06-stationary-classical-correspondence.qmd` is an intentional collection chapter.

Its job is to keep classical density/current/metric-facing comparison out of the native construction chapters as much as possible:

- `03-gravitational-sources.qmd` should build the source layer in M1 terms.
- `04-the-stationary-gravitational-field.qmd` should build the stationary field representation in M1 terms.
- `05-local-gravity-and-observer-bookkeeping.qmd` should build local observer bookkeeping in M1 terms.
- `06-stationary-classical-correspondence.qmd` should then collect calibration and comparison: source-density mapping, Newtonian scalar limit, shift-current comparison, metric-facing dictionary, and local clock/transport comparison.

This split protects the philosophical order of the gravity chapter. Native construction comes first; classical and GR-readable correspondence comes afterward as calibration/compression, not as the primitive explanation.

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
- later QM/Dirac spillover,
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

Current rendered gravity support appendices:
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

This chapter should feel:
- firmer and more concrete than Foundations,
- more physically explanatory than purely formal,
- disciplined about claim boundaries,
- and refreshingly free of internal-planning noise.

The reader should feel that gravity is a real program here, not a placeholder, but also not a bluff.

## Planning block — shift-sector calibration and the factor 4 (2026-07-02)

Decision source: Review-topic discussion (Ada + Arne), gravitomagnetic factor-4 finding.

### Structural decisions
- Source grammar (`J_k^±`, `M_k`, `P_k`, kernels, 3.3–3.4 native construction) is protected: no factor absorbed into sources.
- Shift packaging becomes `A_i := -kappa_A * theta_i^perp` with `kappa_A` an explicitly labeled, coefficient-conditional calibration constant. Definition stays in 3.4 (forward-referencing 3.6 for the value) so the 3.5 transport bookkeeping keeps a single `A_i` object.
- 3.6 keeps the chapter's correspondence job; add subsection "Shift calibration and the factor 4": fixes `kappa_A` from the audit, presents the two physical factors of 2 (even-source sharing with the spatial sector; velocity cross-term in the response), and records the ledger rule that one factor of 2 is expected to migrate into the future `gamma_ij` construction (anti-double-counting).
- No new correspondence section: 3.6 already carries that role.
- QM chapter deliberately out of scope for this package (lapse/generator question is a separate work item).

### Appendix plan (roles per VERIFICATION_POLICY taxonomy)
- `03-06B-frame-drag-coefficient-audit.qmd` (new; role: correspondence/calibration audit, NOT derivation). End-to-end Lense-Thirring in current conventions: rotating source -> P_k -> theta_i -> A_i -> Pi cross term -> precession vs GR. Determines whether the missing coefficient is 2 or 4 (Pi cross term may already supply a 2). BLOCKS all kappa_A prose.
- `03-03A-null-channel-source-diagnostic.qmd` (new; role: conditional derivation — inspectable counting GIVEN the identification `J_k^± ~ T(l_k^±, l_k^±)`, which is itself labeled interpretation/speculative). Contents: momentum-presentation reading of T_munu, native factor-4 counting via odd combination = 4 T^{0k}, NEC-grounded positivity, dust/photon calibration, Komar/pressure bonus. Explicitly a diagnostic/derivation-track note, not the primitive channel definition.
- Boost-consistency derivation: named as planned future appendix (lock criterion: kappa_A graduates from calibration to derivation when null-channel route and boost consistency independently force the audited value). Not written in this package.
- `02-03A` gets a one-paragraph scope note: uniqueness claim covers linear charge-like splits; quadratic flux-like source channels are outside its scope (pre-empts the 1/2-vs-1 weight tension).

### Sequencing (dependency order, not drafting order)
1. Hygiene fixes (ADMC typos + positivity line in Foundations 2.2; section/chapter reference sweep in ch.3; units-prose unification in 3.3; delete two " copy.qmd" appendix duplicates).
2. 03-06B audit -> fixes kappa_A value.
3. 3.4 / 3.5 / 3.6 / 3.8 edits + 03-04A, 03-06A propagation.
4. 03-03A null diagnostic + 02-03A scope note (additive; can draft in parallel with 3).
5. glossary.yml terms (kappa_A, null source channels, momentum presentation tensor), quarto render + crossref check, version bump (v0.4.0-shaped), RELEASES.md.

Branch: `gravitomagnetic-calibration`, PR per STANDARDS (broad change).

### Open decisions
- Exact kappa_A value: pending audit (do not assume 4).
- Whether 03-03A's T_munu interpretation later earns a Foundations-level continuum note: deferred until the derivation track locks.

## Planning block — null-flux source-route derivation outcome (2026-07-03)

Decision source: Derivation-topic null-flux source-route session.

Primary outputs:
- `book/dev/M1_NULL_FLUX_SOURCE_CONSTRUCTION_V1.md`
- `book/dev/M1_NULL_FLUX_MATTER_CONSEQUENCES_V1.md`
- `book/dev/M1_NULL_FLUX_TIER1_RELATION_V1.md`
- `book/dev/M1_BOOST_CONSISTENCY_SHIFT_COEFFICIENT_V1.md`
- `book/dev/M1_NULL_FLUX_PROMOTION_ASSESSMENT_V1.md`
- `book/dev/scripts/null_flux_source_route_audit_v1.py`

### Verdict

Do not promote the literal null-flux identification

```text
J_k^± = lambda * T(l_k^±, l_k^±)
```

to the primary source definition yet.

With the existing dust scalar calibration, the literal route fixes:

```text
lambda = 1/(3c)
P_i = (4/3) j_i
```

Therefore the Lense-Thirring endpoint requires `kappa_A = 3` in the promoted-null source convention, not the currently audited `kappa_A = 4` package. Keeping `kappa_A = 4` with literal null promotion overshoots the endpoint by `4/3`.

### Matter consequences

The literal null route gives a rest-frame perfect-fluid scalar source proportional to:

```text
rho + p/c^2
```

not the Komar/static-GR target:

```text
rho + 3p/c^2
```

Consequences:
- dust remains safe;
- isotropic radiation gives `4/3` rather than the factor-2 target;
- relativistic-star pressure is underweighted;
- a cosmological-constant-like stress tensor has zero null-channel content because `T(l,l)=0` for `T_mn proportional to g_mn`.

The vacuum-energy filtering may be a deep feature, but it is not safe to import into the mainline until the cosmology sector is checked against it.

### Tier-1 relation

No Tier-1 split change.

The null-flux channels are quadratic flux/source presentations:

```text
T(l_k^±, l_k^±) proportional to (M ± p_k)^2/M
```

They are not the affine ADMC channels:

```text
p_{k^±} = M ± (1/2)p_k
```

The Derivation 2.3A scope note remains correct: linear charge-like ADMC splits and quadratic stress-flux source presentations are different mathematical classes.

### Boost-consistency result

Boost consistency gives a conditional family, not an independent lock:

```text
current P_i = j_i convention:        kappa_A = 2(1 + sigma)
literal null-promoted convention:    kappa_A = (3/2)(1 + sigma)
```

Here `sigma` is the still-open isotropic spatial trace coefficient in:

```text
gamma_ij ~= (1 + 2 sigma theta_0) delta_ij
```

Thus the current convention reaches `kappa_A=4` only after assuming or deriving `sigma=1`; the literal null route reaches `kappa_A=3` even with `sigma=1`.

### Future manuscript implications

For a later manuscript session:
- Keep 3.3 source grammar native; do not redefine `J_k^±` as literal stress-tensor null contractions.
- Revise 03-03A from "possible successful lock route" to "diagnostic plus literal-promotion no-go".
- Keep 03-06B as the valid audit of `kappa_A=4` in the current `P_i=j_i` convention.
- Rewrite 3.6's factor story: the observer cross term supplies no factor of 2; the old expectation that future `gamma_ij` makes the shift coefficient re-audit to 2 is unsupported.
- Defer any Foundations-level `T_munu` continuum note or glossary promotion of null source channels.

Recommended next derivation target: either a trace-adjusted/null-inspired source map that can address pressure and normalization, or a native derivation/no-go for the spatial trace selector `sigma=1`. Manuscript integration is premature.

## Planning block — presentation-source derivation closure (2026-07-04)

Decision source: Derivation-topic presentation-source session.

Primary outputs:
- `book/dev/M1_ODD_SECTOR_PRESENTATION_RULE_V1.md`
- `book/dev/M1_DEPTH_EQUALS_STRETCH_DERIVATION_V1.md`
- `book/dev/M1_PRESENTATION_PIPELINE_SYNTHESIS_V1.md`
- `book/dev/scripts/m1_odd_sector_presentation_rule_v1.py`
- `book/dev/scripts/m1_depth_stretch_pipeline_v1.py`

### Verdict

The zero-calibration stationary pipeline closes at weak-field order if the new presentation rule and depth=stretch argument are accepted:

```text
P_i = j_i
sigma = 1
kappa_A = 2(1 + sigma) = 4
```

The Lense-Thirring endpoint remains the audited check, but `kappa_A=4` no longer has to be presented as an empirical calibration in the mature version of the package.

### Odd-sector rule

Use the presentation rule:

```text
M_k = T_00/(3c) + T_kk/c
P_k = T_0k/c
J_k^+ = M_k + P_k/2
J_k^- = M_k - P_k/2
```

This reproduces the fixed even-sector entries with one normalization and gives slow-dust `P_i=j_i`.

Directed-beam verdict: exact forward chirality does not survive this rule. For a beam along `+x`:

```text
J_x^+ = 11 epsilon/(6c)
J_x^- =  5 epsilon/(6c)
```

Exact chirality would require `P_x=(8/3)j_x`, conflicting with the slow-dust source convention. Keep exact chirality as a feature of the literal null-contraction diagnostic only, not as a requirement of the presentation reading.

### Depth=stretch

The M1 time stance now supplies the spatial trace selector. A confined clock cycle at local `c` reads an isotropic spatial stretch by reciprocal cycle rate:

```text
G_stretch = (1 + 2 sigma theta_0)^(-1/2)
```

Matching the scalar clock package:

```text
G = sqrt(1 - 2 theta_0)
```

forces `sigma=1` at weak-field order. This gives PPN `gamma=1`, standard leading light bending, standard Shapiro delay, and the boost-consistency value `kappa_A=4`.

### Future manuscript implications

For a maturity/manuscript session:
- update 3.3 with the presentation rule while keeping channels native;
- rewrite 03-03A as literal-null diagnostic/no-go rather than a successful lock route;
- revise 3.6 so `kappa_A=4` is presented as derivation-track closed, with 03-06B as endpoint audit;
- remove the old expectation that future `gamma_ij` should re-audit the shift coefficient to `2`;
- revise 3.8 so `kappa_A=4` is no longer listed as an open calibration debt;
- revisit the parked units-prose edit, because the transport/presentation reading supports per-area-per-time phrasing.

Recommended next session: maturity/manuscript integration for the gravity source/correspondence package, not further coefficient derivation. Keep full nonlinear `gamma_ij`, exact rotating-source closure, and nonstationary tensor/radiative completion as open boundaries.

## Planning block — derived-pipeline chapter integration (2026-07-04)

Supersedes the 2026-07-02 planning block and the parked `gravitomagnetic-calibration`
branch as the controlling plan. Decision source: Review-topic derivation sessions
(null-flux no-go -> presentation reading -> odd-sector rule + depth=stretch closure).

### Inputs (accepted derivation-track notes)
- `book/dev/M1_MOMENTUM_MANIFESTATIONS_TO_JK_CHANNELS_V1.md` (dictionary; no vacuum row)
- `book/dev/M1_ODD_SECTOR_PRESENTATION_RULE_V1.md` (P_i=j_i; beam chirality rejected)
- `book/dev/M1_DEPTH_EQUALS_STRETCH_DERIVATION_V1.md` (sigma=1; PPN gamma=1)
- `book/dev/M1_BOOST_CONSISTENCY_SHIFT_COEFFICIENT_V1.md` (kappa_A=2(1+sigma))
- `book/dev/M1_PRESENTATION_PIPELINE_SYNTHESIS_V1.md` (integration map)
- Ada review verdict: accepted as V1 "closed under two named premises":
  (P1) uniform 1/c normalization across the three presentation roles;
  (P2) comoving-cycle readout (clock rate = reciprocal stretch).
  Manuscript prose MUST name both premises with their checks (hygiene rules).

### Section jobs (target state)
- 3.3 Sources: presentation rule becomes the source law. Channels stay native/primary;
  presentation decomposition (content share / stress-transport / net traversal) gives
  `M_k = T_00/(3c) + T_kk/c`, `P_k = T_0k/c`, stress notation introduced as
  correspondence compression, not ontology. Manifestation dictionary (dust, gas, photon
  gas, beam, EM, rotating body) in compact table. Units prose: transport/per-area-per-time
  presentation reading (REVERSES the parked hygiene edit). No vacuum row; one-sentence
  pointer that Lambda-shaped phenomenology belongs to chi(t) (full falsifier discussion
  belongs to the expansion chapter, not here).
- App 03-03A (rewrite): presentation-rule derivation + manifestation table + beam
  verdict. Null-contraction diagnostic demoted to its own short appendix 03-03B
  ("null-probe diagnostic and no-go"), preserving NEC-positivity and exact-chirality
  results with their correct owner.
- 3.4 Field: kernel unchanged. New subsection "the two aspects of deformation": even
  source produces depth AND isotropic stretch (`gamma_ij=(1+2 theta_0) delta_ij` weak
  field, sigma=1 stated, derivation in App 03-04B). `A_i=-kappa_A theta_i^perp` stays,
  kappa_A now announced as derived (chain summarized in 3.6).
- App 03-04B (new): depth=stretch derivation (cycle-readout argument, premise P2 named,
  weak-field boundary stated).
- 3.5 Observer: light touch — clock dressing `p_f,c=p_f G` reframed as cycle readout of
  the deformed stage (one paragraph); bookkeeping unchanged.
- 3.6 Correspondence: rewrite "Shift calibration and the factor 4" -> "The shift
  coefficient derived": chain = presentation rule (P_i=j_i) + depth=stretch (sigma=1)
  + boost consistency -> kappa_A=4; 03-06B audit re-statused as endpoint validation;
  REMOVE the kappa_A->2 expectation and the observer-cross-term factor story entirely.
  NEW correspondence block: PPN gamma=1, light bending, Shapiro delay at standard
  values — the chapter may now claim these at weak-field stationary order.
- App 03-06C (new): boost-consistency derivation kappa_A=2(1+sigma) (currently dev-note
  only; it is part of the derivation chain and needs a manuscript home).
- App 03-06B: keep; status language from "calibration" to "correspondence check of the
  derived coefficient".
- 3.7: unchanged apart from one sentence noting the stationary package feeding it is
  now derived.
- 3.8: remove kappa_A from open debts; add the two named premises as hardening items
  (circulation micro-model for P1; equilibrium-size defense for P2); keep nonlinear
  gamma_ij dynamics, native rotating closure, tensor/radiative completion open.
- Foundations 2.6 (KM taxonomy): one careful paragraph — gravitational clock dressing
  remains composition-modifier bookkeeping, but its origin is now read as cycle readout
  of stage deformation (interpretation shift, no equation change).
- Keep from parked branch: ADMC typo fixes, positivity line, section-reference sweep
  (NOT the units-prose edit). Scripts: promote both dev scripts into repo `scripts/`
  with the audit script; keep CI-runnable.
- Glossary: presentation rule terms; version: 0.4.0-dev is now justified (new derived
  results); RELEASES entry.

### Git strategy (separate commit/release session ONLY)
- Close PR #1 unmerged; delete remote+local `gravitomagnetic-calibration` branch.
  (Note: GitHub PRs can be closed, not deleted — the PR record remains visible in the
  PR list, but main's history stays clean since nothing was merged.)
- Build fresh branch `gravity-derived-pipeline` from main; commit the final working-tree
  state as a small set of logical commits (hygiene / source rule + appendices / chapter
  integration / meta). No exploration archaeology in the history.
- The parked authorship/provenance working-tree package is committed separately
  (own branch/PR), never mixed with this work.

### Sequencing
1. Integration authoring session: full .qmd edits in working tree per this block;
   render + crossref + scripts verified locally; NO git operations.
2. Commit/release session: diff review, PR#1 closure + branch deletion, fresh branch,
   logical commits, new PR for Arne's approval.

### Open decisions
- None blocking integration. Hardening items (P1 micro-model, P2 defense) proceed in
  parallel as derivation sessions; if P2 fails, 3.6 falls back to "boost-consistent
  package validated by PPN checks" wording (fallback text should be drafted in the
  integration session as a comment block).

### Addendum (2026-07-04, later): manifestation dictionary gets its own appendix
- NEW Appendix 03-03C "Momentum manifestations and source channels": the full
  dictionary from `book/dev/M1_MOMENTUM_MANIFESTATIONS_TO_JK_CHANNELS_V1.md` as a
  reference appendix. Per manifestation: physical description in channel language,
  stress components in the presentation frame, resulting `J_k^±`/`M_k`/`P_k`, and a
  status line (derived / convention / agreement-with-GR). Entries: cold matter, moving
  dust (incl. O(v^2) ram terms), ideal gas, isotropic photon gas, directed null beam
  (incl. the chirality verdict cross-ref to 03-03B), rotating body, stressed solid
  (tension/compression, positivity bound remark), static EM field (trace-free weight 2).
  Closing remark: no vacuum row, pointer to chi(t).
- Purpose: durable lookup that settles pressure/stress translation questions once;
  3.3's mainline table becomes a short summary pointing here.
- 03-03A keeps the derivation of the rule; 03-03C holds the applications. Register in
  both `_quarto.yml` lists.

## Completion note — derived-pipeline chapter integration (2026-07-04)

The integration authoring session executed the 2026-07-04 planning block (with
addendum) in the working tree. No git operations were performed.

Done:
- 3.3 rewritten: presentation rule as source law (channels primary, stress notation
  as correspondence compression), transport units prose restored, summary
  manifestation table pointing to 3.3C, no vacuum row + one chi(t) pointer,
  premise P1 named.
- Appendices: 03-03A rewritten as the presentation-rule derivation (P1 named, beam
  verdict); NEW 03-03B null-probe diagnostic + no-go (NEC positivity and exact
  chirality preserved under correct owner); NEW 03-03C manifestation dictionary
  (8 entries, per-entry status, no vacuum row); NEW 03-04B depth=stretch (P2 named,
  weak-field boundary); NEW 03-06C boost consistency kappa_A=2(1+sigma); 03-06B
  re-statused to endpoint correspondence check; 03-04A/03-06A/02-03A propagated.
  All registered in both _quarto.yml lists.
- 3.4: "two aspects of deformation" subsection (gamma_ij=(1+2 theta_0) delta_ij,
  sigma=1, ref 3.4B); kappa_A announced as derived.
- 3.5: cycle-readout paragraph; bookkeeping unchanged.
- 3.6: "The shift coefficient derived" (P1 -> P_i=j_i; P2 -> sigma=1; boost ->
  kappa_A=4; audit as endpoint); premises P1/P2 stated with checks; old two-factors
  story and kappa_A->2 expectation removed (replaced by the input-not-absorber
  point); P2-failure fallback wording drafted as HTML comment in the file; NEW
  "classical weak-field tests" block (PPN gamma=1, bending, Shapiro).
- 3.7: one derived-pipeline sentence. 3.8: kappa_A removed from debts; P1
  micro-model and P2 equilibrium-size defense added as hardening targets;
  nonlinear gamma_ij dynamics, rotating closure, tensor/radiative stay open.
- Foundations 2.6: one interpretation paragraph (clock dressing as cycle readout
  of stage deformation; no equation change).
- Scripts promoted: scripts/check_carrier_source_map.py,
  scripts/check_depth_stretch_pipeline.py (plus existing audit script).
- Glossary: kappa_A re-statused; presentation rule/roles added; null source
  channels re-statused to no-go. RELEASES.md: draft v0.4.0-shaped entry appended.
  VERSION left at 0.3.3-dev (commit session decides).

Verified locally: quarto render (PDF profile) OK; check_crossrefs.py OK; all three
physics scripts pass; greps clean (no calibration-language for kappa_A in mainline,
no ADMC typos in rendered files, no vacuum-energy source language).

Flagged, non-blocking:
- The unrendered "* copy.qmd" duplicates remain in chapter/foundations dirs (still
  the standing cleanup-pass item; one of them contains the old ADMC typos but is
  not rendered).
- Next sessions: commit/release per the git-strategy block; P1/P2 hardening
  derivation sessions in parallel.

## Revision note — native-prose repair of the source law (2026-07-05)

The 2026-07-04 integration let classical concepts (energy density, $T_{00}$,
$T_{kk}$, $T_{0k}$) bleed into mainline prose, most visibly the stress-tensor
display of the presentation rule in Chapter 3.3. Mainline chapters build M1
from the ground up; classical packaging belongs to the correspondence layer.
Repaired as follows, working tree only:

- Ch 3.3: presentation rule restated in native densities —
  $M_k=\varrho/3+\varrho^{\mathrm{tr}}_k$, $P_k=j_k$, with $\varrho$ = local
  momentum-content density, $\varrho^{\mathrm{tr}}_k$ = content in transit
  across axis $k$. Stress-tensor display removed from 3.3; manifestation table
  recast in native/qualitative weights; photon factor-2 now carries its native
  mechanism (all light content is in transit: counted once as present, once as
  crossing). Role renamed: stress-transport -> transit.
- Ch 3.6: canonical home of the classical compact form
  $M_k=T_{00}/(3c)+T_{kk}/c$, $P_k=T_{0k}/c$, displayed with the native->classical
  translation ($\varrho=T_{00}/c$, $\varrho^{\mathrm{tr}}_k=T_{kk}/c$, $j_k=T_{0k}/c$).
- Ch 3.5: "local energy" -> "packaged local magnitude $M_{g,loc}$".
  Ch 3.7: "shift-field energy" -> "shift-sector field content".
- Appendix 3.3A: role renamed (transit), native form cross-referenced; appendix
  keeps classical variables since its checks face classical targets.
- Glossary: presentation rule/roles restated native-first; new
  momentum_content_density entry for $\varrho$, $\varrho^{\mathrm{tr}}_k$.

Root cause (for future sessions): the derivation dev-note synthesis
(M1_PRESENTATION_PIPELINE_SYNTHESIS_V1, internal/technical mode) carries the
rule in $T_{\mu\nu}$ form; the integration treated that planning form as prose
law instead of translating it into native chapter language, against the
book-prose role guardrails ("plans as orientation, not prose law"; no
standard-theory anchoring in native-structure sections). Rule of thumb going
forward: equations imported from dev notes must be re-derived into chapter
notation before they enter mainline prose; the classical form of any source
law renders only in Ch 3.6 or appendices.

### Addendum (2026-07-05, later): sectoral retelling of the presentation rule

Ch 3.3 presentation rule restated in M1 sector ontology instead of role taxonomy:
fermic presence isotropic (loop-forced); bosic sector enters twice (presence at
full core-momentum weight, transit at crossing-speed weight — quadratically
suppressed for slow matter, full weight for light); odd package = the bosic
sector's net component (P_k = j_k derived from the sector split). Equations
unchanged. The bosic presence distribution (isotropic 1/3 share applied to bosic
content) is now named in mainline prose as the open distribution question and
the sharp edge of P1; 3.8 debt item and Appendix 3.3A non-claim rephrased
accordingly ("derive the bosic presence distribution" replaces "derive the 1/3
share"). Role vocabulary aligned to presence/transit/net traversal in 3.6,
glossary, and 3.3A. Verified: render, crossrefs, physics scripts all pass.

### Addendum (2026-07-06): carrier-map source rewrite

The 2026-07-05 sectoral retelling still carried too much classical source
apportioning into the main source law. The current rewrite replaces the
"presentation rule" with the M1-native carrier source map:

```text
mathcal J_k^pm = density of (M pm p_k/2)
mathcal M_k = varrho
mathcal P_k = j_k
```

Main consequences:

- Ch 3.3 now builds from one carrier -> continuous source fields -> source
  dictionary, with calligraphic source variables throughout.
- Pressure, stress, and radiation do not add separate M1 well weight. They
  appear only as content already carried by the relevant carriers; classical
  pressure/radiation weights are correspondence-layer subsystem apportioning.
- Ch 3.6 carries the Tolman-style reconciliation: extra classical subsystem
  weights cancel over isolated stationary systems, so totals and exterior
  fields agree while interior apportioning becomes a falsifiable divergence.
- Appendix 3.3A is now the carrier-map derivation; Appendix 3.3C is the matching
  manifestation dictionary.
- The remaining source premise is SI (source identification), not P1 uniform
  normalization. P2 remains unchanged.
- Script sweep: old source-apportioning check replaced by
  `scripts/check_carrier_source_map.py`.
