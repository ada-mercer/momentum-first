# Author notes — Chapter 04 Quantum Mechanics

Status: first manuscript skeleton + opening/notation draft
Created: 2026-05-10
Updated: 2026-05-10 — renamed section 02 to continue the `Core Terms and Variables` chapter pattern.
Mode stack: roles/book-prose + topics/m1 + artifacts/manuscript + styles/book-mainline + audiences/broad-technical

## Chapter burden

Build the M1 quantum bridge as a clean operator/correspondence chapter:

1. Establish basic QM in M1 language.
2. Introduce the core momentum operator `\hat M`; keep energy-unit Hamiltonian notation in the correspondence section only.
3. Show the stationary gravity form `\hat M_g`.
4. Establish correspondence to standard QM/Dirac, the nonrelativistic limit, and the classical/stationary-gravity limit.

## Boundary lock

Presence-vs-expression is allowed only as a light support note around `\Psi`, phase, and expression/detection. Do not let this chapter become about branch ontology, torus geometry, full internal geometry, EM projectors, QFT completion, measurement theory, or compact-object applications.

## Section map and theory/source links

### 01 — Quantum mechanics after gravity
- Job: open from the gravity-chapter handoff and define the chapter's burden; mention early that M1 naturally supports strong-gravity quantum effects because scalar wells modify the local fermic scale inside the operator.
- Add a bounded quantum-source bridge near the opening: in quantum regimes, $J_k^\pm$ are read as state-dependent readings/functionals of the momentum organization carried by the phase-bearing state $\Psi$, with point-particle source densities recovered only as classical/localized compressions. Boundary: no measurement theory, full QFT source law, or complete self-gravity equation.
- Source links: `book/dev/QM_CHAPTER_AUTHOR_HANDOVER_2026-05-10.md`; `book/dev/QM_CHAPTER_HIGH_LEVEL_AUTHOR_PLAN_V1.md`; gravity chapter close in `chapters/02-tier-2-engines/03-gravity-and-structured-spacetime/08-spacetime-lessons-and-open-boundaries.qmd`.
- Writing theory: begin from the conceptual pressure, not from a roadmap; keep the reader's path clear.

### 02 — Core Terms and Variables
- Job: continue the established chapter-opening pattern from Foundations and Gravity by giving the quantum-side vocabulary gateway: state, phase, expression, operator/scalar reading, M-generator language, and stationary gravity operator terms.
- Source links: `book/m1/TERMINOLOGY.md`; `MEMORY.md` M1-1; notation note in `book/dev/QM_CHAPTER_HIGH_LEVEL_AUTHOR_PLAN_V1.md`.
- Writing theory: this is a terms-and-variables lock section; repeat inherited variables only enough to anchor the reader, then focus on the new quantum/operator vocabulary.

### 03 — The core momentum operator
- Job: introduce flat `\hat M=\beta p_f+\boldsymbol\alpha\cdot\hat{\mathbf p}`; explain why the linear Dirac form is the first-order quantum packaging of `M^2=p_f^2+p^2`; distinguish linear state evolution from nonlinear scalar magnitude recovery.
- Source links: `book/tiers/T2_engines/QM_DIRAC_M1_SUMMARY.md`; `book/source/dirac-m1-stationary.txt`; cautious background in `book/dev/INTERNAL_GEOMETRY_WAVE_EQUATION_FORMULATION_V1.md`.
- Boundary: no torus/internal-geometry derivation in mainline.

### 04 — Stationary gravity and the operator `\hat M_g`
- Job: show `p_{f,c}`, `\hat{\boldsymbol\Pi}`, and `\hat M_g` as the gravity deformation of `\hat M`; explicitly show compatibility by squaring the local/principal symbol to recover `M_{g,loc}`.
- Source links: `book/tiers/T2_engines/QM_DIRAC_M1_SUMMARY.md`; `chapters/02-tier-2-engines/03-gravity-and-structured-spacetime/05-local-gravity-and-observer-bookkeeping.qmd`; `appendices/derivations/03-05A-local-observer-bookkeeping.qmd`.
- Note: this chapter uses the simplified momentum-potential convention `\hat{\boldsymbol\Pi}=\hat{\mathbf p}-\mathbf A_g`; the gravity chapter's normalized shift convention can be footnoted later if needed.

### 05 — Why the Schrödinger form appears
- Job: introduce the energy-unit Hamiltonian translation only here, explain `i\hbar\partial_\tau\Psi=\hat H\Psi=c\hat M\Psi` as standard phase-generator structure, then recover standard flat Dirac/QM notation.
- Source links: `book/dev/QM_CHAPTER_HIGH_LEVEL_AUTHOR_PLAN_V1.md`; `book/tiers/T2_engines/QM_DIRAC_M1_SUMMARY.md`.

### 06 — The nonrelativistic limit
- Job: show `M=p_f+p^2/(2p_f)+...`, recover ordinary kinetic energy after multiplying by `c`, and explain why the low-speed envelope has the usual second-order spatial kinetic operator.
- Source links: high-level author plan; FW expansion material in `book/source/dirac-m1-stationary.txt` only as appendix/support.
- Boundary: keep spin-gradient/FW details out of mainline unless a later pass demands them.

### 07 — Classical and stationary-gravity limits
- Job: connect operator language back to `M_{g,loc}` and the stationary transport-generator distinction without symbol overload.
- Source links: `book/m1/TERMINOLOGY.md`; gravity chapter local observer chapter and derivation appendix.

### 08 — Strong gravity and quantum sensitivity
- Job: state the bounded M1-vs-classical difference: strong scalar wells modify the contextual fermic scale, which can enhance tunneling and narrows the strongest equivalence-principle reading for local quantum internal-scale problems.
- Source links: `book/tiers/T2_engines/QM_DIRAC_M1_SUMMARY.md`; gravity chapter local gravity bookkeeping; later phenomenology should stay out of mainline here.
- Boundary: no named compact-object applications; keep this as a structural consequence of `p_f -> p_{f,c}`, not a phenomenology chapter.

### 09 — What the quantum chapter establishes
- Job: close with earned results and explicit boundaries.
- Source links: author handover boundary list; book style guide on honest scope.
