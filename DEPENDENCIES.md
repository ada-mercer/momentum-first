# Dependencies

This repository currently uses a deliberately modest dependency baseline.
The goal is to support Quarto rendering, PDF output, lightweight figure/table orchestration, and repository validation without pulling the heavy scientific engine into the manuscript repo.

## System dependencies

### Required
- **Quarto CLI** — book rendering and project management
- **Python 3 + venv + pip** — local automation scripts and tests
- **R** — Quarto execution engine support for R-based chapters, notebooks, or analysis snippets
- **Julia** — Quarto execution engine support for Julia-based chapters, notebooks, or analysis snippets
- **TeX/LaTeX toolchain** (`latexmk`, `biber`, `texlive`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-science`, `texlive-luatex`) — PDF/book output
- **Ubuntu build toolchain/dev headers** (`build-essential`, `gfortran`, `libcurl4-openssl-dev`, `libfontconfig1-dev`, `libfribidi-dev`, `libgit2-dev`, `libharfbuzz-dev`, `libjpeg-dev`, `libpng-dev`, `libssl-dev`, `libtiff-dev`, `libx11-dev`, `libxml2-dev`, `libxt-dev`) — needed so common R packages compile cleanly on a fresh system

### Recommended baseline utilities
- **git** — version control
- **curl** — installer/bootstrap support
- **wget**, **gnupg**, **software-properties-common** — package/bootstrap support
- **graphviz** — diagrams if needed later
- **inkscape** — vector asset conversion
- **librsvg2-bin** — SVG conversion helpers

## Python dependencies

Defined in `ci/requirements.txt` and `ci/environment.yml`:
- `numpy` — lightweight numerical support for figure/table scripts
- `matplotlib` — plotting
- `pandas` — table/data handling
- `PyYAML` — registry/config processing
- `jupyter` — notebook-backed Quarto execution if needed
- `nbformat` — notebook inspection/validation support
- `pytest` — repo health checks
- `ruff` — fast Python linting

## Intentionally excluded for now

These are **not** baseline dependencies yet:
- the heavy external simulation/rendering library
- the broader R package stack beyond minimal Quarto support (`knitr`, `rmarkdown`)
- Julia package environment setup beyond installing Julia itself
- browser automation dependencies
- custom Quarto filters beyond future need

Those can be added once the manuscript or figure pipeline actually needs them.

## R library path

This repo uses a user-local R package library via `.Renviron`:

```text
~/.local/share/R/%p-library/%v
```

That avoids requiring sudo for basic Quarto-related R packages.

## Install

For Ubuntu/Debian-like systems, use:

```bash
bash ci/install-ubuntu.sh
```

The installer is idempotent and prefers existing system packages, but will install user-local copies of `quarto` and `julia` under `~/.local/opt` / `~/.local/bin` when they are not already available. It also ensures `~/.local/bin` is added to `~/.profile` for future shells.
