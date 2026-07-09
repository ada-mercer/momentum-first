# Verification Policy

This project accepts contributions from both humans and AI systems as **real contributions**.
A contribution becomes part of the evolving framework only after review and verification.
Verification does **not** have to be performed by a human, but not every model or review pass qualifies.

## Purpose

The purpose of this policy is to let the framework evolve rapidly without forcing all progress through a human bottleneck, while still maintaining explicit standards for acceptance.

## Core principles

- AI contributions are genuine contributions, not invisible assistance.
- AI verification is valid when it meets the project standard.
- Authorship and verification are related but distinct.
- Stronger claims require stronger review.
- Verification must be explicit enough to audit later.
- Manuscript prose should not carry internal policy language unless the reader genuinely needs it.

## Claim-role taxonomy for writers and reviewers

Use this taxonomy as **internal writing and review guidance**, not as a requirement to foreground the labels in the manuscript.

### Derivation
A derivation claim says that, given the stated assumptions and setup, a later result follows in an inspectable way. It may still be regime-bound, but it should not depend on silent redefinitions, hidden imports, or unexplained jumps.

### Correspondence
A correspondence claim says that M1 reproduces, organizes, or maps onto a known structure in a stated regime. This is weaker than derivation and should not be written as though the target theory has thereby been explained from first principles.

### Interpretation
An interpretation claim proposes how the formalism should be read. Interpretive material may be valuable and even central, but it should not silently carry more weight than the formal structure beneath it can support.

### Speculation
A speculation claim marks a promising but unsecured direction. It may still belong in notes, planning, or carefully bounded manuscript discussion, but its provisional status should remain visible to writers and reviewers.

## Regime discipline

For substantial technical prose, writers and reviewers should also ask:
- what regime is being claimed,
- what assumptions are active,
- what is actually established in that regime,
- and what remains outside the present closure.

Typical regime labels include inertial baseline, isolated system, stationary background, weak-field, slow-motion, quasi-stationary, or other explicitly stated approximation domains.

## Verification tiers

### V1 — Editorial verification

Appropriate for:
- readability
- prose quality
- local structure
- duplication
- basic consistency

A V1 verifier must be able to:
- follow long-form prose
- identify unclear or redundant passages
- preserve section intent while editing
- produce explicit accept/revise judgments

### V2 — Conceptual verification

Appropriate for:
- logical coherence
- framework consistency
- claim typing
- assumption tracking
- fit with prior section locks

A V2 verifier must be able to:
- distinguish derivation from correspondence, interpretation, and speculation
- identify unsupported jumps
- check consistency with prior accepted framework structure
- produce explicit review outcomes and reasons

### V3 — Technical verification

Appropriate for:
- derivations
- formal definitions
- mappings
- mathematical claims
- theorem-like or proof-like sections

A V3 verifier must be able to:
- follow or reconstruct mathematical argument
- detect formal inconsistency
- test notation discipline
- identify regime or assumption mismatch
- produce explicit review outcomes and reasons

## Capability threshold

A verifier counts only if it satisfies **both**:

1. It is a frontier or near-frontier model for the relevant task class at the time of use, **or** has been locally validated by the project as reliable for that review tier.
2. It is used in a review mode appropriate to the material under consideration.

The project may maintain a separate registry of currently approved verifier models and their eligible tiers.

## Review requirements

For verification to count, the review must:
- be performed in a distinct review pass, not merely in the drafting stream
- be appropriate to the section type and claim strength
- explicitly identify the review outcome
- record enough output to make the judgment inspectable later

Accepted review outcomes:
- **accepted**
- **accepted with minor edits**
- **revision required**
- **rejected**

## Independence requirement

Verification is stronger when the reviewer is independent of the original drafting pass.

Preferred order of strength:
1. different capable model
2. same model family in a fresh review session with a verification prompt
3. same model in the same broad system but clearly separated review mode

For V3 material, prefer:
- one top-tier independent verifier, or
- two independent strong verifiers

## Section-level expectations

- Preface and purely orienting prose usually require at least **V1**, and **V2** when conceptual claims are nontrivial.
- Introduction-level conceptual framing should usually receive **V2**.
- Foundations and derivation-heavy material should usually receive **V3**.
- Long derivations in `appendices/derivations/` should not be treated as accepted without V3 review.

## Authorship vs verification

Authorship answers: **who substantively wrote or shaped this section?**

Verification answers: **has this section been reviewed strongly enough to count as part of the framework?**

These are not the same question and should not be conflated.

## Current project posture

- Named author: **Arne Klaveness**
- AI systems may contribute through reviewable proposal workflows and may be credited under the category label **AI-assisted** where appropriate.
- Human review is welcome, but not mandatory in every case.
- Capability-qualified AI review is sufficient when it meets the standards above.
