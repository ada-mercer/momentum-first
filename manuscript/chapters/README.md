# Chapters

This directory holds the book front matter and main rendered body.

## Current rendered structure

The canonical rendered-structure map is `_quarto.yml`.

Current folder policy:
- top-level chapter folders are grouped by rendered part/tier;
- each chapter folder keeps the global chapter number and chapter slug;
- files inside a chapter use only local section numbers plus slugs;
- each rendered chapter is represented by an `index.qmd` wrapper listed in `_quarto.yml`.

Current layout:
- `00-front-matter/00-preface/index.qmd` — unnumbered Preface wrapper.
- `01-tier-1-foundations/01-introduction/index.qmd` — Chapter 1, Introduction.
- `01-tier-1-foundations/02-foundations/index.qmd` — Chapter 2, Foundations.
- `02-tier-2-engines/03-gravity-and-structured-spacetime/index.qmd` — Chapter 3, Gravity and Structured Spacetime.
- `02-tier-2-engines/04-quantum-mechanics/index.qmd` — Chapter 4, Quantum Mechanics in Momentum Language.
- `02-tier-2-engines/05-expansion/index.qmd` — Chapter 5, Space Expansion as Translation Yield.

## Wrapper and section-file policy

Use:
- one tier/front-matter directory per major rendered division;
- one chapter directory per rendered book chapter;
- `index.qmd` as the rendered chapter wrapper;
- local section files named `NN-short-slug.qmd` inside each chapter directory.

Rendered `index.qmd` files listed directly in `_quarto.yml` must start with a `#` chapter title.
Included section files normally start with `##`, because they are sections inside the chapter wrapper.
Use `###` for subsections.

Do not list individual section files directly in `_quarto.yml` unless the book structure is intentionally changed.

## Naming examples

```text
manuscript/chapters/01-tier-1-foundations/02-foundations/
  index.qmd
  01-core-terms-and-variables.qmd
  02-the-momentum-configuration.qmd
  03-admc.qmd
  04-invertible-mapping.qmd

manuscript/chapters/02-tier-2-engines/04-quantum-mechanics/
  index.qmd
  01-quantum-mechanics-after-gravity.qmd
  04-stationary-gravity-and-the-operator-mg.qmd
```

The chapter number belongs to the chapter folder. The section number belongs to the section file.
