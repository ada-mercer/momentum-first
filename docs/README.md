# Project documentation

This is the navigation layer for people working on *Momentum First*. The root
[`README.md`](../README.md) is the public landing page; this file routes
contributors, authors, and maintainers to the operational source that governs
their work.

## Choose a route

| If you want to… | Start here |
|---|---|
| Understand the framework or read the manuscript | [HTML book](https://ada-mercer.github.io/momentum-first/) or the [root README](../README.md) |
| Edit book source or understand its layout | [`manuscript/README.md`](../manuscript/README.md) |
| Create, rebuild, or review figures | [`figures/README.md`](../figures/README.md) |
| Change HTML or PDF presentation | [`rendering/README.md`](../rendering/README.md) |
| Run checks, generators, or local automation | [`tooling/README.md`](../tooling/README.md) |
| Understand GitHub automation | [`.github/README.md`](../.github/README.md) |
| Prepare a milestone release | [`RELEASES.md`](RELEASES.md) |

## Documentation authority

When two documents overlap, use this order:

1. [`STANDARDS.md`](STANDARDS.md) governs contribution, cleanup, source layout,
   verification, figures, generated outputs, CI, releases, and commits.
2. Executable configuration and manifests govern what the tools actually do:
   [`_quarto.yml`](../_quarto.yml) defines the rendered book structure,
   [`figures/figures.yml`](../figures/figures.yml) registers current figures,
   and [`figures/manifests/geometry3d.yml`](../figures/manifests/geometry3d.yml)
   governs native 3D families.
3. The relevant domain README explains how to work within that domain.
4. A local README may add rules for one specialized subtree, but it should not
   restate or contradict project policy.
5. Plans, handovers, provenance notes, and historical records explain intent or
   history; they do not override the sources above unless explicitly promoted.

The working manuscript is the mature public statement of M1. Supporting plans
and internal records should not silently expand its claims.

## Reference documents

- [`STANDARDS.md`](STANDARDS.md) — governing repository and contribution standard
- [`VERIFICATION_POLICY.md`](VERIFICATION_POLICY.md) — claim roles, review tiers,
  and acceptance requirements
- [`DEPENDENCIES.md`](DEPENDENCIES.md) — supported dependency modes and setup
- [`BOOK_STRUCTURE_PLAN.md`](BOOK_STRUCTURE_PLAN.md) — intended book architecture
- [`STYLE_FLOW_GUIDE.md`](STYLE_FLOW_GUIDE.md) — manuscript prose and flow guidance
- [`RELEASES.md`](RELEASES.md) — version, tag, artifact, and publishing procedure
- [`CONTRIBUTORS.md`](CONTRIBUTORS.md) — contributor record
- [`provenance/README.md`](provenance/README.md) — section-level contribution and
  verification ledger
- [`doi/`](doi/) — DOI preparation records

## Where documentation belongs

- Put public orientation in the root README and keep it brief.
- Put project-wide policy and durable reference material in `docs/`.
- Put authoring and layout guidance in `manuscript/`.
- Put subsystem instructions beside the subsystem they govern.
- Keep detailed geometry3d guidance under `figures/docs/geometry3d/` and route
  readers there from `figures/README.md`.
- Prefer links to the governing document over copied commands or duplicated
  policy. Update every affected entrypoint when responsibilities or paths move.
