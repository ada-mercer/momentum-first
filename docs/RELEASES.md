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

### 0.4.2 — Foundations reading-route revision

- reorganized Foundations into nine sections, adding an opening reader contract
  and a compact table-based notation gateway;
- clarified the momentum-shell picture, ADMC axiom, stage/actor language and
  kinematic-modifier exposition while preserving the inertial mapping and the
  distinction between motion-related and gravitational resting-rate changes;
- aligned figure ownership, chapter documentation and section references, and
  relabeled the supporting appendix 2.4A with redirects from its earlier URLs;
- clarified the adopted appendix regularity assumption and its parity step,
  and removed a retired appendix reference without changing the equations;
- retained existing figure assets, engine scope, historical review boundaries,
  and publication pipelines; no new physical closure or independent V3 review
  is claimed.

### 0.4.1 — Foundations clock-scope corrections

- distinguished motion-related slowing from gravity's change to the resting
  cycle rate, aligning Foundations with the existing ideal-clock comparison;
- clarified the spherical momentum shell as a representation, the free-inertial
  geometry scope, and the perpendicular directional-reading condition;
- updated the Introduction's reading route and Foundations close, retaining
  conditional GR correspondence and the illustrative status of Part 0 geometry;
- aligned authoring guidance and scoped review records without claiming new
  microscopic closure, universal material clocks or independent re-verification;
- retained the existing chapter inventory, figures and publication pipelines.

### 0.4.0 — Reconciled engines and the first Part 0 geometry chapter

- integrated the revised Foundations, gravity and quantum mechanics treatments,
  including eight reconciled gravity derivation appendices and six active QM
  appendices, while preserving conditional comparisons and open closure questions;
- introduced *A First Picture of M1 Geometry*, the adopted opening chapter of
  Part 0, with seven selected, reproducible illustrations of cycles, momentum,
  translation, dilation and illustrative modes; later Part 0 chapters remain planned;
- integrated current gravity/QM figures and retained the Part 0 generation recipes
  without adding the optional 3D stack to ordinary publication CI;
- consolidated book navigation and figure execution, repaired include-aware
  references, metadata coverage and PDF font syntax, and made the release PDF
  artifact path explicit;
- strengthened source and figure validation and enforced release-tag ancestry
  on main; adoption and passing checks do not imply whole-manuscript scientific
  or human verification.

### 0.3.8 — Gravity closure-boundary recalibration

- corrected the Chapter 3 source boundary by separating the SI free-carrier
  identity from the declared interacting-source postulate and retaining its
  scoped single-shell and regular-multisector reciprocal-response obstructions;
- established the action-consistent stationary scalar packet for clock depth,
  ruler scaling, and null propagation, including exact local light speed within
  the stated carrier readout;
- replaced the former derived spatial/directional closure claim with an explicit
  conditional correspondence, preserving the scalar `kappa` versus directional
  `kappa_A` distinction and the conserved radiation-cavity discriminator;
- separated the nonstationary sector into an action-supported scalar candidate
  and a provisional directional/vector seed, without claiming complete
  interacting closure, derived `gamma = 1`, physical directional closure, or
  Kerr, TOV, tensor, strong-field, and waveform completion;
- adopted thirteen Chapter 3 derivation appendices as the trust layer for the
  carrier map, scoped obstructions, observer bookkeeping, stationary
  correspondence audits, radiation discriminator, and nonstationary boundary;
- organized derivation appendices by chapter, repaired Quarto navigation,
  provenance, and downstream paths, and aligned the book structure plan with
  Chapter 3's achieved scalar and provisional directional maturity;
- added the guarded Zenodo manuscript-publication path and focused verification
  needed for the first production manuscript DOI mint.

### 0.3.7 — Bosic-slot stage dressing and χ² expansion kinematics

- replaced the prior translation-yield Chapter 5 with a seven-section
  stage-dressing engine that separates conserved carrier content, dressed
  generator value, true-frame translation, and bound-frame measurement;
- adopted bosic-slot dressing
  `M_χ = sqrt(p_f² + χ²p²)`, deriving the `χ²` true-frame group velocity and
  the exact special-relativistic FLRW free-carrier velocity and drag law under
  the stated clean correspondence;
- preserved the lightlike law while deriving the conformal path identity,
  matched endpoint wavelength and duration relations, and the result that the
  kinematic map does not enlarge causal reach;
- added scoped hydrogenic and Newtonian realizations, including first-power
  coupling selection within the proxy Hamiltonians and standard linear matter
  growth at a supplied background history;
- replaced the two prior Chapter 5 appendices with four derivation appendices
  covering generator placement, free-carrier correspondence, lightlike
  endpoint standards, and local covariance, while keeping stage dynamics,
  gravitational source weighting, ADMC amendment, and all-sector closure open;
- aligned the Chapter 4 bridge, Chapter 5 reference lock, provenance ledger,
  manuscript status, citation metadata, and Quarto render map with the new
  package.

### 0.3.6 — Directional shell readings and release evidence

- adopted directional shell readings and `p_k^\pm = M \pm p_k/2` consistently
  across the rendered manuscript, derivation support, glossary, and canonical
  Foundations figure;
- added two captionless Preface illustrations with prompt/provenance records,
  responsive HTML floats, and PDF wrapfigure integration;
- completed a manuscript-wide conceptual review, targeted technical review of
  the load-bearing Foundations/ADMC and gravity source-map chains, and a bounded
  citation audit;
- corrected the retarded shift sign and one rendered source-notation defect in
  Derivation 3.7A, and added primary or canonical sources at the reviewed
  mathematical, empirical, historical, and correspondence claims;
- completed public contribution and human-verification provenance for all 24
  rendered units, while preserving conservative working-draft status for
  Quantum Mechanics, Space Expansion, and the derivation appendices;
- added a repository invariant requiring the provenance ledger to cover the
  complete Quarto render list without duplicate or placeholder entries.

### 0.3.5 — Repository architecture and publishing hardening

- reorganized the repository around `.github/`, `docs/`, `figures/`,
  `manuscript/`, `rendering/`, and `tooling/` while retaining root `index.qmd`
  as the Quarto book homepage;
- replaced the setup-heavy root README with a public landing page and added a
  progressive documentation map for contributors, authors, and maintainers;
- made plain `quarto render` the verified local PDF path and bound the
  pre-render status generator to the repository Python environment;
- strengthened documentation invariants, cross-reference checks, preview and
  release validation, generated-status checks, and local-artifact ignore rules.

### 0.3.4 — Foundations restructure and oriented-reading ADMC formulation

- restructured Chapter 2, Foundations, from seven to eight sections, adding a
  dedicated momentum-configuration section (§2.2) that develops fermionic
  structure, perpendicular bosonic geometry, the momentum triangle as an M1
  commitment, the shell figures, and the branch machinery before the
  conservation postulate;
- adopted the oriented-reading formulation of ADMC: each particle contributes
  one positive oriented momentum `p_k̂⊕ = M + ½ p_k` per oriented direction,
  with the reversed orientation supplying `M − ½ p_k`; this is
  equation-identical to the former simultaneous two-channel form under
  `k ↔ −k` relabeling, so no prior algebraic result changes;
- reframed Derivation 2.3A as an affine uniqueness theorem for the positive
  oriented reading (additivity, parity exchange, axis-independence, local
  invertibility, and mild regularity imply `αM ± βp`; canonical normalization
  fixes `α = 1, β = ½`), with explicit proved/not-proved scope fencing, and
  restored a correctly scoped uniqueness pointer in §2.3;
- rebuilt §2.4 around the opposite-orientation map, adding the explicit 4×4
  `T`/`T⁻¹` four-component correspondence and the invariant check
  `PᵘP_µ = M² − p² = p_f²`;
- aligned downstream glosses (gravity core terms, Derivations 3.3A/3.3B, and
  the QM bridge) to opposite-orientation-reading language with zero equation
  changes;
- documented the chapter-local `_candidates/` manuscript-candidate workflow in
  `docs/STANDARDS.md`;
- verified the package through the independent review sequence recorded under
  `exchange/reviews/manuscript/` on 2026-07-14 and 2026-07-15.

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
- added directional momentum-coupling density `C_ij` as the second transport
  moment in Chapter 3 source accounting. The achieved stationary
  scalar-plus-shift map remains driven by `M` and `P_i`, with independent
  `C_ij` field effects bracketed; `C_ij` is restored in the stress-energy
  correspondence as `T^{ij}=c C_ij`;
- recorded the two named premises (SI source identification, P2 comoving-cycle
  readout) with their independent checks as the remaining hardening targets;
- promoted the derivation-check scripts `check_carrier_source_map.py` and
  `check_depth_stretch_pipeline.py` into `tooling/scripts/`.

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
- run repository tests, cross-reference checks, and generated-status checks
- rebuild registered figures and reject canonical-output drift
- verify the repo still renders cleanly in CI through the same PDF-first path used by releases

This workflow is **manual only** (`workflow_dispatch`).
It does **not** create a release.

### 3. Tag-triggered release

Workflow: `.github/workflows/release-book.yml`

Purpose:
- verify dependencies
- run repository tests, cross-reference checks, and generated-status checks
- rebuild registered figures and reject canonical-output drift
- verify the pushed tag matches `VERSION`
- render the PDF book
- attach `Momentum-First.pdf` to a GitHub Release
- when DOI setup is complete, publish that exact PDF as a version of the
  canonical Zenodo manuscript record

This workflow runs only when a tag matching `v*` is pushed.
That is the core safeguard against frequent accidental releases.

## Release procedure

1. Ensure the working tree contains only the intended milestone state; exclude
   `_book/`, local environments, caches, review folders, and generated PDF/SVG
   companions that are not explicitly canonical.
2. Choose the milestone version and update all release metadata together:
   `VERSION`, the `version` and `date-released` fields in `CITATION.cff`, and
   the milestone notes in this file.
3. Regenerate derived status when needed, then run the local release gate in a
   clean accepted checkout (use an isolated snapshot while authoring is dirty):

```bash
.venv/bin/python tooling/scripts/build_manuscript_status.py --check
.venv/bin/python tooling/scripts/validate.py --publication
quarto render --profile pdf
quarto render --profile html --output-dir _html-book
```

4. Inspect the final diff, confirm `VERSION` and `CITATION.cff` agree, and commit
   the release state. Do not commit `_book/` or a local `Momentum-First.pdf`.
5. Push the reviewed main commit without tags. Run **Validate Repo** and
   **Render Book Preview** against that exact commit and inspect their results.
   A main push also deploys HTML with the existing latest-release PDF.
6. Create and push only the annotated release tag matching `VERSION`:

```bash
git checkout main
git tag -a v0.4.0 VERIFIED_COMMIT -m "Release v0.4.0"
git push origin refs/tags/v0.4.0
```

7. GitHub Actions will rerun the release gate and render the book PDF.
8. The workflow copies the rendered PDF to the stable release asset name
   `Momentum-First.pdf`, attaches it to the GitHub Release, and thereby updates
   the README's latest-PDF link target.
9. When `ZENODO_MANUSCRIPT_CONCEPT_ID` is configured, the separate
   `zenodo-manuscript` job publishes or verifies the exact release PDF and writes
   the concept DOI, version DOI, and SHA-256 checksum to the Actions summary.
   Zenodo's native GitHub integration separately archives the tagged source.
10. Manually dispatch **Deploy Book Site** if the Pages-hosted PDF should
   immediately mirror the newly published release PDF.

The existing DOI setup is recorded in [`doi/README.md`](doi/README.md).
Subsequent releases reuse those families and require no manual Zenodo upload.
If DOI publication fails, rerun the failed job rather than creating another
record or draft manually.

## After a release

Move `VERSION` forward to the next development value if desired, for example:
- `0.1.1-dev`
- `0.2.0-dev`

That makes it clear the repo has moved beyond the last tagged milestone.

## Notes

- Releases are intended to be **deliberate and relatively rare**.
- The default mode of the repo is ongoing work on `main`, not continuous release publishing.
- The book PDF is a release artifact. Do not commit `_book/` or generated PDF files to the repository during ordinary development.
- The manuscript concept DOI is the general citation target; release-specific
  citations use the corresponding manuscript version DOI. The source DOI family
  is provenance, not the preferred book citation.
- If the project later needs public release cadence, the policy can be revisited intentionally.
