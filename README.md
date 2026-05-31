# momentum-first

[![Latest release](https://img.shields.io/github/v/release/ada-mercer/momentum-first?label=release)](https://github.com/ada-mercer/momentum-first/releases/latest)
[![Latest PDF](https://img.shields.io/badge/PDF-latest-blue)](https://github.com/ada-mercer/momentum-first/releases/latest/download/Momentum-First.pdf)
[![Validate Repo](https://github.com/ada-mercer/momentum-first/actions/workflows/lint-content.yml/badge.svg)](https://github.com/ada-mercer/momentum-first/actions/workflows/lint-content.yml)
[![Deploy Book Site](https://github.com/ada-mercer/momentum-first/actions/workflows/deploy-book-site.yml/badge.svg)](https://github.com/ada-mercer/momentum-first/actions/workflows/deploy-book-site.yml)
[![License: CC BY-NC-SA + MIT](https://img.shields.io/badge/license-CC--BY--NC--SA%20%2B%20MIT-lightgrey.svg)](LICENSE.md)

Quarto-first manuscript repository for the *Momentum First* book.

## Read the book

- [Read the HTML book](https://ada-mercer.github.io/momentum-first/)
- [Download the latest PDF](https://github.com/ada-mercer/momentum-first/releases/latest/download/Momentum-First.pdf)
- [View releases](https://github.com/ada-mercer/momentum-first/releases)

The HTML book is published with GitHub Pages. The PDF is published as a GitHub Release artifact, not committed to the repository.

## Current scope

As of `v0.3.1`, this is an active early manuscript rather than an empty scaffold. The repository contains:

- front matter and Preface
- Tier 1 foundations material
- Tier 2 engines for gravity, quantum mechanics, and expansion
- derivation appendices supporting the gravity and expansion chapters
- Quarto PDF/HTML styling, release automation, standards, and validation scripts

The manuscript is still pre-1.0 and evolving, but the repo structure, release path, and verification posture are now established.

## Working principles

- Quarto-first book workflow
- Reproducible figures and tables
- External heavy scientific code kept outside the manuscript repo
- Quarto execution should be possible across Python, R, and Julia when full rendering needs it
- Contribution workflow follows `STANDARDS.md`: direct-to-main is allowed for Arne/Ada during initial construction; pull requests are the default for external or post-v1 contribution.

## Dependency modes

The full release toolchain is intentionally broad, but not every task needs it.

### Minimal / lint-only

Use this for source checks that do not render the book or rebuild figures.

Typical requirements:
- Python 3
- `PyYAML`
- `pytest` if running the pytest suite

Useful commands:

```bash
python3 scripts/check_dependencies.py --mode minimal
python3 scripts/check_crossrefs.py
python3 -m py_compile scripts/*.py tests/*.py
pytest tests/test_repo_integrity.py
```

### Figure/dev

Use this when checking or rebuilding registered figures.

Typical requirements:
- minimal dependencies
- `numpy`, `matplotlib`, `pandas`
- `Rscript` for R-backed figures

```bash
python3 scripts/check_dependencies.py --mode figures
python3 scripts/build_figures.py
```

### Full render / release

Use this before milestone releases or when validating PDF output.

Typical requirements:
- Quarto CLI
- Python stack from `ci/requirements.txt`
- R with `knitr` / `rmarkdown`
- Julia
- LaTeX/PDF toolchain
- Graphviz, Inkscape, and SVG conversion helpers

```bash
python3 scripts/check_dependencies.py --mode full
quarto render --profile pdf
```

See `DEPENDENCIES.md` for the full dependency baseline and Ubuntu/Debian installer.

## Render locally

The shared book structure lives in `_quarto.yml`. The default Quarto profile is PDF, so a plain render produces the PDF book:

```bash
quarto render
```

HTML remains available as an explicit optional profile:

```bash
quarto render --profile html
```

Use the default PDF render for release checks and the HTML profile for fast reading/review.

## Citation / status

This is a pre-1.0 working manuscript. For now, cite the latest GitHub Release unless a more formal edition is provided.

## Releases

This repo uses **infrequent, milestone-based releases** rather than frequent publish churn.
See `RELEASES.md` for the release policy, workflows, and tagging procedure.

## License

This repository uses a split license. Manuscript text, figures, and rendered outputs are licensed under **CC BY-NC-SA 4.0**; code, scripts, tests, and CI configuration are licensed under **MIT**. See `LICENSE.md`.
