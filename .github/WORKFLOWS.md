# GitHub automation

The workflows in `workflows/` validate, preview, publish, and release the book.
Their triggers are intentionally separated so ordinary development does not
become a release operation.

| Workflow | Role | Trigger |
|---|---|---|
| `lint-content.yml` | repository tests, cross-reference validation, and generated-status check | pull request or manual dispatch |
| `build-figures.yml` | registered figure rebuild and canonical-output drift check | manual dispatch |
| `render-book.yml` | release-equivalent validation and PDF preview artifact | manual dispatch |
| `deploy-book-site.yml` | HTML render and GitHub Pages deployment | relevant push to `main` or manual dispatch |
| `release-book.yml` | release-equivalent validation, version check, PDF render, and GitHub Release asset | `v*` tag push |

The workflow files themselves are the trigger and command authority. Keep their
paths aligned with [`../tooling/`](../tooling/README.md),
[`../manuscript/`](../manuscript/README.md),
[`../rendering/`](../rendering/README.md), and
[`../figures/`](../figures/README.md).

See [`../docs/STANDARDS.md`](../docs/STANDARDS.md) for CI policy and
[`../docs/RELEASES.md`](../docs/RELEASES.md) before changing tags, versions,
release assets, or publishing behavior.
