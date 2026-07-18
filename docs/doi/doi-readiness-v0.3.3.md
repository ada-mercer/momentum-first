# DOI Readiness Plan — Momentum First v0.3.3

Status audit and execution plan for minting DOIs. Supersedes the planning parts
of `zenodo-v0.3.2.md` (the metadata templates there still apply, bumped to 0.3.3).

## 1. Where we are (audit, 2026-07-09)

**In place**
- Public repo `ada-mercer/momentum-first`; releases through `v0.3.2` (PDF attached).
- `CITATION.cff` present and valid (no `doi:` yet — expected before first deposit).
- `LICENSE.md` split license: manuscript `CC-BY-NC-SA-4.0`, code `MIT`.
- DOI metadata templates drafted (`docs/doi/zenodo-v0.3.2.md`).
- Deliberate decision on record: **no `.zenodo.json`** (it would override
  `CITATION.cff` for GitHub-integration archiving). Keep it that way unless we
  need Zenodo-only fields.

**Broken / unproven**
- The `Release Book` workflow failed on `v0.3.2` at *Create GitHub release*
  ("Too many retries", old `softprops/action-gh-release@v2`). It has since been
  rewritten to the `gh` CLI, but **no tagged run has validated the rewrite**.
- Current branch `gravitomagnetic-calibration` has failing *Validate Repo* PR
  checks, plus uncommitted work (manuscript-status ledger, etc.). A release must
  come from a green `main`.
- `VERSION` = `0.3.3-dev`; the release workflow enforces `tag == VERSION`, so the
  `-dev` suffix will fail a `v0.3.3` tag.

## 2. What is missing to establish DOIs

### Repo-side (can be done here)
1. Land current work: get the branch's checks green, merge to `main`.
2. Finalize `VERSION` → `0.3.3`; align `CITATION.cff` `version` + `date-released`.
3. Validate the rewritten `Release Book` pipeline end-to-end on a tag (the exact
   step that failed before). This is the critical unproven link.
4. Confirm a clean `quarto render --profile pdf` (CI proved it for 0.3.2; re-verify
   after content changes).

### External — Arne only (cannot be automated)
5. **Zenodo↔GitHub integration**: log into Zenodo via GitHub, toggle
   `ada-mercer/momentum-first` on. *Gating step for the source/concept DOI.*
6. **Ordering constraint**: Zenodo only archives releases created *after* the
   toggle is on. `v0.3.2` will not be archived retroactively → the archived
   release must be `v0.3.3` (or a fresh re-release).
7. **Manual PDF deposit** (if we pursue a distinct PDF DOI): upload
   `Momentum-First.pdf` to Zenodo with the templated metadata. Requires Arne's
   Zenodo account; I can prepare everything up to the upload.
8. **Publish approval**: Zenodo DOIs are permanent (records can be tombstoned but
   not deleted). This is a hard commitment boundary.

## 3. Decision needed before execution

**DOI strategy — pick one:**
- **(A) PDF manuscript DOI only (recommended).** Manual Zenodo deposit,
  type *Publication / Book*. The PDF is what readers cite; one clean concept +
  version DOI family. Skips Zenodo↔GitHub wiring entirely.
- **(B) GitHub source DOI only.** Automatic via integration; archives the source
  snapshot. Less natural to cite for a book-shaped work.
- **(C) Both.** Two DOI families (source + PDF); maximal provenance, but invites
  citation ambiguity. Only if we clearly designate the PDF record as canonical.

Recommendation: **(A)** now; add (B) later if a source-archive DOI is wanted.

**Also confirm:** version to mint = `0.3.3`; deposit license = `CC-BY-NC-SA-4.0`;
whether the 0.3.3 content freeze includes the new manuscript-status ledger.

## 4. Ordered execution (once strategy + approval are set)

1. Green the branch; merge to `main`.
2. `VERSION` → `0.3.3`; sync `CITATION.cff`; final `quarto render --profile pdf`.
3. Arne reviews the exact diff.
4. Tag + release `v0.3.3` — this validates the rewritten Release Book workflow and
   produces the citable `Momentum-First.pdf`.
5. **If strategy A:** manual Zenodo PDF deposit → mint DOI.
   **If B/C:** enable Zenodo↔GitHub *before* step 4, let it archive `v0.3.3`.
6. Follow-up commit: DOI badge in `README.md`, `doi:`/`identifiers` in
   `CITATION.cff`, DOI on the landing page, note in `docs/RELEASES.md`.

## 5. Critical path

Strategy decision → branch green on `main` → `VERSION`=0.3.3 → **clean tagged
release (proves the fixed workflow)** → Zenodo deposit/integration → DOI →
badge/CFF follow-up.

The single highest-risk item is #3/step 4: the first real tag run after the
workflow rewrite. Everything downstream depends on that release producing the PDF
cleanly.

## 6. Auto-DOI for the release PDF (exploration)

**Question:** can each release's built PDF be automatically given an updated DOI?

**Key constraint:** Zenodo's native GitHub integration archives only the release
**source tarball**, *not* the release's attached assets. So the auto-minted DOI
would point at a source snapshot, and our polished `Momentum-First.pdf` would not
be the deposited object. The GitHub-native route cannot, by itself, DOI the PDF.

**Working solution — Zenodo REST API from CI.** A release-triggered job that mints
a new *version* DOI under a stable *concept* DOI, with the PDF attached:

1. One-time: create the initial deposition (API or manual) → capture the concept
   record id and concept DOI (`10.5281/zenodo.<concept>`), which always resolves
   to the latest version.
2. Store a Zenodo personal token (`deposit:write`, `deposit:actions`) as the GitHub
   secret `ZENODO_TOKEN`.
3. On release, a workflow step:
   - `POST /deposit/depositions/<latest>/actions/newversion`
   - upload the freshly built `Momentum-First.pdf` to the new version's bucket
   - set metadata (version + publication_date pulled from `VERSION`/`CITATION.cff`;
     license `cc-by-nc-sa-4.0`; upload_type publication / publication_type book)
   - `POST .../actions/publish`
   → new version DOI, same concept DOI, PDF attached. Fully automatic per release.

**Guardrails:**
- Prototype against **sandbox.zenodo.org** first — production DOIs are permanent.
- This automates the manual PDF deposit (strategy A), so it becomes the primary
  route rather than a separate one.
- Optionally *also* enable native GitHub integration for a source-archive DOI, if
  source provenance is wanted; keep the PDF record designated canonical.
- Do **not** commit built PDFs into the repo to smuggle them into the source
  archive — that pollutes history for a worse result.

Recommendation: pursue the API-in-CI route for the PDF, validated on sandbox
before the first production mint. Implementation is gated on the `ZENODO_TOKEN`
secret and an initial concept deposition.
