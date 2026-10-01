# DOI Workflow

Status: operational. The v0.3.8 release and manuscript DOI job completed on
2026-08-03. New releases publish versions in the existing families; no new
bootstrap is needed. Production publication retains its environment approval.

This is the canonical DOI procedure. Earlier version-labelled files in this
directory are retained as planning history and metadata provenance.

## Record architecture

| Record | Purpose | Zenodo type | License | Automation |
|---|---|---|---|---|
| Manuscript | Canonical citation for `Momentum-First.pdf` | Publication / Book | CC-BY-NC-SA-4.0 | Repository release workflow through the Zenodo API |
| Source | Tagged repository provenance | Software | File-scoped CC-BY-NC-SA-4.0 + MIT, represented by `other-open` and an explicit rights statement pointing to `LICENSE.md` | Native Zenodo GitHub integration |

The manuscript concept DOI is the general citation target. Each formal release
also receives an immutable version DOI. The source record is a separate DOI
family and is not presented as the preferred manuscript citation.

Arne Klaveness is the sole creator on both records. AI assistance is described
only in acknowledgement text. Do not add Ada/OpenClaw as a creator or structured
person contributor.

Zenodo's GitHub importer can read only one CFF license and applies that value to
the entire archived source file. The repository therefore includes a narrow
`.zenodo.json` override for the source record: `other-open` plus an explicit
description of the CC-BY-NC-SA-4.0/MIT path split governed by `LICENSE.md`.
Zenodo ignores `CITATION.cff` when this override is present; GitHub still uses
the CFF for its repository citation display and preferred book citation.

## Repository implementation

- `zenodo-manuscript.json` is the stable Publication / Book metadata template.
- Root `.zenodo.json` is the source-archive metadata override required for
  accurate split-license disclosure.
- `tooling/scripts/publish_zenodo.py` bootstraps and updates the manuscript DOI
  family. It uses only the Python standard library.
- `.github/workflows/release-book.yml` passes the exact rendered release PDF to
  a separate `zenodo-production` job after the GitHub Release exists.
- `ZENODO_MANUSCRIPT_CONCEPT_ID` must be a GitHub **repository variable**.
- `ZENODO_TOKEN` must be an environment secret in `zenodo-production`, with
  Zenodo `deposit:write` and `deposit:actions` scopes.

The publication client is intentionally strict:

- `bootstrap` creates an empty, unpublished family draft but publishes nothing;
- `publish` refuses to create a family implicitly;
- production publication requires `--confirm-publication`;
- a rerun recognizes an already-published version and verifies the PDF checksum;
- an existing draft for another version, a non-increasing version, multiple
  drafts, or a checksum mismatch stops the workflow;
- tokens can be sent only to the official Zenodo production or sandbox hosts.

## One-time setup

Perform these steps before the first DOI-bearing tag.

Setup completed on 2026-07-31:

- the native Zenodo GitHub integration is enabled for
  `ada-mercer/momentum-first`;
- the manuscript client published and idempotently re-verified Sandbox version
  `0.3.7` under test concept record `578803`;
- the unpublished production manuscript family is bootstrapped with concept
  record ID `21729037` and initial draft ID `21729038`;
- GitHub repository variable `ZENODO_MANUSCRIPT_CONCEPT_ID`, the
  `zenodo-production` environment, its required `ada-mercer` approval, and the
  environment secret `ZENODO_TOKEN` are configured.

The subsequent v0.3.8 release completed production publication:
[release run](https://github.com/ada-mercer/momentum-first/actions/runs/30821088453).
Current manuscript concept DOI: `10.5281/zenodo.21729037`.
Current source concept DOI: `10.5281/zenodo.21775704`.
The initial draft IDs above are historical bootstrap facts, not current drafts.

For an exceptional future credential rotation, use the host's protected secret
entry or GitHub's environment-secret UI; never put tokens in commands, transcripts
or files staged for commit. Keep the existing `ZENODO_TOKEN` environment secret
and `ZENODO_MANUSCRIPT_CONCEPT_ID` repository variable. Do not repeat family
bootstrap for a normal release. Publication remains the permanent external
commitment boundary, distinct from preparing source or a preview.

## Future formal release procedure

1. Update and validate `VERSION`, `CITATION.cff`, and `docs/RELEASES.md` through
   the normal release gate.
2. Confirm the Zenodo GitHub integration is enabled, the repository concept-ID
   variable exists, and the production token is valid.
3. Push the annotated `vX.Y.Z` tag.
4. `Release Book` validates the repository, renders `Momentum-First.pdf`, and
   publishes the GitHub Release.
5. Zenodo archives the tagged source through its GitHub integration. The
   `Publish manuscript DOI version` job publishes the exact PDF as a new version
   of the manuscript family and records both DOI links and the SHA-256 checksum
   in the Actions summary.
6. If the Zenodo job fails, inspect the error and rerun the failed job. Do not
   create another draft or DOI family manually; the client resumes the existing
   version draft or verifies the published version.
7. Manually dispatch `Deploy Book Site` when the site should pick up the new PDF.

The two concept DOI links are already recorded in the README and CFF.
Release-specific version DOIs are recorded in the release receipt and provider
records; they do not require rewriting the tagged source after publication.

## Local validation without publication

Use any valid release PDF and matching release URL:

```bash
python3 tooling/scripts/publish_zenodo.py publish \
  --pdf /path/to/Momentum-First.pdf \
  --version X.Y.Z \
  --publication-date YYYY-MM-DD \
  --github-release-url \
    https://github.com/ada-mercer/momentum-first/releases/tag/vX.Y.Z \
  --concept-record-id 123456 \
  --dry-run
```

Dry-run mode reads no token and performs no network mutation.

## Provider references

- [Enable a repository in Zenodo's GitHub integration](https://help.zenodo.org/docs/github/enable-repository/)
- [Archive a GitHub release](https://help.zenodo.org/docs/github/archive-software/github-upload/)
- [Zenodo record versioning](https://help.zenodo.org/docs/deposit/manage-versions/)
- [Zenodo REST API](https://developers.zenodo.org/)
- [Zenodo JSON metadata precedence](https://help.zenodo.org/docs/github/describe-software/zenodo-json/)
- [Zenodo licenses and mixed-license records](https://help.zenodo.org/docs/deposit/describe-records/licenses/)
