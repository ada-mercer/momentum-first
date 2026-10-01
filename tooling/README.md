# Tooling

This directory contains repository-local automation. Run commands from the
repository root so paths agree with Quarto, manifests, and CI.

## Layout

- `scripts/` — dependency, cross-reference, generated-status, table, figure,
  print-asset, DOI-release, and targeted derivation automation
- `tests/` — pytest checks for dependencies, repository integrity, and
  documentation invariants
- `ci/` — environment specifications and the Ubuntu/Debian bootstrap script

## Common checks

For a lightweight source and documentation pass:

```bash
.venv/bin/python tooling/scripts/validate.py
```

For registered figures:

```bash
python3 tooling/scripts/check_dependencies.py --mode figures
python3 tooling/scripts/build_figures.py
```

For a full rendering environment and book render:

```bash
python3 tooling/scripts/check_dependencies.py --mode full
quarto render
```

The plain command uses the default `pdf` profile declared in `_quarto.yml`.
Use `quarto render --profile html` for the web edition; an explicit
`quarto render --profile pdf` is equivalent to the plain command. Dependency
details and the supported setup modes live in
[`../docs/DEPENDENCIES.md`](../docs/DEPENDENCIES.md).
Figure-specific generation and geometry3d commands live in
[`../figures/README.md`](../figures/README.md).

`validate.py` is shared by local checks, validation CI and Pages. It checks
dependencies, repository tests, the rendered include/link/asset closure and the
generated status table without rewriting that table. `--publication` also
rebuilds registered figures and checks reproducibility; it requires a clean
`figures/build/` baseline and stops before generation when source validation
fails. Use an isolated accepted snapshot for publication rehearsal, not a dirty
authoring checkout. Rendering and publication are separate operations.

The maintained book order is `book.chapters` in `_quarto.yml`; Quarto derives
render targets and the sidebar. Do not add a duplicate `project.render` or HTML
sidebar file list. Templates, candidates and unlisted QMDs are not promoted by
directory scanning. Review/provenance facts remain independently maintained and
are checked against the book order, never generated as scientific approvals.

Check the CI image copies with `python3 tooling/scripts/sync_ci_image.py`.
The [image update procedure](ci/image/README.md) covers deliberate digest changes.

## Maintenance boundary

Scripts should encode repeatable repository operations, while tests should
protect stable qualities such as valid paths, resolvable documentation links,
manifest integrity, and supported release behavior. Avoid tests that require a
README to repeat a current version string or an incidental command merely to
pass.

GitHub workflow roles and triggers are summarized in
[`../.github/WORKFLOWS.md`](../.github/WORKFLOWS.md). Project-wide automation and
generated-output policy lives in [`../docs/STANDARDS.md`](../docs/STANDARDS.md).
