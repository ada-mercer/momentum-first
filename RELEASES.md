# Release Policy

This repository uses **infrequent, milestone-based releases**.
Releases are for meaningful manuscript states, not routine development churn.

## Policy

- Do **not** create a release for ordinary merges, typo fixes, or minor housekeeping.
- Create a release only when the manuscript reaches a durable milestone worth preserving, sharing, or citing.
- Releases are created from **annotated git tags** on `main`.
- GitHub Releases are produced by CI only when a tag matching `v*` is pushed.
- The tag must match the version in the `VERSION` file exactly, minus the leading `v`.

Examples:
- `VERSION` = `0.2.0`
- release tag = `v0.2.0`

## When to release

Good release triggers:
- a new part/chapter cluster reaches a stable draft
- a major notation or structure lock is complete
- a figure pipeline milestone becomes reproducible
- a manuscript snapshot is worth archiving or sharing with others
- a pre-public milestone should be frozen before larger refactors

Bad release triggers:
- routine maintenance commits
- isolated typo fixes
- dependency bumps without manuscript significance
- unfinished exploratory states

## Versioning approach

Use milestone-oriented semantic-style versions:

- `v0.x.y` — private, evolving manuscript
- `v1.0.0` — first public/citable edition-level release

Suggested interpretation:
- **major** = major edition or major structural/conceptual milestone
- **minor** = substantial manuscript milestone
- **patch** = corrective cleanup to an already meaningful release

## Milestone notes

### 0.3.3 — Gravity derived-pipeline and appendix restructure

- promoted the stationary gravity source layer to a native carrier source map:
  `mathcal J_k^pm` is the density of `M pm p_k/2`, giving
  `mathcal M_k = varrho` on every axis and `mathcal P_i = j_i` with no imported
  pressure, stress, or radiation apportioning term;
- scoped the pressure/radiation divergence honestly: total source weight agrees
  for isolated stationary systems and the full exterior agrees for spherical
  sources, while aspherical pressure/stress multipoles become a Tier 3
  discriminator at fractional order `p/rho c^2`;
- derived the two-aspect deformation: clock depth and isotropic spatial stretch as
  one deformation, with weak-field trace coefficient `sigma = 1` from the
  comoving-cycle readout of the M1 time stance;
- derived the shift coefficient `kappa_A = 2(1+sigma) = 4` by boost consistency,
  retiring the calibration posture; the frame-drag audit is re-statused as the
  endpoint validation of the derived value;
- added weak-field stationary claims: PPN `gamma = 1`, standard light bending,
  standard Shapiro delay;
- rewrote Appendix 3.3A as the carrier-map derivation; added Appendix 3.3B
  (null-probe diagnostic and no-go), Appendix 3.3C (momentum-manifestation
  dictionary, no vacuum row), Appendix 3.4B (depth = stretch), and Appendix 3.6C
  (boost consistency);
- strengthened the Chapter 3 source-to-field pipeline: the six ADMC source
  channels now explicitly reduce by even/odd projection to the four-component
  stationary deformation package `(theta_0, theta_i)`, with Appendix 3.4A
  carrying the compact projection lemma while preserving SI/P2 boundaries;
- recorded the two named premises (SI source identification, P2 comoving-cycle
  readout) with their independent checks as the remaining hardening targets;
- promoted the derivation-check scripts `check_carrier_source_map.py` and
  `check_depth_stretch_pipeline.py` into `scripts/`.

## Workflows

### 1. GitHub Pages site deploy

Workflow: `.github/workflows/deploy-book-site.yml`

Purpose:
- render the HTML book with `quarto render --profile html`
- publish the site to GitHub Pages
- include the latest release PDF in the site artifact so Quarto's PDF download link resolves

This workflow runs on relevant pushes to `main` and manual dispatch.

Because GitHub Pages environment protection may reject tag/release-triggered deployments, release publication should be followed by a manual **Deploy Book Site** dispatch when the site must pick up a newly published release PDF.

### 2. Manual preview render

Workflow: `.github/workflows/render-book.yml`

Purpose:
- produce a manual PDF preview artifact before deciding to tag a release
- verify the repo still renders cleanly in CI through the same PDF-first path used by releases

This workflow is **manual only** (`workflow_dispatch`).
It does **not** create a release.

### 3. Tag-triggered release

Workflow: `.github/workflows/release-book.yml`

Purpose:
- verify dependencies
- verify the pushed tag matches `VERSION`
- render the PDF book
- attach `Momentum-First.pdf` to a GitHub Release

This workflow runs only when a tag matching `v*` is pushed.
That is the core safeguard against frequent accidental releases.

## Release procedure

1. Ensure `main` contains the desired milestone state.
2. Update `VERSION` from a development value (for example `0.1.0-dev`) to a release value (for example `0.1.0`).
3. Commit that change.
4. Optionally run a manual preview via the **Render Book Preview** workflow.
5. Create and push an annotated tag:

```bash
git checkout main
git pull --ff-only
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin main --follow-tags
```

6. GitHub Actions will render the book PDF.
7. The workflow copies the rendered PDF to the stable release asset name `Momentum-First.pdf`, attaches it to the GitHub Release, and thereby updates the README's latest-PDF link target.
8. Manually dispatch **Deploy Book Site** if the Pages-hosted PDF should immediately mirror the newly published release PDF.

## After a release

Move `VERSION` forward to the next development value if desired, for example:
- `0.1.1-dev`
- `0.2.0-dev`

That makes it clear the repo has moved beyond the last tagged milestone.

## Notes

- Releases are intended to be **deliberate and relatively rare**.
- The default mode of the repo is ongoing work on `main`, not continuous release publishing.
- The book PDF is a release artifact. Do not commit `_book/` or generated PDF files to the repository during ordinary development.
- If the project later needs public release cadence, the policy can be revisited intentionally.
