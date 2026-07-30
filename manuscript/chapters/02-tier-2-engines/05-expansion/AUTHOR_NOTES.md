# Author notes — Chapter 05 Space Expansion and Stage Dressing

Status: adopted working chapter; χ² package integrated for v0.3.7
Updated: 2026-07-30
Mode stack: roles/book-prose + topics/m1/cosmology + artifacts/manuscript + styles/book-mainline + audiences/broad-technical

## Chapter burden

Build a reader-facing Tier 2 expansion engine that keeps conserved spatial
momentum content separate from the stage-conditioned generator value and
translation rate. The governing bosic-slot construction is

```tex
\hat M_\chi
=
\beta p_f+\chi\,\boldsymbol{\alpha}\!\cdot\!\hat{\mathbf p},
\qquad
M_\chi
=
\sqrt{p_f^2+\chi^2p^2},
```

with true-frame and clean bound-frame velocities

```tex
\dot x_T
=
\chi^2c\frac{p}{M_\chi},
\qquad
v_B
=
\frac{1}{\chi}\dot x_T
=
\chi c\frac{p}{M_\chi}.
```

The second power of `\chi` is supplied by differentiating the dressed
eigenvalue; it is not an independently attached cosmological factor.

## Stable distinctions

- `p_f` and `\mathbf p` are conserved carrier labels in the homogeneous free
  problem.
- `\hat M_\chi` is the dressed generator; `M_\chi` is its positive
  eigenvalue.
- `\chi` is the stage factor; `X=\chi/\chi_o` is the
  observation-normalized ratio, with `\chi_o=1` used only when stated.
- `x_T` is the true-frame translation coordinate; `x_B=x_T/X` is the clean
  bound-frame coordinate.
- `\delta t` labels neighboring-feature intervals in the common history
  parameter; `\Delta t` denotes locally reported durations.
- `\mathcal D_\chi=c\int\chi(t)\,dt` is a propagation kernel, not by itself an
  observational distance.
- Bound-frame kinematics and gravitational source weight are separate
  questions.

## Claim lock

Established within the stated homogeneous two-slot architecture:

- bosic-slot dressing produces the `\chi^2` true-frame group velocity;
- the lightlike limit remains `\dot x_T=\chi c`;
- the clean bound-frame map reproduces the exact special-relativistic FLRW
  free-carrier velocity and drag law when `p` is identified with comoving
  momentum;
- lightlike propagation maps to the usual conformal path and does not enlarge
  causal reach;
- matched endpoint standards give the scoped wavelength and duration ratios.

Conditional realizations:

- hydrogenic covariance under `e^2(X)=e_o^2X`;
- Newtonian bound-orbit covariance and fixed-background linear growth under
  `G_{\mathrm{eff}}(X)=G_NX`;
- first-power coupling selection only within those proxy Hamiltonians and the
  clean local-standard target.

Keep open:

- the dynamical law for `\chi(t)` or `H(t)`;
- a closed stage action or Friedmann/Λ sector;
- dressed gravitational source weighting or any ADMC amendment;
- strong, weak, radiation, nonlinear, horizon-scale, and lensing closure;
- detailed torus, winding, radius, or modulus ontology;
- observational anomaly explanations.

## Active section map

1. `01-space-expansion-and-the-conservation-problem.qmd` — conservation
   pressure and the simplified physical preview.
2. `02-core-terms-and-variables.qmd` — stable notation and frame dictionary.
3. `03-stage-dressing-and-massive-motion.qmd` — bosic-slot construction,
   `\chi^2` law, FLRW correspondence, and placement diagnostic.
4. `04-light-propagation-and-endpoint-comparison.qmd` — lightlike kernel,
   conformal reach, and endpoint relations.
5. `05-bound-frames-and-local-standards.qmd` — clean transform, radar check,
   and adiabatic scope.
6. `06-scoped-realizations-and-correspondence-checks.qmd` — hydrogenic,
   Newtonian, and fixed-history growth proxies.
7. `07-what-the-expansion-engine-establishes.qmd` — maturity ladder and Tier 3
   handoff.

## Appendix trust layer

- `05-02A` — bosic-slot placement and χ² group-velocity theorem.
- `05-03A` — free-carrier FLRW correspondence and drag.
- `05-04A` — lightlike propagation and matched endpoint standards.
- `05-06A` — local covariance and scoped sector realizations.

These appendices remain working-draft trust material. Their qualified AI review
is recorded separately; no new human-verification claim is implied by v0.3.7.
