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

Current production reference:

```text
ghcr.io/ada-mercer/momentum-first-build@sha256:b84ecafd7849b0edaaf82f3faf699dfb9780f32f522dfc6fe477752f7566ee4e
```

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
5. Benchmark figures and PDF rendering before updating any production workflow
   digest.
