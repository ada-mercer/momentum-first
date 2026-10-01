# Part 0 opening chapter — adopted figure provenance

Integrated 2026-10-01 at the owner's request. The eight working QMD files
matched candidate `2026-10-01-v17` byte-for-byte before the integration pass.
The seven referenced PNGs were copied unchanged into
`figures/build/part-0-first-picture/`; `adopted-assets.json` records their hashes,
original candidate paths, figure IDs and owning sections.

These are checked static manuscript assets in `figures/figures.yml`. Ordinary
publication CI checks their presence without regenerating PyVista output or
introducing a new graphics dependency into the pinned publication image.
This integration does not promote the planned geometry3d `torus-cycle` family
to implemented status: these are chapter-specific explanatory schematics.

## Retained generation sources

`recipe/validation/` preserves the six generation/helper scripts from v17
without changing their drawing code. They use Matplotlib, NumPy, Pillow and
the existing shared geometry3d/PyVista backend. No image-generation model is
involved. The final plates require the ordered recipe: basic figures, the
revised two-cycle figure, mode storyboard, opaque momentum close-up, then the
v17 pitch figure. Earlier intermediate plates are deliberately overwritten
within the temporary render directory, not in the canonical asset tree.

From the repository root, using its full local geometry environment:

```bash
.venv/bin/python figures/src/part-0-first-picture/render_all.py --output-dir /tmp/m1-part0-figure-review
```

The destination must be new. The helper writes review PNGs and diagnostics,
never the selected canonical assets. Compare regenerated images with the
adoption hashes and inspect any renderer/font differences before replacement.
V17's earlier mathematical and scientific-writing review records cover their
named revisions and constructions, not blanket scientific certification of
the chapter or these illustrative modes.
