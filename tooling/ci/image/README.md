# Pinned CI build image

This directory defines the full figure and PDF build environment used by
GitHub Actions. The runtime workflows reference a published GHCR image by its
immutable digest; they never rebuild or update the image implicitly.

The image intentionally contains only the dependencies required by the current
registered figure builders, repository checks, and PDF renderer. The local
`tooling/ci/install-ubuntu.sh` installer remains the development and recovery
path outside CI.

Nimbus Sans is installed explicitly because base R resolves its `Helvetica`
device family through fontconfig. Omitting that package changes two canonical
R-rendered PNGs even when every R package version is identical.

The maintained production reference is [`reference.txt`](reference.txt).
Actions must know a container image before checkout, so its four consumer jobs
retain literal digest-pinned copies. `sync_ci_image.py` and repository validation
check those copies; they are not independent configuration choices.

## Update procedure

1. Change `Dockerfile`, `requirements.in`, or `install-r-packages.R`.
2. Regenerate the Python lock from the repository root:

   ```bash
   uv pip compile tooling/ci/image/requirements.in \
     --python 3.14.3 \
     --generate-hashes \
     --output-file tooling/ci/image/requirements.lock
   ```

3. Build and test the image locally.
4. Publish it through the `Build CI Image` workflow.
5. Benchmark the candidate image locally through figures and PDF rendering before
   adopting its digest. In an isolated checkout, update the reference and consumer
   copies together:

   ```bash
   python3 tooling/scripts/sync_ci_image.py --set ghcr.io/ada-mercer/momentum-first-build@sha256:REPLACE_WITH_VERIFIED_64_HEX_DIGEST
   python3 tooling/scripts/sync_ci_image.py
   ```

   The script does not pull, build or publish an image. The manual benchmark
   workflow verifies the digest selected by that checkout; it checks a nonempty
   PDF and embedded fonts, not a fixed manuscript page count. Publication of a
   workflow change or an image remains a separate authorized operation.
