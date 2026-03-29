# Momentum First — Book Structure Plan

Status: working draft
Created: 2026-03-28
Last updated: 2026-03-29
Purpose: establish and refine the section architecture for the book after the Preface/Introduction rewrite, while keeping the front-matter contract, current M1 maturity levels, and the tier logic aligned.

## Dynamic document note

This is a **dynamic working document**, not a frozen outline.

It should be updated whenever:
- a boundary between parts becomes clearer,
- a topic is promoted, deferred, or demoted,
- a clarification from Arne resolves an open structural question,
- a technical area proves mature enough for mainline placement,
- or a section becomes too unstable and should move to appendix/supporting status.

The goal is not to pretend the whole book is already chapter-locked. The goal is to keep one honest, durable map of the current best structure.

## Operating mode

Default operating mode for this document and the surrounding section-mapping work:
- proceed on all open, non-blocked points until they are either ready for review or hit a significant blocker,
- use the clarification queue below instead of scattering unresolved questions across chats or notes,
- only pause for Arne when a decision would materially affect the backbone of the book, reopen a foundational lock, or otherwise change outcomes in a nontrivial way.

## Heartbeat follow-up action

On heartbeat or autonomous follow-up:
1. Open this file.
2. Check `## Comment & Clarification Queue` for any responses from Arne or any points that are now unblocked by chat decisions.
3. If a clarification item is unblocked, take the **smallest newly unblocked useful step** and update this document.
4. If no clarification item is unblocked, continue the **highest-value non-blocked item** from `## Current Work Queue`.
5. Stop only when the item is ready for review or a significant blocker appears.
6. If a significant blocker appears, record it explicitly in this document before stopping.

## Section-map design rules

- Foundations should carry what the reader must understand for the framework to become legible and judgeable.
- Long derivations should move to `appendices/derivations/` once they interrupt narrative flow.
- Distinguish throughout between derivation, correspondence, interpretation, and speculation.
- Keep unstable or fit-sensitive material out of the main foundational spine unless it is genuinely required for comprehension.
- Separate **dependency order** from **reading order**: some deeper-origin material may belong later in the book.
- Present geometry as a **leading carrier hypothesis**, not as the entire identity of M1.
- Treat cosmology, for now, as a **KM-B program** within the downstream engines/correspondence cluster rather than as a detached foundation chapter.

## Current structural judgment

Best current structure:
- **Part I** = orientation and framing
- **Part II** = foundations, including time, KMs, and minimal gravity grammar
- **Part III** = internal geometry / carrier hypothesis
- **Part IV** = kinematic-modification programs and correspondence tracks
- **Part V** = origins and deep grounding
- **Part VI** = predictions, tests, and failure modes
- **Part VII** = appendices and derivations

This currently looks cleaner than the earlier version because it restores three missing pillars to the foundational spine:
1. time / dilation interpretation,
2. kinematic modifier taxonomy,
3. minimal gravity grammar.

It also places cosmology where it structurally belongs right now: as the main KM-B branch within the downstream engine/correspondence architecture.

## Proposed book architecture

### Part I — Orientation

1. **Preface**
   - personal origin, motivation, collaboration posture, reading guidance
2. **Introduction**
   - success of physics, open conceptual pressure, momentum-first wager, standards of judgment

### Part II — Foundations

**Job:** state the primitive framework cleanly enough that the reader understands the basic language of M1 before entering geometry or application-specific programs.

Suggested chapter cluster:

3. **Primitive Quantities and Notation**
   - fermic momentum, bosic momentum, core momentum
   - sign locks and core symbols

4. **ADMC and the Split Conservation Principle**
   - directional split form
   - separate conservation of `p_{k^+}` and `p_{k^-}`
   - why this is the framework’s primitive move

5. **Invertible Mapping, Momentum Triangle, and SR Correspondence**
   - equivalence to conservation of total `M` and `\vec p`
   - momentum-triangle / mass-shell baseline
   - Lorentz-compatibility language

6. **Time, Clocks, and the Interpretation of Dilation**
   - cycle-based reading of time
   - time dilation as reduced cycle rate / contextualized fermic scale
   - preferred-now / true-frame stance if retained, clearly labeled by role/status

7. **Kinematic Modifiers**
   - KM-A / KM-B / KM-C taxonomy
   - what structural map each class modifies
   - why effects are read as structured kinematic change rather than generic force-language alone

8. **Minimal Gravity Grammar**
   - source -> stationary field -> observer bookkeeping pipeline
   - scalar well, shift potential, flux tensor
   - `p_{f,c}`, `\Pi`, `M_{g,loc}`, `H_{g,stat}` symbol discipline
   - scope limited to foundational grammar and stationary-regime framing

9. **Scope, Regime, and Standards of Judgment**
   - derivation vs correspondence vs interpretation vs speculation
   - regime statements, falsifiers, approximation discipline

### Part III — Internal Geometry

**Job:** introduce the first actual geometrization of the framework beyond the geometry-independent algebraic spine.

Suggested chapter cluster:

10. **Why the Framework Needs a Geometry**
    - what the algebraic backbone leaves open
    - what a geometry is supposed to explain

11. **Core Momentum Geometry**
    - geometry-independent baseline
    - candidate geometry comparison
    - why one baseline is kept and others deferred or treated as controls

12. **The Two-Cycle Carrier Hypothesis**
    - torus-like local carrier as the current leading realization
    - why it is plausible and what it buys structurally

13. **Closure, Resonance, and Internal State Structure**
    - stable vs resonant sectors
    - minimal closure logic
    - only the cleanest mainline version

14. **What the Geometry Explains — and What It Does Not**
    - explicit boundary discipline
    - local torus carrier vs broader composite/interacting structure
    - prevent overselling the current geometry program

### Part IV — Kinematic Modification Programs and Correspondence Tracks

**Job:** develop the major downstream branches of M1 as structured programs rather than as disconnected application chapters.

**Part IV discipline rule:** every chapter in this part should, as far as practical, answer the same five questions in the same order:
1. what baseline Part II / Part III structure it inherits,
2. what kinematic modification or engine move it adds,
3. what established target structure it is trying to recover or organize,
4. what is genuinely mainline-ready versus appendix-backed,
5. what remains correspondence, interpretation, or speculation.

That parallelism matters. Without it, Part IV will read like a pile of unrelated technical ambitions.

Suggested chapter cluster:

15. **Gravity as a Stationary Correspondence Program**
    - **inherits:** Part II gravity grammar and KM-A language
    - **adds:** stationary field equations, dictionary rules, transport packaging
    - **target:** GR correspondence in stationary / weak-to-moderate regime
    - **mainline keep:** field packaging logic, dictionary, transport story, regime-bounded closure claims
    - **appendix offload:** coefficient audits, long derivations, strong-field edge cases

16. **Quantum / Dirac Bridge**
    - **inherits:** Part III carrier geometry plus spin-slot scaffolding
    - **adds:** wave/operator structure and first spinorial lift
    - **target:** QM / Dirac correspondence in clearly stated regimes
    - **mainline keep:** conceptual bridge, operator meaning, limited key equations
    - **appendix offload:** long operator derivations, scan grids, sign-audit overflow

17. **QFT / EFT Construction**
    - **inherits:** stationary operator language, gravity/Dirac bridge, core conventions
    - **adds:** EFT operator basis, propagator / EOM discipline, closure tests
    - **target:** stationary EFT/QFT construction rather than grand-unified rhetoric
    - **mainline keep:** core blueprint, what is closed, what is still scaffold
    - **appendix offload:** normalization audits, coefficient residual tables, derivation sprawl

18. **Cosmology as a KM-B Program**
    - **inherits:** KM-B taxonomy from Part II
    - **adds:** `\chi(t)` / translation-yield modification and observational bridge
    - **target:** redshift and large-scale correspondence under regime-bounded cosmology semantics
    - **mainline keep:** conceptual KM-B framing, redshift mapping, observational logic, fit-discipline stance
    - **appendix offload:** ansatz menus, parameter sweeps, fit templates, alternative-history families

19. **Exclusion and State-Space Constraints**
    - **inherits:** KM-C taxonomy and internal-state language
    - **adds:** occupancy / exclusion logic as a state-space constraint rather than force-language
    - **target:** Pauli-style exclusion and many-body admissibility structure
    - **mainline keep:** conceptual exclusion mechanism and minimal admissibility rules
    - **appendix offload:** dense closure arguments, combinatorial scans, speculative generalizations

20. **Composite and Strong-Sector Structure**
    - **inherits:** Part III carrier picture and any stabilized state/connection machinery
    - **adds:** coupled composite geometry, defect/closure completion, strong-sector boundary claims
    - **target:** bounded strong/composite structure, not premature full-sector triumphalism
    - **mainline keep:** only if the local-carrier vs coupled-composite distinction is genuinely clean
    - **appendix offload:** quark-like toy closure models, baryon-specific derivations, unstable strong-sector speculation

### Part V — Origins and Deep Grounding

**Job:** place deeper-origin hypotheses where they can support the framework without masquerading as entry prerequisites.

Suggested chapter cluster:

21. **Micro-Origin Hypotheses**
22. **BFSS / String-Compatible Grounding**
23. **What Grounding Explains — and What It Does Not**

### Part VI — Predictions, Tests, and Failure Modes

**Job:** make the framework judgeable.

Suggested chapter cluster:

24. **Predictions and Benchmark Tests**
25. **Degeneracy, Non-Identifiability, and Model Risk**
26. **Failure Modes and Falsifiers**

### Part VII — Appendices and Derivations

Use for:
- long derivations,
- technical proofs/checks,
- fit templates and scan machinery,
- dense taxonomies and tables,
- alternate derivation paths worth preserving,
- unstable but useful supporting calculations.

## Topic placement table

| Topic | Belongs here | Maybe appendix / supporting | Too early to place confidently |
|---|---|---|---|
| Primitive terms (`p_f`, `p`, `M`) | Part II — Foundations |  |  |
| ADMC + invertible mappings | Part II — Foundations | derivation details in appendix |  |
| Momentum triangle / SR correspondence | Part II — Foundations | technical proofs in appendix |  |
| Time stance / dilation interpretation | Part II — Foundations | philosophy/method appendix if expanded too far |  |
| KM taxonomy (A/B/C) | Part II — Foundations |  |  |
| Minimal gravity grammar | Part II — Foundations | compact correspondence table in appendix if needed |  |
| Core momentum geometry baseline | Part III — Internal Geometry |  |  |
| Torus-like carrier hypothesis | Part III — Internal Geometry | technical derivations and scans in appendix |  |
| Internal geometry formulation | Part III mainline only in trimmed form | dense sector taxonomies and interaction-specific scaffolds in appendix/supporting notes |  |
| Internal geometry worked examples | Part III selective examples only | toy-sector scans, width numerics, closure-defect demos in appendix/supporting notes |  |
| Stationary gravity correspondence / GR dictionary | Part IV — KM / Correspondence Tracks | long coefficient audits in appendix |  |
| Dirac / QM bridge | Part IV — KM / Correspondence Tracks | long derivations in appendix |  |
| QFT / EFT framing | Part IV — KM / Correspondence Tracks | ledger/appendix support likely |  |
| Cosmology `\chi(t)` bridge | Part IV — KM / Correspondence Tracks | fit details / alternative ansatz menus in appendix or supplement |  |
| Exclusion / state-space constraints | Part IV — KM / Correspondence Tracks | appendix for closure arguments |  |
| Composite / strong-sector structure | Part IV if boundary-disciplined and mature enough | appendix/supporting notes if still too exploratory | yes |
| Fit templates / scan machinery |  | Part VII — Appendices / technical supplement |  |
| Detailed ansatz menus |  | Part VII — Appendices / technical supplement |  |
| BFSS / string / sub-particle grounding | Part V — Origins and Deep Grounding | appendix support possible |  |
| Predictions/tests | Part VI — Predictions, Tests, and Failure Modes | supporting calculations in appendix |  |

## Keep / move / defer decisions

### Keep in Part II — Foundations
- primitive vocabulary and notation locks
- ADMC statement and equivalence structure
- shortest readable path through the invertible mapping
- time / clock / dilation interpretation at framework level
- KM taxonomy
- minimal gravity grammar
- explicit scope/status discipline

### Keep in Part III — Internal Geometry
- the first explicit geometry choice
- geometry comparison and baseline-selection logic
- a trimmed mainline version of the torus/local-carrier program
- only the minimum examples needed to make the geometry legible

### Keep in Part IV — KM / Correspondence Tracks
- gravity as correspondence program
- QM / Dirac program
- QFT / EFT program
- cosmology as KM-B branch
- exclusion / many-body state-space branch
- composite/strong-sector material only if mature enough for honest mainline placement

### Move to Part VII — Appendices / supporting notes
- long field-equation derivations
- coefficient audits and closure tables
- fit templates and scan machinery
- resonance-width numerics
- dense state taxonomies introduced too quickly for main narrative
- exploratory extensions whose main role is support rather than conceptual necessity
- executable fit workflows like `INTERNAL_GEOMETRY_FIT_TEMPLATE_V1`, with only minimal main-text references where Part VI discusses benchmark logic, degeneracy, or falsifier structure
- exploratory cosmology ansatz menus like `INTERNAL_GEOMETRY_CHI_ANSATZ_MENU_V1`, with only light main-text reference where Part IV introduces the KM-B cosmology program and its regime-bounded correspondence posture

### Defer / treat as unstable
- any claim requiring a reopened foundational lock
- fit-heavy machinery whose explanatory role is not yet stable
- strong/composite chapter placement if the material remains too patch-dependent

## Comment & Clarification Queue

Use this section to capture comments, unresolved structural choices, and explicit points that need clarification from Arne.

For each item, keep the fields:
- **Why it matters**
- **Current Ada recommendation**
- **Need from Arne**
- **Arne response**
- **Status**
- **Next action when unblocked**

### CQ-01 — How explicit should the preferred-now / true-frame stance be in Part II?
- **Why it matters:** this affects tone, philosophical load, and how early the reader meets the strongest interpretive stance.
- **Current Ada recommendation:** keep it in Part II, but as a disciplined, clearly labeled interpretation tied to the time/dilation chapter rather than letting it dominate the opening backbone.
- **Need from Arne:** decide whether this should be a compact subsection or a more substantial chapter-weight treatment.
- **Arne response:** Arne's current judgment is that the M1 view on time does, in fact, force the manuscript to point toward a true frame.
- **Status:** partially resolved
- **Next action when unblocked:** revise the Part II time chapter so the true-frame stance is presented as a stronger internal consequence of the M1 time view, while still keeping the role/status labels explicit. Final manuscript weight can still be tuned later after further user feedback.

### CQ-02 — How much gravity should live in Part II versus Part IV?
- **Why it matters:** this decides whether Part II stops at gravity grammar or carries a first minimal correspondence block.
- **Current Ada recommendation:** Part II should include the pipeline, symbol grammar, and stationary-regime framing; Part IV should carry the actual correspondence program and heavier derivations.
- **Need from Arne:** decide whether a compact first stationary equation skeleton belongs in Part II or should be saved entirely for Part IV.
- **Arne response:**
- **Status:** open
- **Next action when unblocked:** refine the chapter split between “Minimal Gravity Grammar” and “Gravity as a Stationary Correspondence Program.”

### CQ-03 — What should Part III be called in the public-facing manuscript?
- **Why it matters:** naming affects whether the reader sees the torus as the whole framework or as the current leading carrier hypothesis.
- **Current Ada recommendation:** prefer `Internal Geometry` or `Carrier Geometry` over an early part title like `The Torus Model`.
- **Need from Arne:** choose whether to foreground `internal geometry`, `carrier geometry`, or `two-cycle carrier` language.
- **Arne response:**
- **Status:** open
- **Next action when unblocked:** normalize part/chapter naming across the outline.

### CQ-04 — Is the composite / strong-sector material mature enough for a mainline Part IV chapter?
- **Why it matters:** this determines whether strong-sector content appears as a full downstream chapter or remains appendix-backed / supporting.
- **Current Ada recommendation:** keep it only if it can be presented with strict boundary discipline around the “local torus carrier vs coupled composite geometry” distinction; otherwise demote it for now.
- **Need from Arne:** confirm whether he wants a bounded strong-sector chapter in the main outline now, or a placeholder/deferred note.
- **Arne response:**
- **Status:** open
- **Next action when unblocked:** either write a bounded chapter slot or move the material to deferred/supporting status.

### CQ-05 — Should cosmology in Part IV be one chapter or a two-chapter mini-cluster?
- **Why it matters:** this affects pacing in the downstream program section and how much observational-fit material sits beside conceptual exposition.
- **Current Ada recommendation:** start with one chapter slot in the structure map, but be prepared to split later into `KM-B cosmology framing` and `observational bridge / fit discipline` if the material becomes too dense.
- **Need from Arne:** decide whether the structure should already expose that split now.
- **Arne response:**
- **Status:** open
- **Next action when unblocked:** revise Part IV chapter count and placement.

## Current Work Queue

### WQ-01 — Map remaining dev artifacts into the revised structure
- **Status:** in progress
- **Current target:** continue mapping remaining dev artifacts after placing `book/dev/INTERNAL_GEOMETRY_FIT_TEMPLATE_V1.md` and `book/dev/INTERNAL_GEOMETRY_CHI_ANSATZ_MENU_V1.md`.
- **Resolved mapping 1:** `book/dev/INTERNAL_GEOMETRY_FIT_TEMPLATE_V1.md` belongs primarily in **Part VII — Appendices / technical supplement** as an executable exploratory fit scaffold, with only a short forward reference from **Part VI — Predictions, Tests, and Failure Modes** where model-risk, degeneracy, and benchmark-evaluation logic are discussed.
- **Why:** the file is explicitly an exploratory fitting template, parameter-scan workflow, and rule-penalty scaffold; it supports judgeability and comparison discipline, but it should not drive the book backbone or appear as mainline theory exposition.
- **Resolved mapping 2:** `book/dev/INTERNAL_GEOMETRY_CHI_ANSATZ_MENU_V1.md` belongs primarily in **Part VII — Appendices / technical supplement** as a correspondence-level cosmology ansatz menu, with only a light forward reference from **Part IV — Cosmology as a KM-B Program** where the manuscript explains how candidate `\chi(t)` histories are compared after the main cosmology framing is in place.
- **Why:** the file is explicitly an exploratory fitting menu and candidate-family comparison sheet, not a derivation of cosmology from first principles. It should support the cosmology chapter's regime-bounded correspondence discipline without becoming the chapter's conceptual center of gravity.
- **Resolved mapping 3:** `book/dev/CORE_MOMENTUM_GEOMETRY_PRELIM_V1.md` belongs primarily in **Part III — Internal Geometry**, especially the transition from `Why the Framework Needs a Geometry` into `Core Momentum Geometry`, with selected baseline comparison material supporting the opening geometry-choice argument.
- **Why:** the file cleanly separates a geometry-independent ADMC/SR bridge from a three-way candidate-geometry comparison, then makes a preliminary keep/reject/control decision (`G3` exploratory baseline, `G2` rejected for baseline, `G1` retained as control). That is exactly the kind of material Part III should use to motivate why geometry enters after Foundations without pretending the choice is already final ontology. Its later state-classification and transition-rule sections are too exploratory and dense for mainline placement, so they should remain appendix-backed or supporting notes unless later maturity justifies promotion.
- **Resolved mapping 4:** `book/dev/INTERNAL_GEOMETRY_FORMULATION_V1.md` belongs primarily in **Part III — Internal Geometry** as the main supporting source behind `The Two-Cycle Carrier Hypothesis`, `Closure, Resonance, and Internal State Structure`, and `What the Geometry Explains — and What It Does Not`, with only carefully trimmed conceptual material promoted into the main text.
- **Why:** the file is the first coherent synthesis of the torus/two-cycle carrier program: carrier geometry, closure logic, state taxonomy, spin-slot scaffolding, resonant-state interpretation, and first particle-class mapping. That makes it too central to ignore when shaping Part III, but also too dense and maturity-sensitive to transplant wholesale into the manuscript. The keepable mainline core is the carrier hypothesis, the closure/stability logic, the existence of a spinorial consistency slot, and the stable-vs-resonant distinction. The heavier state taxonomy, detailed particle-class mapping, connection-sector machinery, and defect/composite scaffolding should remain appendix-backed or later-engine support until the maturity of those claims is stronger.
- **Resolved mapping 5:** `book/dev/INTERNAL_GEOMETRY_WORKED_EXAMPLES_V1.md` belongs primarily in **Part VII — Appendices / technical supplement** as worked-example support for the Part III internal-geometry program, with only selective narrative references in **Part III — Internal Geometry** where the manuscript wants one compact example of allowed/forbidden transitions or stable-vs-resonant ordering.
- **Why:** the file is explicitly a worked-examples companion to `INTERNAL_GEOMETRY_FORMULATION_V1.md`. Its value is not in setting the conceptual architecture, but in giving concrete toy-sector checks: parity classes, allowed/forbidden transitions, closure-defect bookkeeping, and resonance-width ordering. That makes it useful for auditability and for future appendix material, but too example-heavy and toy-model-specific to sit in the mainline geometry chapters unless sharply trimmed. Mainline prose should take only the smallest illustrative example it genuinely needs; the bulk belongs in appendix-backed support.
- **Next target:** continue the chapter-to-source map with the next unmapped dev artifact, or consolidate the accumulated mappings into a clearer chapter-to-source table if that becomes the higher-value non-blocked step.

### WQ-02 — Tighten chapter-level descriptions for Part II
- **Status:** completed (2026-03-29)
- **Result:** Part II now exists as a drafted seven-subsection spine covering primitives, ADMC, invertible mapping / momentum triangle / SR correspondence, time/dilation interpretation, KM taxonomy, minimal gravity grammar, and scope/status discipline.
- **Refinement pass:** terminology is now tightened so `fermic` / `bosic` apply to momentum language while `fermionic` / `bosonic` apply to structure/geometry language; `M` is now described as representative of total momentum content; ADMC is stated as direction-general rather than axis-restricted; and rebuildable manuscript figures are now wired into the repo for Foundations.
- **Follow-up:** future edits should be refinement-level unless a foundational lock is intentionally reopened.

### WQ-03 — Tighten chapter-level descriptions for Part IV
- **Status:** open
- **Focus:** keep gravity, QM/QFT, cosmology, and KM-C/composite chapters structurally parallel where possible.

### WQ-04 — Build a chapter-to-source map
- **Status:** in progress
- **Focus:** connect major existing dev files to likely part/chapter destinations so future drafting does not drift.
- **Current output:** start consolidating resolved placements into a living table instead of leaving them only as prose bullets.

#### Chapter-to-source map (living table)

| Source artifact | Primary destination | Mainline use | Appendix / support use | Notes |
|---|---|---|---|---|
| `CORE_MOMENTUM_GEOMETRY_PRELIM_V1.md` | Part III — `Why the Framework Needs a Geometry` / `Core Momentum Geometry` | geometry-entry argument, candidate comparison, keep/reject/control logic | dense classification and transition scaffolding | geometry enters after Foundations, not before |
| `INTERNAL_GEOMETRY_FORMULATION_V1.md` | Part III — `The Two-Cycle Carrier Hypothesis` / `Closure, Resonance, and Internal State Structure` / `What the Geometry Explains — and What It Does Not` | carrier hypothesis, closure logic, spin-slot scaffolding, stable-vs-resonant distinction | state taxonomy, particle-class mapping, connection/defect machinery | central support source for Part III, but too dense to import wholesale |
| `INTERNAL_GEOMETRY_WORKED_EXAMPLES_V1.md` | Part VII primarily; selective Part III support | at most one compact illustrative example if it truly helps readability | toy-sector transition checks, parity classes, closure-defect demos, width ordering | example-heavy companion, not conceptual backbone |
| `INTERNAL_GEOMETRY_FIT_TEMPLATE_V1.md` | Part VII; light Part VI reference | benchmark / degeneracy forward reference only | executable fit scaffold, scan workflow, rule penalties | judgeability support, not mainline theory |
| `INTERNAL_GEOMETRY_CHI_ANSATZ_MENU_V1.md` | Part VII; light Part IV cosmology reference | mention candidate-history comparison discipline only | ansatz families, parameter menus, exploratory cosmology fitting | correspondence support, not derivation |
| `INTERNAL_GEOMETRY_WAVE_EQUATION_FORMULATION_V1.md` | Part IV — `Quantum / Dirac Bridge`; appendix-backed support from Part III geometry | baseline torus-wave equation, winding embedding choice, conserved functional, cautious correspondence slots | calibration ansätze, shell tables, extension menu, long derivation scaffold | strongest current bridge from carrier geometry into QM/Dirac-style program, but not ready to carry full mainline claims alone |
| `QFT_FOUNDATION_CORE_BLUEPRINT_V1.md` | Part IV — `QFT / EFT Construction` | chapter backbone for closure discipline: conventions, action/EOM/propagator chain, overlap regime, claim-gating | execution queue details, audit workflow, residual-management logistics | strongest current structuring source for the QFT chapter; useful because it organizes what counts as foundation versus premature phenomenology |
| `QFT_CORE_CONVENTIONS_LOCK_V1.md` | Part IV — `QFT / EFT Construction`; local support for Part II/IV notation discipline | fixed convention block, symbol semantics, KM typing lock, propagator normalization baseline | detailed convention registry and canonical reference appendix material | especially useful for preventing sign/normalization drift and keeping `M_{g,loc}` vs `H_{g,stat}` semantics stable across chapters |
| `QFT_STATIONARY_EFT_DERIVATION_CORE_V1.md` | Part IV — `QFT / EFT Construction` | minimal stationary EFT core action, KM-A operator basis, exact-vs-closure ledger, D1 derivation spine | hand-off queue, detailed operator expansion, derivation scaffolding for D2 | best current derivation-level source for the opening mainline QFT chapter, but should stay regime-bounded and avoid pretending full covariant closure |

### WQ-05 — Identify what is ready for review versus what remains unstable
- **Status:** open
- **Focus:** keep the mainline outline honest and prevent premature locking.

## Ready for review

- Part I / Part II / Part III / Part IV / Part V / Part VI / Part VII architecture at the level of major part boundaries.
- Core judgment that Foundations must include time, KM taxonomy, and minimal gravity grammar.
- Core judgment that cosmology currently belongs inside the Part IV downstream program cluster.
- Drafted Part II manuscript text in `chapters/02-foundations/`, rendered successfully to HTML.
- Foundations terminology pass completed: `fermic` / `bosic` are now momentum adjectives, `fermionic` / `bosonic` are structure/geometry adjectives.
- Foundations figure pass completed with rebuildable figure scripts and outputs for shell language, momentum triangle, and source -> field -> observer grammar.

## Significant blockers

_None currently._

Add blockers here only when they materially prevent the next structural step.

## Next smallest win

Map the remaining dev artifacts into the revised Part II / Part III / Part IV / Part VII structure, starting with `book/dev/INTERNAL_GEOMETRY_FIT_TEMPLATE_V1.md`.
