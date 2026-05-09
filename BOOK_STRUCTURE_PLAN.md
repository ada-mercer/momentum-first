# Momentum First — Book Structure Plan

Status: working draft
Created: 2026-03-28
Last updated: 2026-05-01
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

## Stability rule

This plan should be **slow to change**.

Use it as a stabilizing element:
- change wording lightly and structure conservatively,
- prefer harmonizing the plan with already-earned internal notes over rewriting the backbone impulsively,
- only change part boundaries, chapter roles, or mainline/promoted status when a real structural gain has been established,
- let exploratory note churn happen in `book/dev/` rather than in this file.

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

Best current rendered/planned structure:
- **Front matter** = landing page plus Preface material: origin, posture, collaboration, reading guidance, and working method
- **Part I — Introduction** = success of physics, conceptual pressure, the momentum-first wager, and the book's standards of judgment
- **Part II — Foundations** = primitive terms, ADMC, invertible mapping/SR correspondence, stage/actor distinction, time, kinematic modifiers, and the handoff to gravity
- **Part III — Gravity and Structured Spacetime** = first major developed engine; physical-first gravity philosophy, concept/symbol gateway, sources, stationary field, local readout, stationary correspondence, nonstationary extension, and open boundaries
- **Part IV — Quantum Structure and the Geometry of Expression** = planned downstream state/expression structure
- **Part V — Cosmology** = planned separate engine
- **Part VI — Generalized State-Space and Composite Programs** = planned broader generalizations
- **Part VII — Deep Structure and Filtered Grounding** = planned late-stage grounding material
- **Part VIII — Predictions, Tests, and Failure Modes** = planned empirical/risk close
- **Part IX — Appendices and Derivations** = derivation trust layer

Why this is currently stronger than the previous arrangement:
1. gravity gets promoted to the first major developed engine,
2. KM remains foundational but does not overtake the part architecture,
3. cosmology gets its own part rather than being buried inside a broad omnibus section,
4. quantum/state-structure material gets a more natural home than a standalone geometry-meta part,
5. deep grounding (including BFSS/string filtering) stays late, where its current maturity level belongs.

The main structural wager is now:
- foundations first,
- gravity first among engines,
- quantum/state-structure next,
- cosmology as a separate engine,
- broader generalizations later,
- deep grounding late and filtered,
- predictions/tests at the end.

## Proposed book architecture

This section should track the rendered `_quarto.yml` structure where that structure already exists. Later parts remain planning-level until their files are created.

### Front matter and Preface

Rendered files:
- `index.qmd`
- `chapters/00-preface/index.qmd`

**Job:** orient the reader before the formal argument starts.

The Preface owns:
- the persistent tension that motivates the book;
- what kind of book this is;
- authorship and collaboration posture;
- how to read the book;
- working method.

The Preface should stay personal and methodological. It should not carry the technical burden of the Introduction or Foundations.

### Part I — Introduction

Rendered files:
1. `chapters/01-introduction/01-01-the-success-of-physics.qmd`
2. `chapters/01-introduction/01-02-open-questions-and-conceptual-pressure.qmd`
3. `chapters/01-introduction/01-03-the-momentum-first-wager.qmd`
4. `chapters/01-introduction/01-04-what-this-book-is-trying-to-do.qmd`

**Job:** frame the conceptual pressure and the wager without pretending the case is already won.

The Introduction owns:
- respect for the success of existing physics;
- the open questions and conceptual pressure points that motivate M1;
- the momentum-first wager;
- what the book is trying to do and how it asks to be judged.

It should be conceptually sharp but nontechnical: a legitimization-and-standards part, not a derivation part and not a manifesto.

### Part II — Foundations

Rendered files:
1. `chapters/02-foundations/02-01-core-terms-and-variables.qmd`
2. `chapters/02-foundations/02-02-admc.qmd`
3. `chapters/02-foundations/02-03-invertible-mapping.qmd`
4. `chapters/02-foundations/02-04-space-and-momentum-stage-and-actor.qmd`
5. `chapters/02-foundations/02-05-time.qmd`
6. `chapters/02-foundations/02-06-kinematic-modifiers.qmd`
7. `chapters/02-foundations/02-07-what-foundations-establishes.qmd`

**Job:** state the primitive framework cleanly enough that the reader understands the basic M1 language before entering the first major engine.

Foundations owns:
- primitive terms and notation: fermic momentum, bosic momentum, core momentum, sign locks, and core symbols;
- ADMC as the directional-positive conservation postulate and its realized split;
- the invertible mapping, momentum triangle, conservation equivalence, and SR correspondence;
- the stage/actor distinction between space and momentum;
- time, clocks, dilation, contraction, and the true-frame stance at the currently justified interpretive level;
- kinematic modifiers as the grammar for structured departures from the inertial baseline;
- a clean close stating what Foundations has and has not established.

Foundations should not develop the gravity program. Gravity belongs to Part III. Foundations may only hand off to gravity as the first major downstream case where the relational/spatial stage is altered and local kinematics must be read in context.

### Part III — Gravity and Structured Spacetime

**Job:** make gravity the first major developed engine of the book, and use it to introduce structured spacetime in a disciplined, minimally overcommitted way.

**Part III discipline rule:** gravity should carry real explanatory weight here, not appear as one downstream application among many. Geometry enters in this part only insofar as gravity forces the question of what sort of spatial structure is needed. Most gravity content previously living in Part II should now be treated as belonging here.

**Part III boundary rule:**
- Part II should prepare gravity only at the level of general framework language and modifier taxonomy.
- Part III should carry the real gravity machinery: stationary scope, physical source -> deformation/field representation -> observer readout pipeline, source construction, field construction, observer bookkeeping, a collected stationary correspondence layer, and the first structured-spacetime implications.
- Strong-field and dynamical extensions may be foreshadowed here, but should not be allowed to dominate the mainline stationary arc.

**Working structure references:**
- content map: `book/dev/PART_III_GRAVITY_CONTENT_MAP_V1.md`
- chapter-purpose boundaries: `book/dev/PART_III_GRAVITY_CHAPTER_PURPOSES_V1.md`

Suggested chapter cluster:

10. **Gravity in M1: Philosophical Approach**
    - make the physical M1 gravity claim before introducing machinery
    - explain gravity as momentum content changing the relational/spatial conditions in which other momentum is expressed
    - present the first layer physically: stress, deformation, structuring of the relational stage, and altered local clock/path/transport conditions
    - keep field variables and GR geometry downstream as mathematical representation and comparison language
    - hand off to the concept/symbol chapter once the physical picture is clear

11. **Gravity-Side Core Terms and Variables**
    - define the working route: source -> field -> observer
    - keep physical deformation, M1 field representation, and GR comparison terms conceptually distinct without treating them as five primitive route layers
    - introduce directional source channels `J_k^±`
    - introduce even/odd packaging via `M_k` and `P_k`
    - introduce scalar-well/depth and directional/shift language as mathematical representation of deformation modes
    - prepare the source, field, observer-bookkeeping, and nonstationary chapters

12. **Gravitational Sources**
    - develop directional source channels `J_k^±` after the concept gateway has made them necessary
    - show how even/additive and odd/directional source content capture different physical deformation modes
    - introduce operational source variables such as `rho` and `j_i`
    - state stationary source consistency conditions
    - use minimal source examples and figures without burying the reader in derivation sprawl

13. **The Stationary Gravitational Field**
    - introduce the M1 field representation after the physical deformation picture is established
    - develop scalar-well, shift potential, and flux-tensor packaging
    - give the minimal stationary field map in M1 terms
    - preserve the distinction between physical deformation and its mathematical field description
    - keep detailed classical/GR correspondence out of this chapter except where a brief orientation note is unavoidable

14. **Local Gravity and Observer Bookkeeping**
    - `p_{f,c}`, `\Pi`, `M_{g,loc}`, `H_{g,stat}` symbol discipline
    - local versus asymptotic quantities
    - what is modified, what is conserved, and how transport is read
    - show clocks, paths, and transported momentum as local readouts of altered relational conditions
    - avoid overpromoting QM/Dirac spillover
    - leave proper-time/Kerr/dictionary comparisons to the collected stationary correspondence chapter

15. **Stationary Classical Correspondence**
    - collect the classical comparison material in one place so chapters 3.3–3.5 can remain M1-native
    - calibrate the source packages against ordinary density/current language
    - show the Newtonian scalar limit and stationary shift-current comparison
    - present the metric-facing dictionary and local clock/transport comparison only as correspondence/compression language
    - state clearly what the stationary correspondence establishes and what remains native-derivation work

16. **Nonstationary Gravity: Extension Track**
    - exact locked linear nonstationary baseline
    - retarded scalar and shift picture
    - exact stationary recovery
    - promoted nonlinear layer and tensor slot at explicit maturity labels
    - what now counts as solid first-pass closure versus still-conditional completion work

17. **Spacetime Lessons and Open Boundaries**
    - minimum structural lessons about spacetime from the gravity program
    - what geometry constraints are genuinely forced already
    - what the nonstationary extension track adds without overclaiming final closure
    - where the current program remains correspondence rather than derivation
    - strong-field, dynamical, and ontology-level limits/open questions

Working author-architecture note:
- `book/dev/PART_III_GRAVITY_AUTHOR_ARCHITECTURE_V1.md`

Current planning judgment:
- the opening must be physical-first, not field-first or GR-first.
- `Gravity in M1` should now function as a philosophical approach chapter: momentum content changes the relational/spatial conditions in which other momentum is expressed.
- core concepts and symbols should move into a separate gateway chapter so 3.1 can sing without carrying notation, source algebra, field sectors, and roadmap duties at once.
- the current best reader-facing Part III structure is an eight-chapter arc: philosophical approach, concept/symbol gateway, source construction, stationary field construction, local readout/bookkeeping, collected stationary correspondence, bounded nonstationary extension, and spacetime lessons/open boundaries.
- the stationary correspondence chapter is intentional: it keeps classical density/current/metric-facing comparison from leaking into every native M1 chapter between 3.3 and 3.5.
- appendices should carry the derivation trust layer aggressively so the new mainline chapters read like a book rather than a lab notebook.

### Part IV — Quantum Structure and the Geometry of Expression

**Job:** develop the next layer of state structure needed after gravity: presence vs expression, closure/resonance, candidate carriers, and the QM/Dirac bridge.

**Part IV discipline rule:** this is the natural home for immature-but-important space/state-structure material. Keep toy geometry bounded, keep `Psi`-language disciplined, and connect geometry-of-expression questions to quantum structure rather than treating them as free-floating ontology.

Suggested chapter cluster:

18. **Why Quantum Structure Requires More Than the Inertial Shell**
    - what Foundations + Gravity still leave open
    - why state structure and expression now matter

19. **State Presence, Expression, and `Psi`**
    - `Psi` versus `|Psi|^2`
    - presence versus local expression
    - interference and suppression without ontological disappearance

20. **Closure, Resonance, and Admissibility**
    - stable versus resonant sectors
    - closure logic and admissibility
    - defect/mismatch beginnings at the level currently justified

21. **Candidate Carriers and Toy Geometries**
    - torus/two-cycle as bounded visualization only
    - compact fermic core / larger bosic expression structure
    - comparison of surviving heuristic geometry families

22. **Quantum / Dirac Bridge**
    - wave/operator bridge
    - spinorial structure
    - limited mainline correspondence in clearly stated regimes

### Part V — Cosmology

**Job:** treat cosmology as a separate engine rather than as a buried sub-branch of a generic KM-programs part.

**Part V discipline rule:** cosmology should be presented as its own regime-bounded engine with explicit observational logic, not as a detached speculative appendix to gravity.

Suggested chapter cluster:

23. **Cosmology as a Separate Engine**
    - why this is not just gravity scaled up
    - why KM-B deserves separate treatment here without becoming a whole part architecture elsewhere

24. **Yield Modification and Redshift Structure**
    - `\chi(t)` framing
    - redshift mapping
    - observational interpretation

25. **Cosmological Correspondence, Regimes, and Alternatives**
    - what is recovered
    - what is only regime-bound
    - what remains underdetermined

26. **Cosmology Risks and Open Questions**
    - degeneracy
    - fit dependence
    - what could fail

### Part VI — Generalized State-Space and Composite Programs

**Job:** collect broader downstream extensions that matter, but do not need to come before gravity, quantum structure, or cosmology in the reader's path.

Suggested chapter cluster:

27. **Exclusion and State-Space Constraints**
28. **QFT / EFT Construction**
29. **Composite and Strong-Sector Structure**

### Part VII — Deep Structure and Filtered Grounding

**Job:** place deeper-origin hypotheses where they can support the framework without masquerading as entry prerequisites.

**Part VII discipline rule:** imported deep-structure proposals are downstream of the earlier parts, not upstream of them. In practice, this means Part VII should use the explicit M1 requirement sheet and any BFSS-to-M1 extraction template as filters. Grounding claims should survive M1 translation; they should not redefine M1 primitives.

Suggested chapter cluster:

30. **Micro-Origin Hypotheses**
    - bounded origin candidates and what each is trying to explain
    - no imported framework gets to silently set the primitive ontology
31. **BFSS / String-Compatible Grounding Under M1 Constraints**
    - test which BFSS/string structures survive translation into M1 variables
    - use the extraction-template logic: candidate intrinsic sector, transport sector, aggregate scale, mismatch/closure cost, and readable source -> field -> observer projection
    - keep failures and excessive-ontology routes explicit
32. **What Deep Grounding Explains — and What It Does Not**
    - clear boundary between filtered support, suggestive analogy, and actual derivation
    - state plainly what remains unknown about space and deep structure

### Part VIII — Predictions, Tests, and Failure Modes

**Job:** make the framework judgeable.

Suggested chapter cluster:

33. **Predictions and Benchmark Tests**
34. **Degeneracy, Non-Identifiability, and Model Risk**
35. **Failure Modes and Falsifiers**

### Part IX — Appendices and Derivations

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
| Minimal gravity grammar | Part III — Gravity and Structured Spacetime (with a small preparatory bridge in Part II if needed) | compact correspondence table in appendix if needed |  |
| Core momentum geometry baseline | Part IV — Quantum Structure and the Geometry of Expression, in trimmed form |  |  |
| Torus-like carrier / two-cycle model | Part IV only as a bounded toy model / visualization aid | technical derivations, scans, and stronger ontological claims in appendix/supporting notes |  |
| Internal geometry formulation | Part IV mainline only in sharply trimmed, boundary-disciplined form | dense sector taxonomies and interaction-specific scaffolds in appendix/supporting notes |  |
| Internal geometry worked examples | Part IV selective examples only if they clarify the toy-model role | toy-sector scans, width numerics, closure-defect demos in appendix/supporting notes |  |
| Stationary gravity correspondence / GR dictionary | Part III — Gravity and Structured Spacetime | long coefficient audits in appendix |  |
| Dirac / QM bridge | Part IV — Quantum Structure and the Geometry of Expression | long derivations in appendix |  |
| QFT / EFT framing | Part VI — Generalized State-Space and Composite Programs | ledger/appendix support likely |  |
| Cosmology `\chi(t)` bridge | Part V — Cosmology | fit details / alternative ansatz menus in appendix or supplement |  |
| Exclusion / state-space constraints | Part VI — Generalized State-Space and Composite Programs | appendix for closure arguments |  |
| Composite / strong-sector structure | Part VI if boundary-disciplined and mature enough | appendix/supporting notes if still too exploratory | yes |
| Fit templates / scan machinery |  | Part IX — Appendices / technical supplement |  |
| Detailed ansatz menus |  | Part IX — Appendices / technical supplement |  |
| BFSS / string / sub-particle grounding | Part VII — Deep Structure and Filtered Grounding | appendix support possible |  |
| Predictions/tests | Part VIII — Predictions, Tests, and Failure Modes | supporting calculations in appendix |  |

## Keep / move / defer decisions

### Keep in Part II — Foundations
- primitive vocabulary and notation locks
- ADMC statement and equivalence structure
- shortest readable path through the invertible mapping
- the space-as-stage / momentum-as-actor distinction as the bridge from inertial kinematics to later ontology
- time / clock / dilation interpretation at framework level
- KM taxonomy
- explicit scope/status discipline
- at most a very small bridge sentence or transition into gravity, not the gravity machinery itself

### Keep in Part III — Gravity and Structured Spacetime
- the first full gravity engine treatment
- stationary-first scope and regime framing
- source -> stationary field -> observer pipeline
- source construction and source figures
- stationary field construction / GR dictionary in bounded regime
- observer bookkeeping (`p_{f,c}`, `\Pi`, `M_{g,loc}`, `H_{g,stat}`)
- only the minimum spatial-structure discussion forced by gravity itself

### Keep in Part IV — Quantum Structure and the Geometry of Expression
- `Psi` presence versus `|Psi|^2` expression distinction
- closure / resonance / admissibility material at current justified level
- bounded toy-model / visualization version of the torus or two-cycle carrier picture
- trimmed geometry comparison only where it supports quantum/state-structure legibility
- QM / Dirac bridge

### Keep in Part V — Cosmology
- cosmology as a separate engine
- `\chi(t)` framing and redshift logic
- observational bridge with explicit regime bounds

### Keep in Part VI — Generalized State-Space and Composite Programs
- QFT / EFT program
- exclusion / many-body state-space branch
- composite/strong-sector material only if mature enough for honest mainline placement

### Move to Part IX — Appendices / supporting notes
- long field-equation derivations that are mature enough to support mainline claims
- coefficient audits and closure tables that are stable enough to be cited
- fit templates and scan machinery only when they serve a mature judgeability chapter rather than an exploratory branch
- resonance-width numerics only when they are stable enough to function as support rather than active exploration
- dense state taxonomies introduced too quickly for main narrative, but only after the taxonomy itself is mature enough to preserve
- executable fit workflows like `INTERNAL_GEOMETRY_FIT_TEMPLATE_V1`, with only minimal main-text references where Part VI discusses benchmark logic, degeneracy, or falsifier structure, and only if the workflow remains worth preserving as mature support

### Keep in notes / dev only for now
- immature torus/two-cycle ontology claims
- speculative state taxonomies, particle mappings, or closure classes not yet needed by the manuscript backbone
- exploratory scans, ansatz menus, and patch-sensitive geometry extensions whose main role is active exploration
- exploratory cosmology ansatz menus like `INTERNAL_GEOMETRY_CHI_ANSATZ_MENU_V1` until they become stable enough to support a reader-facing correspondence chapter
- strong/composite sketches that are not yet boundary-disciplined
- BFSS/string candidate structures that have not yet been filtered through an explicit M1 constraint sheet

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

### CQ-02 — How much gravity should live in Part II versus Part III?
- **Why it matters:** this decides whether Part II stops at a minimal bridge into gravity or carries too much engine content before the dedicated gravity part begins.
- **Current Ada recommendation:** Part II should keep only the smallest bridge material needed for readability; Part III should carry the actual gravity grammar, pipeline, source construction, field construction, observer bookkeeping, and structured-spacetime discussion.
- **Need from Arne:** decide whether any compact preview of the gravity pipeline still belongs in Part II, or whether gravity should begin cleanly only in Part III.
- **Arne response:** gravity should be promoted to Part III; most gravity content from Part II should be relocated as part of this move.
- **Status:** resolved enough for current structure
- **Next action when unblocked:** audit Part II chapter notes against the new gravity boundary and strip out any gravity machinery that belongs in Part III.

### CQ-03 — How should the gravity-first Part III be named in the public-facing manuscript?
- **Why it matters:** naming should signal that gravity and structured spacetime now lead the first major engine part, without prematurely turning space-structure speculation into settled ontology.
- **Current Ada recommendation:** prefer `Gravity and Structured Spacetime` or similarly concrete language over a geometry-first or torus-first title.
- **Need from Arne:** confirm the preferred public-facing name once the chapter cluster settles.
- **Arne response:** gravity should be Part III; the detailed content structure should center on stationary scope, pipeline, source, field, observer, and bounded implications for spacetime.
- **Status:** resolved enough for current structure
- **Next action when unblocked:** normalize the part and chapter naming once the surrounding chapter numbers settle.

### CQ-06 — Should most torus material be demoted from mainline architecture?
- **Why it matters:** if the torus/two-cycle construction does not satisfy the requirements for core momentum conservation, it should not be allowed to function as a mainline explanatory backbone.
- **Current Ada recommendation:** yes — demote most torus content from `leading realization` status to a bounded `toy model / visualization aid` role unless and until a conservation-clean formulation exists. Keep only the smallest amount of torus material needed to illustrate possible relations between `p_f`, `p`, closure, and gravity-driven deformation.
- **Need from Arne:** confirm whether you want the manuscript to keep one short public-facing toy-model chapter/section, or to move the torus almost entirely out of the mainline.
- **Arne response:** yes — adopt this plan and stance. Keep the torus only as a bounded symbolic / visualization layer for something real but simplified, not as the framework’s core explanatory backbone. Also: keep speculative / immature material in working notes for now; appendices should not carry immature topics.
- **Status:** resolved enough for current structure
- **Next action when unblocked:** rewrite Part III source-artifact placements so torus material is explicitly split into `mainline toy-model / visualization`, `appendix-ready mature support`, and `notes/dev-only speculative material`.

### CQ-07 — Should M1 geometry constraints be made explicit before evaluating BFSS/string candidate structures?
- **Why it matters:** this fixes the methodological order. If M1 is primary, imported geometries should be filtered by M1 constraints rather than allowed to redefine them.
- **Current Ada recommendation:** yes — keep the explicit requirement sheet and later use it to reduce the BFSS/string solution space, but do not let that methodology dominate the early book architecture.
- **Need from Arne:** confirm whether this should remain the default evaluation protocol even after the gravity-first restructure.
- **Arne response:** yes — adopt this. Explicitly state the new M1-imposed constraints on admissible geometry, then later use them to prune the BFSS/string candidate space.
- **Status:** resolved enough for current structure
- **Next action when unblocked:** maintain the current stable Part IV / Part VII split using the consolidated requirements note, the geometry comparison checklist, and the BFSS-to-M1 extraction template rather than expanding the backbone further.

### CQ-04 — Is the composite / strong-sector material mature enough for a mainline Part VI chapter?
- **Why it matters:** this determines whether strong-sector content appears as a full downstream chapter or remains appendix-backed / supporting.
- **Current Ada recommendation:** keep it only if it can be presented with strict boundary discipline; otherwise demote it for now.
- **Need from Arne:** confirm whether he wants a bounded strong-sector chapter in the main outline now, or a placeholder/deferred note.
- **Arne response:**
- **Status:** open
- **Next action when unblocked:** either keep the bounded Part VI slot or move the material to deferred/supporting status.

### CQ-05 — How large should the cosmology part be?
- **Why it matters:** cosmology now has its own part, so the structure needs to decide whether one chapter is enough or whether the engine naturally wants a small multi-chapter arc.
- **Current Ada recommendation:** keep a small multi-chapter arc now: engine framing, redshift/yield logic, regime-bounded correspondence, and explicit risks/open questions.
- **Need from Arne:** decide whether this is the right visible granularity or whether cosmology should be compressed further.
- **Arne response:** cosmology should have its own part; it is a separate engine.
- **Status:** partially resolved
- **Next action when unblocked:** tune chapter density within Part V without changing its separate-engine status.

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
- **Resolved mapping 6:** `book/dev/INTERNAL_GEOMETRY_WAVE_EQUATION_PREP_V1.md` belongs as a **supporting source** behind **Part IV — `Quantum / Dirac Bridge`**, especially for the clean torus-carrier wave setup, the explicit W1-vs-W2 choice framing, admissibility/closure constraints, and the staged D1-D3 derivation agenda.
- **Why:** the file is a disciplined preparation note that clears conceptual mud before renewed fitting. It is valuable because it separates fixed locks from current freedom and states the wave-level stop conditions explicitly, but it is better treated as setup/support for the stronger formulation file than as the chapter's primary backbone.
- **Resolved mapping 7:** `book/dev/INTERNAL_GEOMETRY_WAVE_DIRAC_FILTER_V1.md` belongs primarily in **Part VII — Appendices / technical supplement**, with at most a compact supporting reference from **Part IV — `Quantum / Dirac Bridge`** where parameter-discipline or operating-point triage needs brief justification.
- **Why:** the file is a narrow, scan-specific filter note that applies a conservative Dirac-consistency control scalar to a previously identified candidate region. That makes it useful as an audit trail for why some parameter regions were demoted, but too specific and too tied to one scan pass to function as mainline prose.
- **Resolved mapping 8:** `book/dev/INTERNAL_GEOMETRY_EM_CHANNEL_DERIVATION_V1.md` belongs primarily in **Part IV — `Quantum / Dirac Bridge`**, with only a bounded forward link toward later state-space/composite chapters where charge-sign bookkeeping or channel admissibility is reused.
- **Why:** the note is the strongest current derivation-level bridge from internal orientation structure to an EM-like coupling channel: it gives the orientation-to-signed-coupling map, derives the source equation and conserved current from one action, closes the static and Lorentz-force sign story, and states explicit falsifier/regime gates. That makes it a good support source for the Part IV bridge chapter's correspondence logic, but the validation harness, scoring workflow, and strict-tier promotion machinery are too process-heavy for mainline prose and belong in appendix/supporting status.
- **Resolved mapping 9:** `book/dev/EM_WORK_INDEX_V1.md` belongs in **Part VII — support / authoring infrastructure**, not as manuscript content.
- **Why:** it is a consolidated artifact index, re-ingest order, and execution tracker for the EM validation cluster. Its value is navigational and operational, not explanatory.
- **Resolved mapping 10:** `book/dev/INTERNAL_GEOMETRY_EM_STRICT_EVIDENCE_TIER_V1.md` belongs in **Part VII — appendix / validation-policy support**, with at most a brief Part IV note that EM correspondence claims are being graded through stricter evidence tiers.
- **Why:** the file is a policy-and-gate specification for how validation confidence is promoted, not a derivation of framework structure. It strengthens auditability but should stay out of reader-facing mainline prose except as background support for how strong a claim is being made.
- **Resolved mapping 11:** `book/dev/INTERNAL_GEOMETRY_EM_VALIDATION_DATA_CURATION_V1.md` belongs in **Part VII — appendix / source-curation support**.
- **Why:** the file is a provenance registry and curation note for validation records. That is valuable for audit trails and review, but it is not manuscript narrative and should not occupy mainline Part IV real estate.
- **Resolved mapping 12:** `book/dev/INTERNAL_GEOMETRY_EM_VALIDATION_RUN_TEMPLATE_V1.md` belongs in **Part VII — support / reproducibility infrastructure**.
- **Why:** the file is an executable workflow template for scoring/report generation. Its role is operational reproducibility, not conceptual exposition.
- **Resolved mapping 13:** `book/dev/M1_GEOMETRY_CONSTRAINTS_ON_BFSS_SOLUTION_SPACE_V1.md` belongs primarily at the **Part III / Part V boundary**, with its main methodological spine serving **Part III — `M1 Geometry Constraints`** and its pruning consequences feeding **Part V — filtered BFSS/string grounding**.
- **Why:** the note makes the methodological order explicit: M1 constraints come first, imported BFSS/string structure is filtered second. Its hard/soft constraint sheet strengthens Part III directly, while its verdict table and pruning summary give Part V a disciplined non-derivative role. It should remain an internal support source for now rather than manuscript prose.
- **Next target:** continue the chapter-to-source map with the next unmapped Part IV / Part VII source, or switch to WQ-03 and tighten Part IV chapter-level descriptions now that the EM cluster is more cleanly separated into mainline bridge vs validation-support layers.

### WQ-02 — Tighten chapter-level descriptions for Part II
- **Status:** completed (2026-03-29)
- **Result:** Part II now exists as a drafted eight-subsection spine covering primitives, ADMC, invertible mapping / momentum triangle / SR correspondence, the stage/actor distinction between space and momentum, time/dilation interpretation, KM taxonomy, minimal gravity grammar, and scope/status discipline.
- **Refinement pass:** terminology is now tightened so `fermic` / `bosic` apply to momentum language while `fermionic` / `bosonic` apply to structure/geometry language; `M` is now described as representative of total momentum content; ADMC is stated as direction-general rather than axis-restricted; and rebuildable manuscript figures are now wired into the repo for Foundations.
- **Follow-up:** future edits should be refinement-level unless a foundational lock is intentionally reopened.

### WQ-03 — Tighten chapter-level descriptions for Part IV
- **Status:** in progress
- **Focus:** keep gravity, QM/QFT, cosmology, and KM-C/composite chapters structurally parallel where possible.
- **Current preparation note:** the EM cluster is now cleanly split between one bounded Part IV bridge source (`INTERNAL_GEOMETRY_EM_CHANNEL_DERIVATION_V1.md`) and Part VII-only validation/reproducibility infrastructure (`INTERNAL_GEOMETRY_EM_STRICT_EVIDENCE_TIER_V1.md`, `INTERNAL_GEOMETRY_EM_VALIDATION_DATA_CURATION_V1.md`, `INTERNAL_GEOMETRY_EM_VALIDATION_RUN_TEMPLATE_V1.md`, `EM_WORK_INDEX_V1.md`). Use that separation when tightening the `Quantum / Dirac Bridge` chapter description so validation governance does not leak into mainline exposition.
- **Heartbeat update (2026-03-31):** tightened the intended job of `Quantum / Dirac Bridge` so it now reads more cleanly as the first operator-level lift out of Part III geometry rather than as a container for every wave/EM/QM workflow note.
- **Refined chapter spine:**
  - **inherits:** Part III carrier geometry, closure logic, and spin-slot scaffolding
  - **adds:** baseline torus-wave equation, winding embedding choice, conserved internal-wave functional, and the first operator / spinorial lift needed to state a Dirac-style bridge
  - **target:** regime-bounded QM / Dirac correspondence, including the orientation-to-signed-coupling bridge only at the level needed to motivate EM-sign structure
  - **mainline keep:** conceptual bridge from carrier geometry to operator language; the meaning of the wave field and winding sectors; one clean conserved-functional / admissibility story; limited key equations; the bounded EM sign/coupling correspondence where it clarifies the bridge
  - **appendix offload:** calibration ansatz menus, scan grids, parameter filters, strict-tier evidence governance, source-curation mechanics, reproducibility templates, and long derivation overflow
- **Why this tightening helps:** `INTERNAL_GEOMETRY_WAVE_EQUATION_FORMULATION_V1.md` is strong enough to anchor the chapter’s wave/operator spine, while `INTERNAL_GEOMETRY_WAVE_EQUATION_PREP_V1.md` and `INTERNAL_GEOMETRY_EM_CHANNEL_DERIVATION_V1.md` can support that spine without letting setup notes or validation workflow become the chapter’s real center of gravity.
- **Heartbeat update (2026-03-31, QFT):** tightened the intended job of `QFT / EFT Construction` so it reads as a disciplined stationary-foundation chapter rather than as a grab-bag of broader phenomenology or premature closure claims.
- **Refined QFT chapter spine:**
  - **inherits:** the operator-level lift from `Quantum / Dirac Bridge`, the stationary gravity/transport language, and the fixed notation/convention discipline needed to prevent sign drift
  - **adds:** a minimal stationary EFT core action, explicit finite operator basis, EOM/propagator closure route, overlap-regime bookkeeping, and a claim-gating ledger for exact vs closure-dependent pieces
  - **target:** stationary EFT/QFT construction in a declared overlap regime, not full covariant completion or broad phenomenological triumphalism
  - **mainline keep:** the canonical convention lock that stabilizes symbols and propagator normalization; the minimal D1 action block and KM-A operator classes; the clean action -> EOM -> propagator -> overlap workflow; the exact-vs-closure ledger and regime fence
  - **appendix offload:** detailed coefficient workbooks, normalization audits, residual ledgers, benchmark-ingestion workflow, audit execution queues, and any broader nonstationary/composite extensions
- **Why this tightening helps:** `QFT_FOUNDATION_CORE_BLUEPRINT_V1.md`, `QFT_STATIONARY_EFT_DERIVATION_CORE_V1.md`, and `QFT_CORE_CONVENTIONS_LOCK_V1.md` already support one coherent chapter identity: build the smallest auditable stationary QFT foundation first, freeze conventions, and refuse broader claims until overlap closure is explicit. Making that the chapter spine keeps Part IV parallel and prevents the QFT chapter from absorbing every downstream ambition.
- **Next target:** propagate the same sharper `inherits -> adds -> target -> mainline keep -> appendix offload` treatment to `Cosmology as a KM-B Program`, then decide whether the Part IV chapter blurbs themselves should be rewritten to match.

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
| `INTERNAL_GEOMETRY_WAVE_EQUATION_PREP_V1.md` | Part IV — `Quantum / Dirac Bridge` (supporting source) | clean torus-carrier wave setup, W1-vs-W2 choice framing, admissibility/closure constraints, D1-D3 derivation agenda | spectrum tables, preparatory derivation notes, stop-condition scaffolding | best read as a disciplined setup note feeding the main wave-equation formulation rather than as an independent chapter backbone |
| `INTERNAL_GEOMETRY_WAVE_DIRAC_FILTER_V1.md` | Part IV — `Quantum / Dirac Bridge` (appendix / support) | conservative parameter-discipline reference for the Dirac bridge if a compact filter note is useful | scan triage, operating-point selection, filter criterion audit trail | useful to justify why high-eta wave-scan regions were demoted, but too narrow and scan-specific for mainline prose |
| `INTERNAL_GEOMETRY_EM_CHANNEL_DERIVATION_V1.md` | Part IV — `Quantum / Dirac Bridge` with bounded forward link to composite/state-space chapters | orientation-to-signed-coupling bridge, single-action source/current derivation, static/dynamical sign-law closure, explicit falsifier regime table | validation harness details, score gates, source-curation mechanics, robustness-tier hardening | strongest current EM-channel bridge note; useful mainline only at the level of the sign/coupling story and regime-bounded correspondence, not as a full validation narrative |
| `INTERNAL_GEOMETRY_EM_STRICT_EVIDENCE_TIER_V1.md` | Part VII — appendix / validation-policy support for Part IV EM material | at most a brief Part IV mention that correspondence claims are promoted through stricter evidence tiers | strict-tier gate rules, uncertainty-aware scoring policy, sample-floor requirements, robustness hardening path | validation-governance artifact, not reader-facing theory exposition |
| `INTERNAL_GEOMETRY_EM_VALIDATION_DATA_CURATION_V1.md` | Part VII — appendix / source-curation support | none directly; at most invisible audit support behind Part IV EM correspondence claims | source registry, extraction provenance, curation cautions, record-ingestion notes | belongs with validation/audit infrastructure rather than manuscript narrative |
| `INTERNAL_GEOMETRY_EM_VALIDATION_RUN_TEMPLATE_V1.md` | Part VII — support / reproducibility infrastructure | none directly | executable scoring workflow, run command, output checklist, gate thresholds | workflow template rather than manuscript content |
| `EM_WORK_INDEX_V1.md` | Part VII — support / authoring index | none directly; at most invisible workflow support while drafting Part IV | artifact registry, re-ingest order, execution tracker, validation-file navigation | operational index rather than manuscript content |
| `M1_GEOMETRY_CONSTRAINTS_ON_BFSS_SOLUTION_SPACE_V1.md` | Part III — `M1 Geometry Constraints`; secondary support for Part V — filtered BFSS/string grounding | hard/soft constraint sheet, candidate-structure verdict logic, explicit M1-first filter order | deeper BFSS/string pruning details and any later comparison expansions | useful as the bridge that keeps Part V subordinate to Part III constraints rather than the other way around |
| `M1_AS_A_PRUNING_AND_EFFECTIVE_VARIABLE_DISCIPLINE_FOR_BFSS_V1.md` | Part V — filtered BFSS/string grounding; secondary support for Part III boundary discipline | M1-as-filter framing, BFSS effective-subsector logic, conflict map, ontology-budget stance | later BFSS-to-M1 dictionary attempts and deeper micro-origin adjudication | frames BFSS as a candidate deep support layer only if an M1-effective truncation can be made explicit |
| `FLAT_SPACE_M1_GEOMETRY_SOLUTION_SPACE_V1.md` | Part III — `M1 Geometry Constraints` / candidate-carrier filtering | flat-space hard/soft constraint sheet, reduced solution-space judgment, candidate-family triage, small-fermic / large-bosic heuristic | later family-by-family comparison tables and sketchbook-style geometry support | useful because it strips away gravity/cosmology and asks what geometry must still do just to support electrons and the interaction sectors |
| `PSI_PRESENCE_VS_ABS_PSI2_EXPRESSION_AND_BOSIC_SWELLING_V1.md` | Part III support note / cross-cutting interpretation lock | `Psi`-level presence vs `|Psi|^2`-like expression, bosic swelling retention, time-dilation retention | later formal projection/functionals note if promoted | useful as the easy-find reminder that particle presence, local expression, bosic extension, and time dilation should not be conflated |

**EM-cluster placement lock (working):** keep only `INTERNAL_GEOMETRY_EM_CHANNEL_DERIVATION_V1.md` as the bounded Part IV bridge source for reader-facing EM/sign correspondence. Treat the strict-tier spec, curation registry, run template, and work index as Part VII validation/reproducibility infrastructure unless later manuscript drafting reveals a genuinely reader-facing methodological paragraph worth promoting.

### WQ-05 — Identify what is ready for review versus what remains unstable
- **Status:** open
- **Focus:** keep the mainline outline honest and prevent premature locking.

## Ready for review

- Part I / Part II / Part III / Part IV / Part V / Part VI / Part VII architecture at the level of major part boundaries.
- Core judgment that Foundations must include the space-as-stage / momentum-as-actor bridge, time, and KM taxonomy, but should stop before a dedicated gravity subsection.
- Core judgment that Part III, not Part II, should carry the real gravity terminology and machinery: source-side parity split, stationary field packaging, observer bookkeeping, and the first readable correspondence layer.
- Current manuscript judgment: the former bridge subsection `02-07-minimal-gravity-grammar.qmd` is now redundant and should remain out of the rendered Foundations chapter unless later needed in heavily reduced form.
- Core judgment that cosmology currently belongs inside the Part IV downstream program cluster.
- Drafted Part II manuscript text in `chapters/02-foundations/`, rendered successfully to HTML.
- Foundations terminology pass completed: `fermic` / `bosic` are now momentum adjectives, `fermionic` / `bosonic` are structure/geometry adjectives.
- Foundations figure pass completed with rebuildable figure scripts and outputs for shell language, momentum triangle, and source -> field -> observer grammar; the source-side directional density map now belongs conceptually with Part III source construction rather than with the Foundations bridge subsection.
- Gravity-architecture review result (2026-04-10, updated 2026-04-11): use a fresh-start six-chapter Part III reader-facing structure after quarantining the old draft in `_old`; freeze the stationary/classical overlap material as the real mainline backbone; give the upgraded nonstationary package one explicit bounded extension chapter; treat full completion claims as still open; and keep divergence-audit material out of the Part III explanatory spine unless later maturity clearly justifies promotion.

## Significant blockers

_None currently._

Add blockers here only when they materially prevent the next structural step.

## Next smallest win

Hand the fresh-start Part III package to an author with one clean chapter-and-appendix map, then begin drafting `03-01 Gravity in M1` against that handoff rather than reusing the quarantined `_old` chapter prose.
