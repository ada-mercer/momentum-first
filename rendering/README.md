# Rendering

This directory owns presentation assets shared by the Quarto outputs. It does
not define the book's chapter order or manuscript content.

## Layout

- `assets/backgrounds/pdf/` — title, contents, part, and appendix backgrounds
- `filters/` — Quarto/Pandoc filters used during rendering
- `styles/html/` — HTML theme and project CSS
- `styles/pdf/` — LaTeX macros, preamble, and title-page definitions

The root Quarto files connect these assets to the book:

- [`../_quarto.yml`](../_quarto.yml) defines shared structure and defaults.
- [`../_quarto-html.yml`](../_quarto-html.yml) defines HTML-specific behavior.
- [`../_quarto-pdf.yml`](../_quarto-pdf.yml) defines PDF-specific behavior.

Keep content decisions in `manuscript/` and reusable presentation decisions
here. When moving or renaming a rendering asset, update the applicable Quarto
profile and run the affected render from the repository root.

```bash
quarto render
quarto render --profile html
```

The plain command renders PDF because `_quarto.yml` declares `pdf` as the
default profile. `quarto render --profile pdf` is the equivalent explicit form.

The PDF is a release artifact rather than a tracked repository file. See
[`../docs/RELEASES.md`](../docs/RELEASES.md) for publishing rules.
