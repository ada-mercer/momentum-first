# Manuscript source

This directory contains the canonical book source owned by the manuscript.
Quarto configuration remains at the repository root, and root `index.qmd`
remains there because it is the book homepage.

## Layout

- [`chapters/`](chapters/README.md) — front matter and the main chapter spine
- [`appendices/derivations/`](appendices/derivations/README.md) — long technical
  derivations cited from the main text
- [`appendices/examples/`](appendices/examples/README.md) — worked examples and
  pedagogical support
- `backmatter/` — generated or maintained closing material included by Quarto
- `metadata/` — structured manuscript status data
- `bibliography.bib` — bibliography database
- `glossary.yml` — glossary source
- `references.qmd` — rendered references page

The canonical rendered order is [`../_quarto.yml`](../_quarto.yml), not the
filesystem listing. A source file is part of the rendered book only when it is
listed there or included from a listed wrapper.

## Authoring rules

- Rendered chapter wrappers are named `index.qmd` and start with a level-one
  heading.
- Chapter-local section files use `NN-short-slug.qmd` names and normally start
  with a level-two heading.
- Keep manuscript candidates in chapter-local `_candidates/` directories and
  displaced working copies in `_old/`; both are local, Git-ignored review areas.
- Put long supporting algebra in the derivations appendix rather than breaking
  the main narrative.
- Update [`chapters/README.md`](chapters/README.md) and
  [`../_quarto.yml`](../_quarto.yml) together when the rendered structure
  intentionally changes.

Project-wide contribution and verification rules live in
[`../docs/STANDARDS.md`](../docs/STANDARDS.md) and
[`../docs/VERIFICATION_POLICY.md`](../docs/VERIFICATION_POLICY.md). Prose guidance
lives in [`../docs/STYLE_FLOW_GUIDE.md`](../docs/STYLE_FLOW_GUIDE.md).

## Verification

For path, include, figure, or cross-reference changes, run:

```bash
python3 tooling/scripts/check_crossrefs.py
```

Run Quarto from the repository root when rendered structure, includes,
citations, figures, or format behavior may have changed. See
[`../tooling/README.md`](../tooling/README.md) for the available validation and
rendering routes.
