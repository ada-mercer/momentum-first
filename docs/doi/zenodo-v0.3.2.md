# DOI metadata plan for Momentum First v0.3.2

This note prepares two DOI paths after the `v0.3.2` release is published.

## 1. PDF manuscript DOI

Recommended Zenodo deposit type: **Publication / Book** or **Publication / Report**.

Recommended uploaded file:

- `Momentum-First.pdf` from GitHub Release `v0.3.2`

Recommended metadata:

- **Title:** Momentum First
- **Version:** 0.3.2
- **Creator:** Arne Klaveness
- **Contributor / acknowledgement note:** Developed with AI-assisted drafting, review, editing, and repository automation support. All claims, interpretations, and release decisions remain the responsibility of the human author.
- **Description:** Momentum First is a pre-1.0 theoretical manuscript exploring a momentum-centered framework for foundations, gravity, quantum mechanics, and cosmology. It develops Additive Directional Momentum Conservation, positive directional momentum channels, gravity and quantum bridge structures, and a translation-yield account of cosmological expansion.
- **Keywords:** physics; theoretical physics; momentum; gravity; quantum mechanics; cosmology; quarto book
- **Language:** English
- **License:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (`CC-BY-NC-SA-4.0`)
- **Related identifier:** `https://github.com/ada-mercer/momentum-first/releases/tag/v0.3.2` with relation `isSupplementedBy` or `isIdenticalTo` only if Zenodo guidance supports the chosen relation for the uploaded release PDF.

Recommended citation after DOI creation:

> Klaveness, A. (2026). *Momentum First* (Version 0.3.2). Zenodo. https://doi.org/...

## 2. GitHub repository/source DOI

Recommended route: Zenodo GitHub integration.

Steps:

1. Connect Zenodo to GitHub.
2. Enable repository `ada-mercer/momentum-first` in Zenodo.
3. Ensure `CITATION.cff` is present in the repository root.
4. Create or re-run a GitHub Release after integration is enabled.
5. Zenodo should archive the source snapshot and assign:
   - a version DOI for `v0.3.2` or the next release,
   - a concept DOI for all versions of the repository record.

For now, do **not** add `.zenodo.json` unless Zenodo-specific fields are needed. When both `.zenodo.json` and `CITATION.cff` are present, Zenodo uses `.zenodo.json` and ignores `CITATION.cff` for GitHub release archiving. `CITATION.cff` is enough for GitHub citation UI and a straightforward Zenodo integration.

## After DOI creation

Once the PDF DOI and repository DOI exist:

1. Add DOI badges to `README.md`.
2. Add DOI identifiers to `CITATION.cff`.
3. Add DOI links to the HTML landing page if desired.
4. Consider a small follow-up commit documenting the DOI records.
