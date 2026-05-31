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

## Workflows

### 1. GitHub Pages site deploy

Workflow: `.github/workflows/deploy-book-site.yml`

Purpose:
- render the HTML book with `quarto render --profile html`
- publish the site to GitHub Pages
- include the latest release PDF in the site artifact so Quarto's PDF download link resolves

This workflow runs on relevant pushes to `main`, manual dispatch, and published releases.

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
