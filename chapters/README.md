# Chapters

This directory holds the book's front matter and main body using a chapter-directory pattern.

Current structure:
- `00-preface/index.qmd`
- `01-introduction/index.qmd` plus subsection files
- `02-foundations/index.qmd` plus subsection files

## Authoring policy

Use:
- one directory per major chapter/section
- `index.qmd` for the chapter-level framing
- numbered subsection files for the actual development

This structure is preferred because it gives human and AI authors a more realistic target size for each drafting task, reduces context bloat, and makes section-level review easier.

## Subsection naming

Use numbered subsection filenames such as:
- `01-01-situation.qmd`
- `01-02-challenge.qmd`
- `02-03-invertible-mapping.qmd`

Keep filenames aligned with visible section numbering when practical.
