# Contribution and verification provenance

This directory records section-level contribution and human-verification status for *Momentum First*.

## Public authorship rule

The formal manuscript author and DOI creator is **Arne Klaveness**.

AI assistance may be credited as contribution, but the public ledger uses the category label **AI-assisted** rather than naming a particular AI system or persona. The label means non-human assistance contributed to drafting, editing, review, derivation support, repository work, or related preparation. It is not a formal author name.

## Ledger model

The section ledger is `section-ledger.yml`. Each entry should stay simple:

```yaml
- title: Example section
  path: chapters/example.qmd
  contributors:
    - Arne Klaveness
    - AI-assisted
  contribution_note: >
    Free-text description of the relative contribution, e.g. Arne supplied the core
    idea and final acceptance; AI-assisted drafting shaped the first prose pass.
  human_verification: partially_verified
  verification_note: >
    Free-text description of what has or has not been checked by the human author.
```

## Verification status values

- `verified` — human verification has been recorded for the section.
- `partially_verified` — some human review is recorded, but material remains pending.
- `not_yet_verified` — known to lack human verification.
- `not_yet_recorded` — no ledger decision has been made yet.

Contribution and verification are separate. A section may have substantial AI-assisted contribution and still be human-verified; it may also be AI-assisted and not yet human-verified. The ledger exists to make that distinction explicit before DOI publication.
