# Momentum First

[![Latest release](https://img.shields.io/github/v/release/ada-mercer/momentum-first?label=release)](https://github.com/ada-mercer/momentum-first/releases/latest)
[![Latest PDF](https://img.shields.io/badge/PDF-latest-blue)](https://github.com/ada-mercer/momentum-first/releases/latest/download/Momentum-First.pdf)
[![Validate Repo](https://github.com/ada-mercer/momentum-first/actions/workflows/lint-content.yml/badge.svg)](https://github.com/ada-mercer/momentum-first/actions/workflows/lint-content.yml)
[![Deploy Book Site](https://github.com/ada-mercer/momentum-first/actions/workflows/deploy-book-site.yml/badge.svg)](https://github.com/ada-mercer/momentum-first/actions/workflows/deploy-book-site.yml)
[![License: CC BY-NC-SA + MIT](https://img.shields.io/badge/license-CC--BY--NC--SA%20%2B%20MIT-lightgrey.svg)](LICENSE.md)

*Momentum First* is an open, evolving research manuscript that asks how far
physics can be rebuilt when momentum conservation is taken as the primary
starting point.

## Read the book

- [Read the HTML book](https://ada-mercer.github.io/momentum-first/)
- [Download the latest PDF](https://github.com/ada-mercer/momentum-first/releases/latest/download/Momentum-First.pdf)
- [Browse milestone releases](https://github.com/ada-mercer/momentum-first/releases)

The HTML book is published through GitHub Pages. The PDF is a release artifact
and is not committed to the repository.

## What the framework develops

- **One conservation structure for energy and momentum.** M1 treats energy and
  ordinary momentum as two readings of the same underlying structure: the
  total amount of momentum present and the net amount in a given direction.
- **Gravity sourced by momentum.** Momentum shapes gravity's strength and form,
  including its effects on clocks. Organized momentum flow produces rotational
  effects such as frame-dragging.
- **Time as a measure of physical change.** Clocks are physical cycles. When a
  clock slows, M1 looks for a change in that cycle rather than a change in time
  itself.
- **A bridge to quantum mechanics.** The momentum picture leads to the familiar
  Dirac equation, recovers the Schrödinger limit, and connects quantum behavior
  to the same account of gravity.
- **Cosmic expansion without momentum loss in flight.** M1 explores whether
  redshift and stretched signal durations can arise because momentum produces
  displacement differently as the universe evolves.

The foundations and stationary-gravity chapters are the manuscript's most
mature parts. The quantum and expansion chapters remain working bridges: they
establish explicit connections and consequences while leaving broader theory
and observational completion open.

## Repository guide

The repository is organized by responsibility:

- [`manuscript/`](manuscript/README.md) — book source, bibliography, metadata,
  appendices, and back matter
- [`figures/`](figures/README.md) — figure sources, registries, build outputs, and
  specialist figure documentation
- [`rendering/`](rendering/README.md) — HTML and PDF presentation assets
- [`docs/`](docs/README.md) — contributor navigation, standards, policy, and
  project reference material
- [`tooling/`](tooling/README.md) — validation, generation, and environment tools
- [`.github/`](.github/WORKFLOWS.md) — continuous integration, previews,
  publishing, and release automation

The root [`index.qmd`](index.qmd) is intentionally retained as the Quarto book
homepage. The full rendered order is defined by [`_quarto.yml`](_quarto.yml).

Start with the [project documentation map](docs/README.md) to contribute,
author manuscript material, rebuild figures, verify changes, or maintain a
release.

## Status, citation, and license

This is a working manuscript under active development. Cite a specific
[GitHub release](https://github.com/ada-mercer/momentum-first/releases) when a
stable version matters. Machine-readable citation metadata lives in
[`CITATION.cff`](CITATION.cff), and contribution and verification records live
under [`docs/provenance/`](docs/provenance/README.md).

Manuscript text, figures, and rendered outputs are licensed under
**CC BY-NC-SA 4.0**. Code, scripts, tests, and CI configuration are licensed
under **MIT**. See [`LICENSE.md`](LICENSE.md).
