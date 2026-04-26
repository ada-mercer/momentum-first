# Chapters

This directory holds the book's front matter and main body.

## Current rendered structure

The canonical rendered-structure map is `_quarto.yml`.

Current pattern:
- `00-preface/index.qmd` is the unnumbered Preface wrapper.
- `00-preface/00-*.qmd` files are included Preface sections.
- `01-introduction/*.qmd` files listed in `_quarto.yml` are rendered chapters inside the Introduction part.
- `02-foundations/*.qmd` files listed in `_quarto.yml` are rendered chapters inside the Foundations part.
- `03-gravity-and-structured-spacetime/*.qmd` files listed in `_quarto.yml` are rendered chapters inside the Gravity and Structured Spacetime part.

## Default chapter-file policy

Use:
- one directory per major front-matter or part/chapter cluster,
- one rendered `.qmd` file per book chapter entry in `_quarto.yml`,
- numbered chapter files for rendered part chapters.

Rendered chapter files listed directly in `_quarto.yml` must use standard Quarto book heading levels:
- `#` for the chapter title,
- `##` for first-level in-chapter sections,
- `###` for subsections.

Do not start rendered chapter files with `##`; LaTeX/PDF numbering can then produce broken subsection numbers such as `III.1.0.1`.

## Preface wrapper exception

The Preface is the only approved wrapper exception.

`00-preface/index.qmd` remains the rendered unnumbered Preface chapter and starts with:

```md
# Preface {.unnumbered}
```

It may include section files such as:
- `00-01-a-persistent-tension.qmd`
- `00-02-what-kind-of-book-this-is.qmd`
- `00-03-on-authorship-and-collaboration.qmd`
- `00-04-how-to-read-this-book.qmd`
- `00-05-working-method.qmd`

Included Preface section files start with `##` because they are sections inside the Preface, not standalone rendered chapters.

Do not introduce additional wrapper chapters unless `STANDARDS.md` is intentionally updated.

## Naming

Keep numbered filenames aligned with visible section or chapter order when practical.

Examples:
- `01-01-the-success-of-physics.qmd`
- `02-03-invertible-mapping.qmd`
- `03-02-gravitational-sources.qmd`

For the Preface, use `00-NN-short-slug.qmd` for included section files.
