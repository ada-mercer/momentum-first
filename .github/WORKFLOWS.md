# GitHub automation

The workflows in `workflows/` validate, preview, publish, and release the book.
Their triggers are intentionally separated so ordinary development does not
become a release operation.

| Workflow | Role | Trigger |
|---|---|---|
| `build-ci-image.yml` | build, attest, and publish the reusable figure/PDF environment to GHCR | relevant push to `main` or manual dispatch |
| `lint-content.yml` | repository tests, cross-reference validation, and generated-status check | pull request or manual dispatch |
| `build-figures.yml` | registered figure rebuild and canonical-output drift check | manual dispatch |
| `render-book.yml` | release-equivalent validation and PDF preview artifact | manual dispatch |
| `deploy-book-site.yml` | HTML render and GitHub Pages deployment | relevant push to `main` or manual dispatch |
| `release-book.yml` | release-equivalent validation, version check, PDF render, GitHub Release asset, and configured manuscript-DOI publication | `v*` tag push |

The workflow files themselves are the trigger and command authority. Keep their
paths aligned with [`../tooling/`](../tooling/README.md),
[`../manuscript/`](../manuscript/README.md),
[`../rendering/`](../rendering/README.md), and
[`../figures/`](../figures/README.md).

Figure and PDF jobs consume the project image by immutable registry digest.
The source image tag identifies its defining commit, but tags are never used as
the production trust boundary. See
[`../tooling/ci/image/README.md`](../tooling/ci/image/README.md) for the update
and validation procedure.

The release workflow's `zenodo-manuscript` job runs only after the one-time DOI
setup has supplied the repository variable `ZENODO_MANUSCRIPT_CONCEPT_ID`. It
uses the protected `zenodo-production` environment and its `ZENODO_TOKEN`
secret. Zenodo's native GitHub integration separately archives the tagged
source release. See [`../docs/doi/README.md`](../docs/doi/README.md).

See [`../docs/STANDARDS.md`](../docs/STANDARDS.md) for CI policy and
[`../docs/RELEASES.md`](../docs/RELEASES.md) before changing tags, versions,
release assets, or publishing behavior.
