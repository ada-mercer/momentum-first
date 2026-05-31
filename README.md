# momentum-first

Quarto-first manuscript repository for the *Momentum First* book.

## Current scope

This repository currently establishes the project structure, book configuration, figure/build layout, and automation entrypoints.
Chapter development, detailed manuscript content, and figure implementations will be added later.

## Working principles

- Quarto-first book workflow
- Reproducible figures and tables
- External heavy scientific code kept outside the manuscript repo
- Quarto execution should be possible across Python, R, and Julia
- Contribution workflow follows `STANDARDS.md`: direct-to-main is allowed for Arne/Ada during initial construction; pull requests are the default for external or post-v1 contribution.

## Dependencies

See `DEPENDENCIES.md` for the current baseline dependency set and installation path.

## Render locally

The shared book structure lives in `_quarto.yml`. The default Quarto profile is PDF, so a plain render produces the PDF book:

```bash
quarto render
```

HTML remains available as an explicit optional profile:

```bash
quarto render --profile html
```

Use the default PDF render for release checks and the HTML profile for fast reading/review.

## Read the book

- [Download the latest PDF](https://github.com/ada-mercer/momentum-first/releases/latest/download/Momentum-First.pdf)

The PDF is published as a release artifact, not committed to the repository. Until the first release with this artifact is created, the link may return 404.

## Releases

This repo uses **infrequent, milestone-based releases** rather than frequent publish churn.
See `RELEASES.md` for the release policy, workflows, and tagging procedure.

## License

This repository uses a split license. Manuscript text, figures, and rendered outputs are licensed under **CC BY-NC-SA 4.0**; code, scripts, tests, and CI configuration are licensed under **MIT**. See `LICENSE.md`.
