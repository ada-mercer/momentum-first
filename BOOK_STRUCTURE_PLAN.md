# Momentum First — Book Structure Plan

Status: working draft
Created: 2026-03-28
Last updated: 2026-05-11
Purpose: establish and refine the book architecture while keeping the rendered Quarto hierarchy, M1 maturity levels, and tier logic aligned.

## Dynamic document note

This is a **dynamic working document**, not a frozen outline.

It should be updated whenever:
- a boundary between parts becomes clearer,
- a topic is promoted, deferred, or demoted,
- a clarification from Arne resolves an open structural question,
- a technical area proves mature enough for mainline placement,
- or a section becomes too unstable and should move to appendix/supporting status.

The goal is not to pretend the whole book is already chapter-locked. The goal is to keep one honest, durable map of the current best structure.

## Stability rule

This plan should be **slow to change**.

Use it as a stabilizing element:
- change wording lightly and structure conservatively,
- prefer harmonizing the plan with already-earned internal notes over rewriting the backbone impulsively,
- only change part boundaries, chapter roles, or mainline/promoted status when a real structural gain has been established,
- let exploratory note churn happen in `book/dev/` rather than in this file.

## Operating mode

Default operating mode for this document and the surrounding structure-mapping work:
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
- Present geometry as a **candidate carrier / grounding question**, not as the entire identity of M1.
- Treat imported frameworks such as BFSS and string theory as filtered candidate-support structures. They may supply useful mathematics, but they do not redefine M1 primitives.
- Keep the Quarto distinction clear: rendered **parts** are tier-level reader divisions; rendered chapter files may themselves include smaller section files.

## Current structural judgment

Best current rendered/planned structure:

- **Front matter** = landing page plus Preface material: origin, posture, collaboration, reading guidance, and working method.
- **Tier 1 — Foundations** = rendered chapters `Introduction` and `Foundations`.
- **Tier 2 — Engines** = achieved or near-achieved M1 effective engines. Currently rendered chapters: `Gravity and Structured Spacetime` and `Quantum Mechanics in Momentum Language`. Next likely engine: `Cosmology in Momentum Language`. QFT/EFT remains a candidate Tier 2 engine if it can be kept as a bounded stationary/effective foundation rather than a broad completion claim.
- **Tier 3 — Tests, Predictions, and Failure Modes** = empirical/risk close. Near-term candidate: neutron-star shallow-heating / strong-gravity quantum-sensitivity test channel.
- **Tier 0 — Deep Structure and Sub-Particle Models** = provisional downstream-in-reading-order treatment of underlying space/sub-particle carrier models: BFSS/string-compatible structures, torus/two-cycle models, closure/resonance, and internal geometry under M1 constraints.
- **Appendices and Derivations** = derivation trust layer and technical support.

Why this is stronger than the preliminary Tier 2A/Tier 2B arrangement:

1. Tier 2 is no longer split into a mature-engine half and a speculative-deep-structure half.
2. Gravity and QM remain the first achieved engines; cosmology and possibly bounded QFT/EFT can join them as engines when mature.
3. Predictions/tests remain downstream of the engines, where claims can be made judgeable without importing new ontology.
4. Deep structure is restored to its natural status as **Tier 0**: ontologically deeper, but later in the reader's path because Tier 2 engines should constrain what the sub-particle/space-structure model must explain.
5. BFSS/string/torus/internal geometry remain available, but as filtered candidate support structures rather than primitive ontology.

The main structural wager is now:

- establish M1 language and locks in Tier 1,
- develop effective engines in Tier 2,
- expose predictions, tests, degeneracies, and falsifiers in Tier 3,
- then treat Tier 0 / Deep Structure as a provisional sub-particle and underlying-space model constrained by the earlier tiers.

## Proposed book architecture

This section should track the rendered `_quarto.yml` structure where that structure already exists. Later parts remain planning-level until their files are created.

### Front matter and Preface

Rendered files:
- `index.qmd`
- `chapters/00-front-matter/00-preface/index.qmd`

**Job:** orient the reader before the formal argument starts.

The Preface owns:
- the persistent tension that motivates the book;
- what kind of book this is;
- authorship and collaboration posture;
- how to read the book;
- working method.

The Preface should stay personal and methodological. It should not carry the technical burden of the Introduction, Foundations, or later engine chapters.

### Tier 1 — Foundations

Rendered files:
1. `chapters/01-tier-1-foundations/01-introduction/index.qmd` — **Introduction**
2. `chapters/01-tier-1-foundations/02-foundations/index.qmd` — **Foundations**

**Job:** make M1 legible and judgeable before engines begin.

#### Chapter 1 — Introduction

The Introduction owns:
- respect for the success of existing physics;
- open questions and conceptual pressure points;
- the momentum-first wager;
- what the book is trying to do;
- how the book asks to be judged.

It should be conceptually sharp but nontechnical: a legitimization-and-standards chapter, not a derivation chapter and not a manifesto.

#### Chapter 2 — Foundations

Foundations owns:
- primitive terms and notation: fermic momentum, bosic momentum, core momentum, sign locks, and core symbols;
- ADMC as the directional-positive conservation postulate and its realized split;
- the invertible mapping, momentum triangle, conservation equivalence, and SR correspondence;
- the stage/actor distinction between space and momentum;
- time, clocks, dilation, contraction, and the true-frame stance at the currently justified interpretive level;
- kinematic modifiers as the grammar for structured departures from the inertial baseline;
- a clean close stating what Foundations has and has not established.

Foundations should not develop the gravity program. Gravity belongs to Tier 2. Foundations may only hand off to gravity as the first major downstream case where the relational/spatial stage is altered and local kinematics must be read in context.

### Tier 2 — Engines

Rendered files:
1. `chapters/02-tier-2-engines/03-gravity-and-structured-spacetime/index.qmd` — **Gravity and Structured Spacetime**
2. `chapters/02-tier-2-engines/04-quantum-mechanics/index.qmd` — **Quantum Mechanics in Momentum Language**

Planned later candidates:
3. **Cosmology in Momentum Language** — next likely Tier 2 chapter.
4. **QFT / EFT Foundations** — only if mature enough as a bounded stationary/effective engine.

**Job:** develop M1's achieved or near-achieved effective engines in reader-facing form.

**Tier 2 discipline rule:** Tier 2 is for engines that can be explained primarily in M1-native variables and checked against standard regimes. It is not the home for full deep-origin speculation.

#### Chapter 3 — Gravity and Structured Spacetime

**Job:** make gravity the first major developed engine of the book, and use it to introduce structured spacetime in a disciplined, minimally overcommitted way.

Current rendered chapter arc:
1. philosophical approach: gravity as momentum content changing relational/spatial conditions;
2. gravity-side core terms and variables;
3. source construction;
4. stationary field construction;
5. local observer bookkeeping;
6. stationary classical correspondence;
7. bounded nonstationary extension track;
8. spacetime lessons and open boundaries.

Gravity should carry real explanatory weight here, not appear as one downstream application among many. Geometry enters in this chapter only insofar as gravity forces the question of what sort of spatial structure is needed.

#### Chapter 4 — Quantum Mechanics in Momentum Language

**Job:** build the M1 quantum bridge as a clean operator/correspondence chapter.

Current rendered chapter arc:
1. quantum mechanics after gravity;
2. quantum-side core terms and variables;
3. the core momentum operator `\hat M`;
4. stationary gravity and the operator `\hat M_g`;
5. correspondence with standard quantum mechanics;
6. the nonrelativistic limit;
7. classical and stationary-gravity limits;
8. strong gravity and quantum sensitivity;
9. what the quantum chapter establishes.

This chapter has now taken over the mature `QM / Dirac bridge` burden from the old planned quantum-geometry part. Presence-vs-expression remains a light supporting stance around `\Psi`, phase, and expression/detection. Torus/internal geometry, EM projectors, full QFT, measurement theory, and compact-object phenomenology remain outside this chapter unless later maturity demands a carefully bounded cross-reference.

#### Planned Tier 2 chapter — Cosmology in Momentum Language

**Job:** treat cosmology as a separate M1 engine, not as gravity scaled up and not merely as a fit exercise.

Likely chapter burden:
- why cosmology is a KM-B / translation-yield engine rather than a local gravity chapter;
- `\chi(t)` as the bosic displacement-yield modifier;
- redshift mapping `1+z = \chi_{emit}/\chi_{obs}` in its proper regime;
- how the cosmology engine preserves the M1 variables `p`, `p_k`, and `M` without global fermic rescaling;
- a bounded handoff to Tier 3 for observational fits, degeneracy, and falsifiers.

Current recommendation: make cosmology the next Tier 2 authoring target after the current plan sync. Keep ansatz menus and fit machinery out of the main engine exposition except as brief signposts.

#### Planned Tier 2 candidate — QFT / EFT Foundations

**Job:** decide whether QFT/EFT is ready to be a bounded effective engine chapter.

Current recommendation:
- Tier 2 if the chapter is a narrow stationary/effective foundation: convention lock, minimal action, EOM/propagator route, overlap-regime checks, and claim discipline;
- Tier 0 / supporting notes if the material shifts into composite/internal-geometry/state-space speculation;
- Tier 3 if the material is mainly an empirical overlap, residual, or benchmark program.


### Tier 3 — Tests, Predictions, and Failure Modes

**Status:** planned major part.

**Job:** make the framework judgeable.

Suggested chapter cluster:
1. **Prediction Channels and Benchmarks**
2. **Neutron-Star Shallow Heating and Strong-Gravity Quantum Sensitivity** — near-term candidate next chapter.
3. **Cosmology Fits, Degeneracy, and Redshift Alternatives**
4. **QFT/EFT Overlap and Residual Tests**
5. **Internal-Geometry / Particle-Sector Test Channels**
6. **Failure Modes and Falsifiers**

**Tier 3 discipline rule:** this part should not introduce deep-structure ontology. It tests consequences, exposes degeneracy, and names failure channels.

#### Planned Tier 3 chapter — Neutron-Star Shallow Heating and Strong-Gravity Quantum Sensitivity

**Job:** turn the Chapter 04 strong-gravity quantum-sensitivity result into a focused empirical/risk channel.

Likely chapter burden:
- state the observed shallow-heating problem without overclaiming a solved phenomenology;
- connect the M1 mechanism to `p_f -> p_{f,c}` in strong scalar wells;
- explain how modified under-barrier momentum balance can affect tunneling/reaction rates and crustal heating channels;
- identify what would be compared against standard crust models;
- state degeneracies, failure modes, and what would falsify the M1 reading.

Boundary: this belongs in Tier 3 because it is a test/prediction channel, not a new engine and not a deep-structure ontology claim.

### Tier 0 — Deep Structure and Sub-Particle Models

**Status:** provisional later part; not yet detailed chapter-by-chapter.

Recommended public title: **Tier 0 — Deep Structure and Sub-Particle Models**.

**Job:** study candidate underlying space/sub-particle structures under M1 constraints after the Tier 2 engines and Tier 3 test targets have clarified what the deeper model must explain.

**Reading-order note:** Tier 0 is ontologically deeper but should appear later in the book. The reader first needs the M1 primitives, the effective engines, and the test channels before the book asks what underlying carrier or sub-particle model could support them.

**Tier 0 discipline rule:** M1 remains primary. BFSS, string theory, torus geometry, closure/resonance models, and internal geometry are tested as candidate support structures. They do not redefine `p_f`, `p`, `M`, ADMC, or the source -> field -> observer grammar.

Provisional chapter cluster, intentionally light for now:

1. **What a Deeper Model Must Explain**
   - collected constraints inherited from Tier 1, Tier 2, and Tier 3;
   - why deep structure is constrained by the engines rather than allowed to rewrite them.

2. **M1 Constraints on Admissible Underlying Structure**
   - ADMC split intact;
   - invertible `(M,p_k) <-> (p_{k+},p_{k-})` map;
   - positive directional conservation legible;
   - `M^2=p_f^2+p^2` readable in baseline regime;
   - source -> field -> observer pipeline compatible;
   - imported ontology cannot redefine M1 primitives.

3. **Candidate Carrier / Space-Structure Models**
   - torus/two-cycle as bounded candidate carrier and visualization;
   - fiber/bundle-style internal structure if useful;
   - closure, winding, resonance/admissibility;
   - what such models help explain and why they are not yet core ontology.

4. **BFSS/String-Compatible Structures Under M1 Translation**
   - left/right split analogy versus M1 directional split;
   - winding/mode/level-matching analogies;
   - holonomy/phase structures;
   - BFSS as candidate generator and pruning target, not primitive ontology.

5. **Open Boundaries and Deferred Composite Sectors**
   - internal geometry and composite/particle-sector programs that are not yet engine-ready;
   - strict maturity labels and dev-only boundaries for fit-heavy material.

Recommended support notes:
- `book/dev/M1_GEOMETRY_CONSTRAINTS_ON_BFSS_SOLUTION_SPACE_V1.md`
- `book/dev/BFSS_TO_M1_EXTRACTION_TEMPLATE_V1.md`
- `book/dev/M1_AS_A_PRUNING_AND_EFFECTIVE_VARIABLE_DISCIPLINE_FOR_BFSS_V1.md`
- `book/dev/INTERNAL_GEOMETRY_BFSS_STRING_MATH_BRIDGE_V1.md`
- `book/dev/CORE_MOMENTUM_GEOMETRY_PRELIM_V1.md`
- `book/dev/INTERNAL_GEOMETRY_CONSOLIDATED_REVIEW_V2.md`
- torus wave/scan notes only as supporting/dev evidence unless a later pass promotes them.

### Appendices and derivations

Rendered now:
- stationary gravity derivation appendices;
- nonstationary gravity extension appendices;
- references.

**Job:** derivation trust layer and technical support.

Use for:
- long derivations;
- technical proofs/checks;
- coefficient audits;
- operator derivations;
- BFSS/string extraction worksheets once mature;
- torus scan machinery once mature;
- fit templates and scan machinery;
- dense taxonomies and tables;
- alternate derivation paths worth preserving.

Immature material should remain in `book/dev/`, not appendices, until stable enough to support the reader-facing argument.

## Topic placement table

| Topic | Updated placement | Note |
|---|---|---|
| Introduction / standards | Tier 1 chapter | Former old rendered division I is now a chapter. |
| Foundations / ADMC / SR map | Tier 1 chapter | Former old rendered division II is now a chapter. |
| Primitive terms (`p_f`, `p`, `M`) | Tier 1 — Foundations | Technical proofs in appendices if needed. |
| Time stance / dilation interpretation | Tier 1 — Foundations | Keep role/status labels explicit. |
| KM taxonomy | Tier 1 — Foundations | Grammar for later engines. |
| Gravity | Tier 2 chapter | Rendered and structurally achieved. |
| Stationary gravity correspondence / GR dictionary | Tier 2 — Gravity | Long audits in appendices. |
| QM / Dirac / `\hat M` / `\hat M_g` | Tier 2 chapter | Rendered Chapter 04; no longer future geometry material. |
| Presence vs expression | Light support in QM; fuller treatment only if needed in Tier 0 | Not load-bearing ontology. |
| Strong-gravity quantum sensitivity | Tier 2 QM result; Tier 3 tests | Keep claims bounded: `p_f -> p_{f,c}` can affect phase/envelope/tunneling. |
| Neutron-star shallow heating | Tier 3 test chapter candidate | Near-term prediction/application channel; not an engine chapter. |
| Cosmology `\chi(t)` | Tier 2 engine; Tier 3 for fit/degen tests | Next likely Tier 2 chapter. |
| QFT/EFT | Tier 2 if bounded stationary/effective engine; Tier 3 for overlap tests | Composite/internal-geometry-heavy material stays Tier 0/support. |
| Torus / two-cycle model | Tier 0 candidate carrier | Bounded carrier/visualization, not primitive backbone. |
| Closure / resonance / admissibility | Tier 0 / support | Helps constrain sub-particle/internal state models. |
| BFSS / string-compatible grounding | Tier 0 | M1 filters BFSS/string; not the reverse. |
| Internal geometry / composite sectors | Tier 0, with dev-only guardrails | Promote only when maturity supports it. |
| Fit scans / dense tables | Appendices or `book/dev/` | Not mainline unless stable. |
| Predictions/tests/falsifiers | Tier 3 | Empirical/risk close. |

## Keep / move / defer decisions

### Keep in Tier 1 — Foundations
- primitive vocabulary and notation locks;
- ADMC statement and equivalence structure;
- shortest readable path through the invertible mapping;
- the space-as-stage / momentum-as-actor distinction;
- time / clock / dilation interpretation at framework level;
- KM taxonomy;
- explicit scope/status discipline;
- at most a very small bridge sentence or transition into gravity.

### Keep in Tier 2 — Engines
- Gravity as the first full engine treatment;
- stationary-first gravity scope and regime framing;
- source -> stationary field -> observer pipeline;
- stationary correspondence and bounded nonstationary extension;
- QM as the core operator/correspondence chapter;
- `\hat M`, `\hat M_g`, standard QM/Dirac correspondence, nonrelativistic and classical/stationary limits;
- strong-gravity quantum sensitivity as a bounded structural result;
- cosmology as a separate KM-B / `\chi(t)` engine if the chapter stays engine-first rather than fit-first;
- QFT/EFT only if it can be written as a bounded stationary/effective engine.

### Keep in Tier 3 — Tests, Predictions, and Failure Modes
- prediction channels and benchmark tests;
- neutron-star shallow heating / strong-gravity quantum-sensitivity tests;
- cosmology degeneracy and fit-risk analysis;
- QFT/EFT overlap and residual tests;
- internal-geometry / particle-sector test channels;
- failure modes and falsifiers.

### Keep in Tier 0 — Deep Structure and Sub-Particle Models
- M1 constraints on admissible underlying structure;
- BFSS/string structures as filtered support, not primitives;
- torus/two-cycle models as candidate carriers / bounded visualization;
- closure, resonance, admissibility, and mismatch costs;
- internal geometry and composite-sector programs under maturity labels;
- dev-source mapping for candidate support notes.

### Move to Appendices / supporting notes once mature
- long field-equation derivations;
- coefficient audits and closure tables;
- operator derivations too detailed for the mainline;
- BFSS/string extraction worksheets;
- torus scan machinery;
- fit templates and scan machinery;
- dense state taxonomies and alternate derivation paths.

### Keep in `book/dev/` for now
- immature torus/two-cycle ontology claims;
- speculative state taxonomies, particle mappings, or closure classes not yet needed by the manuscript backbone;
- exploratory scans, ansatz menus, and patch-sensitive geometry extensions;
- exploratory cosmology ansatz menus until they become stable enough to support a reader-facing chapter;
- strong/composite sketches that are not yet boundary-disciplined;
- BFSS/string candidate structures that have not yet been filtered through an explicit M1 constraint sheet.

## Comment & Clarification Queue

Use this section to capture comments, unresolved structural choices, and explicit points that need clarification from Arne.

### CQ-01 — How explicit should the preferred-now / true-frame stance be in Tier 1?
- **Why it matters:** this affects tone, philosophical load, and how early the reader meets the strongest interpretive stance.
- **Current Ada recommendation:** keep it in Foundations as a disciplined, clearly labeled interpretation tied to the time/dilation chapter rather than letting it dominate the opening backbone.
- **Arne response:** Arne's current judgment is that the M1 view on time does, in fact, force the manuscript to point toward a true frame.
- **Status:** partially resolved.
- **Next action:** tune the Foundations time section only if later prose review shows the stance is either too timid or too dominant.

### CQ-02 — How much gravity should live in Foundations versus Tier 2?
- **Why it matters:** this decides whether Foundations stops at framework language or carries too much engine content before the dedicated gravity chapter begins.
- **Current Ada recommendation:** Foundations should keep only the smallest bridge material needed for readability; Gravity should carry the actual grammar, source construction, field construction, observer bookkeeping, and structured-spacetime discussion.
- **Arne response:** gravity should be promoted to its own developed engine treatment.
- **Status:** resolved enough for current structure.
- **Next action:** keep auditing Foundations for gravity machinery that belongs in Chapter 3.

### CQ-03 — How should Tier 0 / Deep Structure be titled?
- **Why it matters:** naming determines whether the part is read as a speculative appendix, imported-framework program, or M1-owned sub-particle/space-structure target.
- **Current Ada recommendation:** use `Tier 0 — Deep Structure and Sub-Particle Models` as the working title; avoid naming the part after BFSS/string/torus.
- **Arne response:** adopt Tier 0 / sub-particle / underlying-space framing and keep the detailed structure provisional.
- **Status:** resolved enough for current structure.
- **Next action:** do not detail Tier 0 heavily until Tier 2 and Tier 3 shape has constrained it further.

### CQ-04 — How much torus/two-cycle material belongs in Tier 0 mainline?
- **Why it matters:** the torus model is useful, but can easily overclaim as ontology.
- **Current Ada recommendation:** yes, keep one bounded candidate-model treatment in Tier 0, with explicit non-ontology guardrails. Keep fit-heavy and speculative extensions in `book/dev/` unless matured.
- **Arne response:** keep the torus only as a bounded symbolic / visualization layer for something real but simplified, not as the framework's core explanatory backbone.
- **Status:** resolved enough for current structure.
- **Next action:** when drafting Tier 0, separate mainline candidate-carrier explanation from dev-only scans and speculative particle mappings.

### CQ-05 — Where should cosmology land under the tier-as-part architecture?
- **Why it matters:** cosmology can be an engine, a fit/testing program, or both.
- **Current Ada recommendation:** keep cosmology as a Tier 2 engine if `\chi(t)` can be presented cleanly; put fit/degen/test material in Tier 3.
- **Arne response:** cosmology should have its own visible treatment; it is a separate engine.
- **Status:** partially resolved.
- **Next action:** perform a cosmology maturity review before creating its chapter files.

### CQ-06 — Should QFT/EFT be Tier 2, Tier 3, or Tier 0/support?
- **Why it matters:** QFT/EFT could be a bounded effective engine, an overlap-test program, or a generalized state-space/internal-geometry extension.
- **Current Ada recommendation:** Tier 2 only if the material can be written as a bounded stationary/effective engine; Tier 3 if it is mainly overlap/residual testing; Tier 0/support if it depends on composite/internal-geometry speculation.
- **Status:** open.
- **Next action:** review QFT/EFT dev notes after the current plan sync.

### CQ-07 — Is composite / strong-sector material mature enough for mainline Tier 0?
- **Why it matters:** this determines whether strong-sector content appears as a visible chapter or remains dev-only/supporting.
- **Current Ada recommendation:** keep a placeholder in Tier 0 open boundaries, not a full mainline claim, unless the material can be presented with strict boundary discipline.
- **Status:** open.
- **Next action:** classify composite/strong-sector notes during the next source-map pass.

## Current Work Queue

### WQ-01 — Synchronize the plan after tier-as-part restructure
- **Status:** updated 2026-05-11.
- **Result:** `BOOK_STRUCTURE_PLAN.md` now reflects Tier 1 Foundations, Tier 2 Engines, Tier 3 Tests/Predictions/Failure Modes, and later-reading-order Tier 0 Deep Structure / Sub-Particle Models. The previous Tier 2A/Tier 2B split has been removed.
- **Next action:** wait to update `_quarto.yml` with future placeholder parts until actual chapter files are created.

### WQ-02 — Detail the Cosmology Tier 2 chapter
- **Status:** next likely planning target.
- **Question:** how much of `\chi(t)` is engine exposition versus Tier 3 fit/test material?
- **Next action:** inspect cosmology source notes and propose a chapter burden / section map.

### WQ-03 — Detail the neutron-star shallow-heating Tier 3 chapter
- **Status:** next likely planning target.
- **Question:** how should the strong-gravity quantum-sensitivity result become a bounded neutron-star shallow-heating test chapter?
- **Next action:** inspect relevant shallow-heating / strong-gravity notes and propose a chapter burden / section map.

### WQ-04 — Rebuild the chapter-to-source map under the new tiers
- **Status:** open.
- **Reason:** the old source map used obsolete old rendered-part labels and the preliminary Tier 2A/Tier 2B split is now retired. A backup of the pre-update plan was saved at `book/dev/BOOK_STRUCTURE_PLAN_PRE_TIER_PARTS_BACKUP_2026-05-10.md` so useful mappings can be migrated without keeping stale architecture in the live plan.
- **Next action:** migrate only stable mappings into a new tier-based source map, starting with Cosmology / NS shallow heating, then later Tier 0 support notes.

### WQ-05 — Identify what is ready for review versus what remains unstable
- **Status:** open.
- **Focus:** keep the mainline outline honest and prevent premature locking.

## Ready for review

- Tier-as-part architecture at the level of major part boundaries.
- Tier 1 containing Introduction and Foundations as rendered chapters.
- Tier 2 containing Gravity and Quantum Mechanics as rendered chapters, with Cosmology as the next likely engine target.
- Tier 3 containing predictions/tests/failure modes, with neutron-star shallow heating as the next likely test-channel target.
- Core judgment that the old broad `Quantum Structure and the Geometry of Expression` plan is obsolete because Chapter 04 now handles the mature QM/operator bridge.
- Core judgment that BFSS/string/torus/internal-geometry material belongs in Tier 0 / Deep Structure and Sub-Particle Models, not in a Tier 2B engine-adjacent part.
- Core judgment that immature fit-heavy or ontology-heavy material remains in `book/dev/` until mature enough for appendices or mainline reference.

## Significant blockers

_None currently._

Add blockers here only when they materially prevent the next structural step.

## Next smallest win

Build short planning briefs for the two likely next authoring targets: Tier 3 neutron-star shallow heating and Tier 2 cosmology.
