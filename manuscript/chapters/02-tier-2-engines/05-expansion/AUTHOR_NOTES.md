# Author notes — Chapter 05 Space Expansion as Translation Yield

Status: adopted chapter under bounded second-pass refinement
Updated: 2026-07-28
Mode stack: roles/book-prose + topics/m1/cosmology + artifacts/manuscript + styles/book-mainline + audiences/broad-technical

## Chapter burden

Build a reader-facing M1 account of space expansion as a translation-yield engine. Apparent expansion must remain legible in momentum language without placing the expansion factor inside the conserved momentum variables.

The governing placement is

```tex
\chi(t)=\text{translation yield},
\qquad
\dot x_k(t)=\chi(t)c\frac{p_k}{M(p)}.
```

ADMC and the shell readings remain unscaled:

```tex
p_k^\pm=M(p)\pm\frac12p_k.
```

The conditional signal dictionary is

```tex
1+z=\frac{\chi_e}{\chi_o},
```

with `\chi_e=\chi(t_e)`, `\chi_o=\chi(t_o)`, and `\chi_o=1` by default normalization.

## Bookkeeping distinction

- `t` is the common homogeneous background-history parameter used in `\chi(t)` and the propagation integral.
- `x_k` is the associated background translation coordinate.
- `\delta t_e` and `\delta t_o` are neighboring-feature endpoint separations in that background parameter.
- `\Delta t_e` and `\Delta t_o` are durations reported against emitter and observer clock standards.
- The common-path derivation relates the background endpoint separations. The duration law additionally uses the matched endpoint-clock condition supported by the clean UYC branch.
- `\mathcal D_\chi=c\int\chi(t)dt` is a propagation kernel, not by itself an observational distance.

## UYC status lock

Universal Yield Covariance is adopted at the covariance-principle level for the universal-yield construction. Its kinematic transform and sector targets are established in Derivations 5.6A and 5.6B. Electromagnetic, gravitational, strong, and weak realization, exact local residuals, and empirical closure remain pending.

UYC should not be described as merely an optional stronger route. Preserve the three levels:

1. adopted covariance principle;
2. established kinematic transform and covariance targets;
3. pending sector realization and empirical closure.

## Boundary lock

Keep central:

- expansion/conservation pressure as the opening problem;
- actor change versus stage change;
- translation yield outside ADMC;
- no photon momentum cooling or bosic-momentum decay;
- fixed intrinsic `c`, with `\chi c` as the lightlike translation expression;
- `\chi\propto1/a` as the broad formal correspondence;
- `a_B=\chi_o/\chi` as the normalized clean UYC branch;
- redshift as a conditional matched-standard endpoint dictionary;
- duration stretching from the neighboring-feature path comparison plus the endpoint-clock condition;
- UYC as the adopted covariance principle, with sector realization pending;
- observational tests as discriminators among completed histories and realizations.

Keep out of active claims:

- `\chi` multiplying momentum inside ADMC;
- photon momentum cooling or momentum decay;
- variable intrinsic-`c` ontology;
- exact local indistinguishability;
- completed electromagnetic, gravitational, strong, or weak UYC realization;
- solved distance, flux, Tolman, CMB, BBN, recombination, growth, lensing, horizon, dark-energy, Hubble-tension, or early-galaxy claims;
- reuse of `\chi` as an unexplained matter-mobility factor.

## Active section map

1. `01-space-expansion-and-the-conservation-problem.qmd` — conservation pressure, actor and stage, and effective-pitch intuition.
2. `02-core-terms-and-variables.qmd` — inherited momentum notation, translation yield, propagation coordinates, and signal labels.
3. `03-translation-yield-and-directional-displacement.qmd` — downstream translation map and limiting checks.
4. `04-redshift-as-comparison-between-yield-states.qmd` — lightlike propagation, history kernel, and neighboring-feature path comparison.
5. `05-duration-dilation-and-signal-stretching.qmd` — conditional spectral dictionary and matched-clock duration relation.
6. `06-bound-systems-and-local-screening.qmd` — adiabatic local equilibrium, SMC-to-UYC route, transform, and sector boundary.
7. `07-yield-histories-and-distance-kernels.qmd` — endpoint ratio, history kernel, observable distance, and causal reach.
8. `08-interfaces-to-observational-cosmology.qmd` — discriminating observational program.
9. `09-what-the-expansion-chapter-establishes.qmd` — earned hierarchy and Tier 3 handoff.

## Verification priorities

After adoption, check:

- every display-math delimiter is paired;
- the index includes all nine files in order;
- no superseded shell-reading notation has returned;
- `\chi` never appears inside ADMC or intrinsic `p_f=m_0c`;
- UYC is not described as optional;
- the redshift dictionary remains conditional;
- the duration relation retains both its path and endpoint-clock assumptions;
- `\mathcal D_\chi` is not called a luminosity or angular-diameter distance;
- terminology uses **translation yield** as the chapter's governing term.
