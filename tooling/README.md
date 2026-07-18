# Tooling

This directory contains repository-local automation. Run commands from the
repository root so paths agree with Quarto, manifests, and CI.

## Layout

- `scripts/` — dependency, cross-reference, generated-status, table, figure,
  print-asset, and targeted derivation checks
- `tests/` — pytest checks for dependencies, repository integrity, and
  documentation invariants
- `ci/` — environment specifications and the Ubuntu/Debian bootstrap script

## Common checks

For a lightweight source and documentation pass:

```bash
python3 tooling/scripts/check_dependencies.py --mode minimal
python3 tooling/scripts/check_crossrefs.py
python3 -m py_compile tooling/scripts/*.py tooling/tests/*.py
pytest tooling/tests/test_repo_integrity.py
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

## Maintenance boundary

Scripts should encode repeatable repository operations, while tests should
protect stable qualities such as valid paths, resolvable documentation links,
manifest integrity, and supported release behavior. Avoid tests that require a
README to repeat a current version string or an incidental command merely to
pass.

GitHub workflow roles and triggers are summarized in
[`../.github/WORKFLOWS.md`](../.github/WORKFLOWS.md). Project-wide automation and
generated-output policy lives in [`../docs/STANDARDS.md`](../docs/STANDARDS.md).
