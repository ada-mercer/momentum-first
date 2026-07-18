# Derivations Appendix

This folder holds derivation appendices that support the main text without overloading the flow of the primary chapters.

## Naming rule

Each derivation file is labeled according to the **first section or subsection where it is cited**, followed by a running letter.

Examples:
- `3.1A`
- `3.1B`
- `2.5A`
- `2.5B`

## Filename convention

Use a filesystem-safe form while preserving the visible derivation label inside the file.
Recommended filename pattern:

- `03-01A-short-slug.qmd`
- `03-01B-short-slug.qmd`
- `02-05A-short-slug.qmd`

This keeps lexicographic ordering stable while preserving the human numbering convention.

## In-text reference style

In the main text, refer to derivations by their visible label, for example:
- Derivation 3.1A
- Derivation 2.5B

## Purpose

Put in this folder:
- longer algebraic derivations
- technical expansions that interrupt narrative flow
- alternate derivation paths worth preserving
- supporting proofs/checks for a section's main claims

Keep in the main section:
- core definitions
- main theorem/postulate statements
- the shortest argument needed to preserve readability
