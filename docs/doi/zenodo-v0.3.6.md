# Zenodo metadata draft — Momentum First v0.3.6

Status: historical metadata draft; no DOI was reserved or created. The active
procedure is `docs/doi/README.md`.
Prepared: 2026-07-28

## Record architecture

Use one canonical Zenodo **Publication / Book** record for the released
`Momentum-First.pdf`. The initial deposit should create:

- a version DOI for the exact v0.3.6 PDF;
- a concept DOI for the manuscript across later versions.

Do not create a separate source/software DOI for v0.3.6. The repository URL and
GitHub Release remain related identifiers, not a competing citation target.

## Metadata

- **Title:** Momentum First
- **Creator:** Arne Klaveness
- **Resource type:** Publication / Book
- **Publication date:** 2026-07-28
- **Version:** 0.3.6
- **Language:** English
- **License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0
  International (`CC-BY-NC-SA-4.0`)
- **Description:** Momentum First is a pre-1.0 theoretical manuscript exploring
  a momentum-centered framework for foundations, gravity, quantum mechanics,
  and cosmology. It develops Additive Directional Momentum Conservation,
  directional shell readings, gravity and quantum bridge structures, and a
  translation-yield account of cosmological expansion.
- **Keywords:** physics; theoretical physics; momentum; gravity; quantum
  mechanics; cosmology; quarto book
- **Contributor acknowledgement:** Developed with AI-assisted drafting, review,
  editing, formalization, source, figure, and repository support. Arne
  Klaveness remains the sole manuscript author and DOI creator; all claims,
  interpretations, and release decisions remain his responsibility.
- **File:** the exact `Momentum-First.pdf` attached to GitHub Release `v0.3.6`
- **ORCID:** omit unless Arne supplies and confirms one

## Related identifiers

Review the relation before entry; do not guess it in the production record.
Candidate identifiers:

- `https://github.com/ada-mercer/momentum-first`
- `https://github.com/ada-mercer/momentum-first/releases/tag/v0.3.6`

The selected relation must say accurately how the deposited PDF relates to the
repository or release. Do not use `isIdenticalTo` unless the identified object
is the same exact PDF.

## Artifact fields to freeze

Populate these only from the final clean candidate:

- filename: `Momentum-First.pdf`
- pages: pending final candidate
- bytes: pending final candidate
- SHA-256: pending final candidate
- candidate commit: pending final candidate

## DOI-in-PDF decision

No DOI is currently reserved or printed in the manuscript. Before final content
freeze, Arne must choose one:

1. **Do not print the DOI in v0.3.6 (recommended).** Freeze and release the PDF,
   deposit that exact file, then add DOI backlinks to the repository and site
   after publication. This avoids a circular reserve–rerender–recheck step.
2. **Print the version DOI in v0.3.6.** Defer final freeze, reserve the DOI in
   WP5, add an identifier line to the manuscript, rerender, recommit, and repeat
   the artifact gate before release.

Neither choice authorizes DOI reservation or publication.
