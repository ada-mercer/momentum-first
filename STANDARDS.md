# Momentum First Standards

Status: working standard
Purpose: define the project standards that cleanup, CI, authoring, verification, and release sessions should uphold.

This document is the standards entrypoint. More detailed policy may live in specialized files, but cleanup/commit sessions should start here and follow the referenced documents when relevant.

## 1. Contribution authority and workflow

During the initial construction phase, Arne and Ada may commit directly to `main` when the work is explicitly requested, reviewed through local diff/verification, and aligned with the current project standards.

Pull requests are required by default for:
- external contributors,
- post-v1/public collaboration,
- changes where review independence is specifically needed before merge,
- broad or risky changes whose effects are not locally clear.

Direct-to-main work must still preserve:
- clean logical commits,
- no secrets, caches, logs, local machine state, or accidental large files,
- recorded verification where relevant,
- explicit surfacing of unresolved risks.

If a session instruction conflicts with these rules, surface the conflict before committing or pushing unless the user has given an explicit override.

## 2. Safety and cleanup boundaries

Cleanup work must preserve valuable work before optimizing neatness.

Before deleting, moving, rewriting, or ignoring files, classify them as one of:
- canonical source,
- generated canonical output,
- generated disposable output,
- temporary/scratch work,
- legacy/reference material,
- stale duplicate,
- accidental local artifact,
- possible secret or private/local state.

Destructive deletion is allowed only for obvious trash such as caches, compiled byproducts, empty accidental files, or ignored build debris.

If a file may contain useful exploratory work, move it to a review/archive location or ask before removing it.

If a cleanup step would affect many files, rendered manuscript content, canonical figures, CI/release behavior, or anything difficult to reverse, pause and surface the plan first.

Never commit:
- secrets or credentials,
- private logs,
- local environment files,
- caches,
- `_book/`,
- `.quarto/`,
- `.venv/`,
- accidental large files,
- machine-specific state.

Narrow exception: the repo-owned `.Renviron` may be committed only while it remains a documented, non-secret dependency configuration file. Do not treat arbitrary local environment files as covered by this exception.

Prefer `.gitignore` updates for recurring disposable artifacts.

## 3. Repository source-of-truth layout

The repository should distinguish source, build output, reference material, and scratch work clearly.

Canonical manuscript source:
- `index.qmd`
- `_quarto.yml`
- format-specific Quarto config files such as `_quarto-pdf.yml` and `_quarto-html.yml`
- `chapters/**/*.qmd`
- `appendices/**/*.qmd`
- `bibliography.bib`
- `glossary.yml`
- manuscript-owned style/filter/config files
- documented repo-level dependency configuration such as the current non-secret `.Renviron`

Canonical figure source:
- `figures/src/`
- `figures/data/`
- `figures/lib/`
- `figures/scripts/`
- `figures/figures.yml`
- `figures/manifests/`

Canonical generated figure output:
- `figures/build/` when the output is referenced by the manuscript or registered as a canonical figure artifact.

Disposable/generated output:
- `_book/`
- `.quarto/`
- caches
- ad hoc render/test output
- temporary comparison files unless explicitly preserved under an approved review path.

Reference and planning material:
- `AUTHOR_NOTES.md`
- `BOOK_STRUCTURE_PLAN.md`
- `STYLE_FLOW_GUIDE.md`
- `VERIFICATION_POLICY.md`
- `STANDARDS.md`
- `RELEASES.md`
- `DEPENDENCIES.md`
- `figures/docs/`
- `figures/LEGACY_REVIEW.md`
- `figures/ANIMATIONS.md`

Legacy or exploratory material may be kept when it has reference value, but it should not be mistaken for canonical source unless a README, manifest, or active manuscript reference says so.

Cleanup sessions must not delete or demote files merely because they are not currently rendered. First check whether they are source, reference, planned support, or legacy material with retained value.

## 4. Manuscript, Quarto, and part structure

The manuscript is Quarto-first. `_quarto.yml` is the canonical rendered-structure map.

Current rendered structure:
- `index.qmd` is the unnumbered book opener/front stub.
- `chapters/00-preface/index.qmd` is the unnumbered Preface wrapper.
- Preface body sections live in separate included files under `chapters/00-preface/`.
- Numbered parts are declared explicitly in `_quarto.yml` using Quarto `part:` entries.
- Within numbered parts, the listed `.qmd` files are rendered book chapters.
- `references.qmd` sits after the rendered manuscript body.

Default chapter-file pattern:
- Files listed directly in `_quarto.yml` are rendered chapters and must start with `#`.
- Use `##` for first-level in-chapter sections and `###` for subsections.
- Do not start rendered chapter files with `##`; this can break PDF numbering.
- Keep numbered chapter filenames aligned with visible order when practical.

Approved wrapper exception:
- Wrapper chapters are not a general pattern.
- The only approved wrapper chapter is `chapters/00-preface/index.qmd`.
- This exception keeps the Preface as one unnumbered front-matter chapter while allowing section-level files for editing.
- The Preface wrapper starts with `# Preface {.unnumbered}`.
- Included Preface section files start with `##`.
- Do not introduce additional wrapper chapters unless there is a deliberate structure decision and this standard is updated.

Part policy:
- A Quarto `part:` is a major reader-facing division, not merely a folder.
- Part boundaries should be slow to change and should follow `BOOK_STRUCTURE_PLAN.md`.
- Do not create, rename, split, or merge parts as cleanup.
- If a file belongs to a future/proposed part, preserve it as planning/dev material until the structure is intentionally promoted.
- Directories under `chapters/` should align with current or planned part/chapter clusters, but `_quarto.yml` decides what renders.

Before committing manuscript-structure changes:
- check `_quarto.yml` paths,
- check moved/deleted chapter files against references and `BOOK_STRUCTURE_PLAN.md`,
- update `chapters/README.md` if the live structure changed,
- run targeted or full Quarto render when rendered structure changed,
- preserve reader-facing rendered content unless the task explicitly includes prose revision.

## 5. Claim and verification standards

`VERIFICATION_POLICY.md` is the canonical policy for claim roles, regime discipline, and review tiers.

Writers and reviewers must distinguish:
- derivation,
- correspondence,
- interpretation,
- speculation.

Substantial technical claims should make clear, at least in notes/review context:
- active assumptions,
- approximation or regime,
- what is established,
- what remains outside present closure,
- what would count as failure or revision pressure.

Verification expectations:
- Preface and orienting prose usually require V1 review, and V2 when conceptual claims are nontrivial.
- Introduction-level conceptual framing usually requires V2 review.
- Foundations and derivation-heavy material usually require V3 review.
- Long derivations in `appendices/derivations/` should not be treated as accepted without V3 review.

Cleanup/commit sessions should not silently promote unverified material from draft/support status into canonical manuscript status.

Manuscript prose should express claim strength naturally. Do not overload reader-facing text with internal policy labels unless the reader directly needs them.

## 6. Style and flow standards

`STYLE_FLOW_GUIDE.md` is the working guide for manuscript readability, flow, and rhetorical control.

The guide supports drafting and review. It is not a mechanical lint rule, and cleanup/commit sessions should not uphold it by rewriting prose unless explicitly asked.

The live manuscript and part-level style contracts take priority over stale guide assumptions. If the guide conflicts with the current Quarto structure or an intentional part/chapter rhythm, preserve the manuscript structure and update the guide.

Cleanup/commit sessions may flag clear style-standard drift, especially:
- body prose that reads like internal notes,
- repeated caveats that weaken rather than clarify,
- unsupported claim escalation,
- duplicated paragraphs or stale copied text,
- equations or figures with no clear local function,
- headings or filenames that no longer match the section's job,
- obvious spelling or naming errors in canonical terminology.

Signposting phrases are caution flags, not automatic errors. They are acceptable when they mark dependency order, regime shifts, claim status, or transitions between major parts.

Style fixes should be committed separately from structural cleanup unless they are tiny and directly tied to the cleanup target.

## 7. Figure standards

`figures/README.md` is the canonical entrypoint for figure source/build conventions.

There are two canonical figure-control systems:

1. `figures/figures.yml`
   - registry for current non-geometry3d figures,
   - supports deterministic `.R` / `.py` sources,
   - supports prompt-backed AI figures via `*.prompt.md`,
   - records source, output, target chapter, and generator when relevant.

2. `figures/manifests/geometry3d.yml`
   - manifest for native 3D figure families,
   - records family source directories, canonical/review outputs, backend policy, and scene-level exceptions.

A manuscript figure is canonical if it is:
- directly referenced by active manuscript `.qmd` files, or
- registered in `figures/figures.yml`, or
- declared as a canonical scene/output in `figures/manifests/geometry3d.yml`.

Generated figure outputs may be committed only when they are:
- active manuscript assets,
- registered canonical outputs,
- declared geometry3d canonical outputs,
- or explicitly preserved review artifacts under an approved `review/` path.

For ordinary release commits, committed generated figure assets should be PNG files. Generated PDF/SVG companions stay uncommitted unless a manifest, README, or explicit release decision promotes them.

Scratch/demo outputs such as:
- `figures/build/geometry3d/test-renders/`,
- `_tmp-*` files or folders,
- exploratory or iterative `figures/build/geometry3d/*/review/` output piles not explicitly accepted as durable review artifacts,
- ad hoc backend calibration renders,

are not canonical by default. Commit them only if a README, handover, or review note explicitly accepts them as durable reference material.

Prompt-backed AI figures must keep:
- the prompt file under `figures/src/...`, next to the figure family or chapter it supports,
- the checked PNG image artifact under `figures/build/`,
- the generator recorded in `figures/figures.yml` when known.

Root-level prompt folders such as `prompts/` are not canonical for manuscript figures. If a prompt produces or documents a committed figure, move or rewrite it as `figures/src/<area>/<figure>.prompt.md` and register it in `figures/figures.yml`.

Native 3D figures must follow:
- `figures/docs/geometry3d/`,
- `figures/manifests/geometry3d.yml`,
- explicit canonical/fallback/inspection backend policy.

Cleanup sessions should not delete legacy or unrendered figures merely because they are absent from active manuscript references. Classify them against `figures/LEGACY_REVIEW.md`, current manifests, and manuscript plans first.

## 8. Generated-output standards

Generated outputs must be classified before they are committed, ignored, moved, or deleted.

Generated output classes:

1. Disposable build output
   - `_book/`
   - `.quarto/`
   - caches
   - `__pycache__/`
   - `.pytest_cache/`
   - temporary render products
   - local logs

   These should normally be ignored and not committed.

2. Canonical generated manuscript assets
   - generated figure outputs referenced by active manuscript files,
   - registered outputs in `figures/figures.yml`,
   - declared canonical geometry3d outputs,
   - accepted static assets that are intentionally not regenerated during normal CI.

   These may be committed when the source or acceptance record is also present. For ordinary release commits, commit the PNG asset only. PDF/SVG figure companions are treated as generated companions and stay uncommitted unless a manifest, README, or explicit release decision promotes them.

3. Review/reference generated outputs
   - approved backend comparison renders,
   - preserved visual review artifacts,
   - accepted before/after comparison material,
   - outputs documented by a README, handover, or review note.

   These may be committed only when their review/reference purpose is explicit.

4. Scratch/demo generated outputs
   - ad hoc test renders,
   - `_tmp-*` outputs,
   - local experiments,
   - failed render debris.

   These should not be committed unless explicitly promoted.

Generated outputs should be reproducible where practical. If an output is intentionally static or prompt-backed, the source prompt, generator, acceptance note, or registry entry should make that clear.

The book PDF is a release artifact. It should be produced by the release workflow or an explicit release-prep step, then attached to a GitHub Release as `Momentum-First.pdf`. It should not normally be committed to the repository or regenerated on every ordinary CI run.

The README may link to the latest release PDF at `releases/latest/download/Momentum-First.pdf`. Until a release containing that asset exists, the link may return 404.

Cleanup sessions should prefer `.gitignore` updates for recurring disposable outputs and should avoid deleting uncertain generated artifacts until their role is classified.

## 9. CI and pipeline standards

CI should verify project health without turning ordinary development into a release process.

Current CI roles:

1. Validation CI
   - runs on pull requests and manual dispatch,
   - bootstraps the baseline environment,
   - checks declared dependencies,
   - runs lightweight tests or smoke checks.

2. Manual render preview
   - runs only by manual dispatch,
   - renders the book PDF through the release-like path,
   - uploads `Momentum-First.pdf` as an Actions artifact,
   - does not create a GitHub Release.

3. Tag-triggered release
   - runs only for tags matching `v*`,
   - verifies the tag matches `VERSION`,
   - renders the PDF,
   - attaches `Momentum-First.pdf` to the GitHub Release.

4. Figure CI
   - may exist as a scaffold before full implementation,
   - should not be treated as validating canonical figures until it actually runs the relevant figure-generation or smoke-check commands.

Pipeline rules:
- Do not make ordinary pushes create releases.
- Do not commit `_book/` or release PDFs as a substitute for release artifacts.
- Keep heavyweight rendering separate from lightweight validation unless there is a clear reason to combine them.
- Prefer explicit commands such as `quarto render --to pdf` when a workflow's purpose is format-specific.
- CI changes should be small, inspectable, and verified locally where practical.
- If a workflow is only a scaffold, label it as such rather than implying active coverage.

## 10. Version and release standards

Releases are milestone-based, not continuous publishing.

`VERSION` is the canonical repository version file. A release tag must match `VERSION` exactly, with a leading `v` added to the tag name.

Example:
- `VERSION` = `0.2.0`
- release tag = `v0.2.0`

Release rules:
- Do not create releases for ordinary cleanup, typo fixes, or routine manuscript churn.
- Create releases only for durable manuscript or infrastructure milestones worth preserving, sharing, or citing.
- Releases must be made from `main`.
- Release tags should be annotated.
- The tag-triggered release workflow must verify tag/version agreement before publishing.
- The stable PDF release asset name is `Momentum-First.pdf`.

Versioning posture:
- `v0.x.y` is for private/evolving manuscript milestones.
- `v1.0.0` is the first public/citable edition-level release.
- After a release, `VERSION` may move to the next development value, such as `0.2.0-dev`.

Cleanup/commit sessions must not create release tags, bump release versions, or rewrite release policy as routine cleanup.

## 11. Commit and push standards

Commits should preserve reviewability even when work is allowed to go directly to `main`.

Commit rules:
- Commit only after inspecting the final diff for the intended logical unit.
- Stage by logical unit, not by broad path or convenience pattern.
- Keep unrelated changes in separate commits when practical.
- Do not mix cleanup, prose revision, figure generation, CI/release changes, and verification-policy changes unless they are genuinely one change.
- Include generated outputs only when the relevant standards classify them as canonical or accepted review/reference artifacts.
- Do not commit `_book/`, `.quarto/`, caches, local backups, private logs, secrets, or accidental large files.
- Record the relevant verification command(s) in the commit message body or session summary when the change affects rendering, figures, CI, dependencies, or release behavior.

Commit messages should describe the change, not merely the activity.

Prefer:
- `Add release PDF workflow and README link`
- `Document figure source and geometry3d build standards`
- `Restructure Preface as Quarto wrapper chapter`

Avoid:
- `cleanup`
- `updates`
- `fix stuff`
- `misc`

Push rules:
- Do not push unless explicitly requested or the active workflow clearly includes pushing.
- Before pushing, check branch, upstream, status, and recent commits.
- Never push known secrets, local environment state, disposable build output, or unresolved accidental files.
- If pushing would publish a tag, create a release, or otherwise trigger consequential external automation, pause and surface the plan first.
- Release tags are governed by Standard 10 and must not be pushed as routine cleanup.
