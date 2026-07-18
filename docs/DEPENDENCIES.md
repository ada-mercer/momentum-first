# Dependencies

This repository has three dependency modes. The full release toolchain is deliberately broad because the book targets PDF/HTML Quarto output and mixed-language figure/table support. Most review and lint tasks do **not** require the full stack.

## Modes

### 1. Minimal / lint-only

Purpose:
- validate repo structure
- check manuscript paths and cross-references
- run lightweight Python tests
- compile repo scripts

Typical requirements:
- **Python 3**
- **PyYAML**
- **pytest** when running tests

Commands:

```bash
python3 tooling/scripts/check_dependencies.py --mode minimal
python3 tooling/scripts/check_crossrefs.py
python3 -m py_compile tooling/scripts/*.py tooling/tests/*.py
pytest tooling/tests/test_repo_integrity.py
```

### 2. Figure/dev

Purpose:
- validate and build registered figures
- work on figure/table automation

Typical requirements:
- minimal dependencies
- **numpy** — numerical support
- **matplotlib** — plotting
- **pandas** — table/data handling
- **Rscript** with `ggplot2`, `svglite`, and `ragg` — required by registered
  `.R` figures and their canonical raster/vector devices

Commands:

```bash
python3 tooling/scripts/check_dependencies.py --mode figures
python3 tooling/scripts/build_figures.py
```

### 3. Full render / release

Purpose:
- render the Quarto book
- validate PDF output
- run the release workflow locally or in CI

Typical requirements:
- figure/dev dependencies
- **Quarto CLI** — book rendering and project management
- **R** with `knitr`, `rmarkdown`, `ggplot2`, `svglite`, and `ragg` — Quarto R
  execution and registered-figure support
- **Julia** — Quarto Julia execution support
- **TeX/LaTeX toolchain** (`latexmk`, `biber`, `texlive`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-science`, `texlive-luatex`) — PDF/book output
- **graphviz** — diagrams if needed later
- **inkscape** — vector asset conversion
- **librsvg2-bin** — SVG conversion helpers

Commands:

```bash
python3 tooling/scripts/check_dependencies.py --mode full
quarto render
```

The plain command is the supported local default and produces the PDF book
because `_quarto.yml` sets the default profile to `pdf`. Use
`quarto render --profile html` when you explicitly want the web edition;
`quarto render --profile pdf` remains an equivalent explicit PDF command.

## Ubuntu/Debian installer

For Ubuntu/Debian-like systems, use:

```bash
bash tooling/ci/install-ubuntu.sh
```

The installer is idempotent and prefers existing system packages, but will install user-local copies of `quarto` and `julia` under `~/.local/opt` / `~/.local/bin` when they are not already available. It also creates or updates the repo Python virtual environment from `tooling/ci/requirements.txt`.

By default, the installer ensures `~/.local/bin` is added to `~/.profile` for future local shells. For CI or review environments where profile mutation is undesirable, use either flag:

```bash
bash tooling/ci/install-ubuntu.sh --ci
bash tooling/ci/install-ubuntu.sh --no-profile-edit
```

GitHub workflows use `--ci`.

## System dependencies installed by `tooling/ci/install-ubuntu.sh`

- **git** — version control
- **curl** — installer/bootstrap support
- **wget**, **gnupg**, **software-properties-common** — package/bootstrap support
- **Python 3 + venv + pip** — local automation scripts and tests
- **R** — Quarto execution engine support for R-based chapters, notebooks, or analysis snippets
- **Julia** — Quarto execution engine support for Julia-based chapters, notebooks, or analysis snippets
- **Quarto CLI** — installed locally when absent
- **TeX/LaTeX toolchain** — PDF/book output
- **Graphviz**, **Inkscape**, **librsvg2-bin** — diagram/vector conversion support
- **Ubuntu build toolchain/dev headers** (`build-essential`, `gfortran`, `libcurl4-openssl-dev`, `libfontconfig1-dev`, `libfribidi-dev`, `libgit2-dev`, `libharfbuzz-dev`, `libjpeg-dev`, `libpng-dev`, `libssl-dev`, `libtiff-dev`, `libuv1-dev`, `libx11-dev`, `libxml2-dev`, `libxt-dev`) — needed so common R/Python packages compile cleanly on a fresh system

## Python dependencies

Defined in `tooling/ci/requirements.txt` and `tooling/ci/environment.yml`:
- Python `3.14` is the canonical CI figure-rendering runtime;
- `numpy`
- `matplotlib`
- `pandas`
- `Pillow`
- `PyYAML`
- `jupyter`
- `nbformat`
- `pytest`
- `ruff`

Raster-sensitive Python packages and their Matplotlib dependency chain are
pinned in `tooling/ci/requirements.txt` so clean-runner figure regeneration is
byte-stable with the committed canonical PNGs.

A smaller lint-only set is documented in `tooling/ci/requirements-minimal.txt`.

## Intentionally excluded for now

These are **not** baseline dependencies yet:
- the heavy external simulation/rendering library
- the broader R package stack beyond the current Quarto/figure baseline
  (`knitr`, `rmarkdown`, `ggplot2`, `svglite`, `ragg`)
- Julia package environment setup beyond installing Julia itself
- browser automation dependencies

Those can be added once the manuscript or figure pipeline actually needs them.

## R library path

Local R package installs use `R_LIBS_USER` when available. The repo provides `.Renviron.example` with the recommended user-local path:

```text
~/.local/share/R/%p-library/%v
```

Copy it to `.Renviron` for local work if needed. `.Renviron` itself is ignored because it is machine-local configuration; `tooling/ci/install-ubuntu.sh` creates it automatically when absent.
