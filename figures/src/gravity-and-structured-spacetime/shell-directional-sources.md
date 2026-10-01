# Shell directional sources

Approved Research2 figure, integrated on 2026-09-18. Registry ID:
`fig-shell-directional-sources`. Intended section: `03-gravitational-sources.qmd`.
Registration makes the PNG a canonical figure asset; chapter insertion is not
part of this pipeline integration.

## Sources and build

- Renderer: `shell_directional_sources.py`.
- Editable composition: `shell_directional_sources.layout.yaml`.
- Caption and mathematical scope: `shell-directional-sources.caption.md`.
- Reuses the original Foundations renderer's `scalar_spoke` helper and origin/
  contour styling through a repository-relative import. No external lab paths,
  media files or GenAI assets are required.
- Canonical output: `figures/build/gravity-and-structured-spacetime/shell-directional-sources.png`.
- PNG is the default output; SVG/PDF are optional uncommitted companions.

From the repository root:

```bash
python3 figures/scripts/generate_all.py
# Or render only this figure:
.venv/bin/python figures/src/gravity-and-structured-spacetime/shell_directional_sources.py
# Optional companions, outside canonical builds:
.venv/bin/python figures/src/gravity-and-structured-spacetime/shell_directional_sources.py --output-dir /tmp/shell-source-review --formats png svg pdf
```

The renderer also supports `--layout` for explicit layout variants. It verifies
both hemispheres by solid-angle quadrature for the displayed oblique momentum.
The caption keeps the auxiliary density distinct from the reading contour;
registration does not promote it to microscopic physics or assert 4M physical
particle content.

## Provenance

Adapted from the approved code-built lab figure
`labs/visualization/shell-directional-sources/render_integral_simple.py` in the
shared project. Research2 messages 12560 and 12564 specified simplification,
fourth-quadrant dOmega, original capped spokes and origin/line weights;
message 12571 requested pipeline integration. Earlier lab versions are retained
as historical working artifacts, not pipeline dependencies.
