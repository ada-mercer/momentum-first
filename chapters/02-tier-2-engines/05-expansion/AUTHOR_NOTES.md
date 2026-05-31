# Author notes — Chapter 05 Space Expansion as Translation Yield

Status: fresh rewrite in place under corrected translation-yield lock
Updated: 2026-05-16
Mode stack: roles/book-prose + topics/m1/cosmology + artifacts/manuscript + styles/book-mainline + audiences/broad-technical

Active rewrite plan: `book/dev/author-plans/COSMOLOGY_CHAPTER_REWRITE_PLAN_V1.md`.

## Preflight completed for this rewrite

This pass used the rewrite plan plus the required preceding manuscript context:

- Introduction: momentum-first wager, fair standard of judgment, and non-doctrinal posture.
- Foundations: `p_f`, `p`, `p_k`, `M`, ADMC, inverse map, stage/actor distinction, time/clock stance, and Kinematic Modifier taxonomy.
- Gravity and Structured Spacetime: source -> field -> local readout grammar; gravity as local momentum-sourced deformation of the relational stage; local clock and transport bookkeeping.
- Quantum Mechanics: Tier 2 engine style: build a grammar, show compatibility/correspondence where earned, and leave empirical or ontological completion visibly bounded.
- `momentum-first/STYLE_FLOW_GUIDE.md` and `book/m1/TERMINOLOGY.md`.

Comprehension gate for the chapter:

- ADMC is stated without `\chi`: `p_{k^+}=M(p)+\frac12p_k`, `p_{k^-}=M(p)-\frac12p_k`.
- `p` is bosic momentum magnitude; `p_k` is a directional component of `\vec p`; `M(p)` is the core momentum package; `\chi(t)` is translation yield.
- Gravity remains the local source -> field -> observer engine. Space expansion is treated as a background translation-yield engine comparing emission, propagation, and reception across epochs.
- This chapter is Tier 2: it establishes the space-expansion engine grammar, conditional signal mappings, compatibility guardrails, and test interfaces. Tier 3 must supply fitted histories, kernels, and falsifiers.

## Chapter burden

Build the first reader-facing M1 account of space expansion as a translation-yield chapter.

The chapter should make apparent expansion legible in momentum language without putting expansion into the momentum variables. The large-scale stage may change how much translation directed bosic momentum expression yields across epochs. That change is represented by `\chi(t)`.

Corrected lock:

```tex
\chi(t)=\text{translation yield},
\qquad
\dot x_k(t)=\chi(t)c\frac{p_k}{M(p)},
\qquad
1+z=\frac{\chi_e}{\chi_o}.
```

with `\chi_e=\chi(t_e)`, `\chi_o=\chi(t_o)`, and `\chi(t_o)=1` by default normalization.

ADMC remains unscaled:

```tex
p_{k^+}=M(p)+\frac12p_k,
\qquad
p_{k^-}=M(p)-\frac12p_k.
```

The inverse identities remain:

```tex
M(p)=\frac{p_{k^+}+p_{k^-}}2,
\qquad
p_k=p_{k^+}-p_{k^-}.
```

Keep `c` explicit in mainline prose. It is the inherited local light/momentum scale in the map, not a variable-`c` cosmology. For lightlike propagation the map gives `\dot x=\chi(t)c`; describe this as a variable translation-yield propagation rate, not as a second fundamental speed of light.

## Boundary lock

Keep central:

- expansion/conservation pressure as the opening problem;
- no separate dark-energy substance in the M1 primitive expansion account; acceleration-like behavior, if modeled later, must come through the yield history or another explicit mechanism;
- space expansion as the main yield-modifier example;
- `\chi(t)` as translation yield, outside ADMC;
- `\chi\sim1/a` as the formal scale-factor comparison, while preserving the M1 interpretation as translation yield rather than primitive metric expansion;
- redshift as a yield-ratio mapping;
- duration dilation as the paired signal-stretching mapping;
- local-physics preservation as bound-system/core-momentum organization plus compatibility scales, not a proof of exact invariance;
- observational interfaces as falsifier and model-building burdens;
- Tier 3 handoff for fitted `\chi(t)` histories, distance kernels, flux laws, CMB/BBN/recombination, and matter growth.

Keep out of mainline equations and active claims:

- `p_can`, `p_phys`, `p_b`, dual-momentum ontology;
- `\chi` multiplying `p_k` inside ADMC;
- photon momentum-cooling or momentum-decay explanations of redshift;
- variable-`c` ontology;
- global co-scaling of constants as proof;
- exact local indistinguishability;
- solved CMB, Tolman, horizon, dark-energy, Hubble-tension, BBN, recombination, or early-galaxy claims;
- reuse of `\chi` for screened matter mobility. If needed later, reserve `\mu_m(a,k,\mathrm{env})`.

## Revised section map

1. `01-space-expansion-and-the-conservation-problem.qmd` — opens from the expansion/conservation pressure and frames the chapter as a Tier 2 translation-yield engine.
2. `02-core-terms-and-variables.qmd` — locks ADMC, `p`, `p_k`, `M(p)`, `\chi(t)`, `c`, event notation, `H_\chi`, and reserved `\mu_m`.
3. `03-translation-yield-as-the-m1-expansion-engine.qmd` — places space expansion inside the KM taxonomy while contrasting it cleanly with local gravity.
4. `04-directional-channels-and-translation-yield.qmd` — formal core: unchanged momentum grammar, then the yield-modified translation map.
5. `05-redshift-as-a-yield-ratio-mapping.qmd` — conditional internal mapping `1+z=\chi_e/\chi_o`, with anti-tired-light guardrail subordinate to the positive mechanism.
6. `06-duration-dilation-and-signal-stretching.qmd` — paired pulse-length and endpoint-integral derivations of `\Delta t_o=(1+z)\Delta t_e`.
7. `07-what-changes-and-what-is-preserved.qmd` — changes/preserved split, explicit bound-system/core-momentum screening language, plus `H_\chi\tau_{dyn}\ll1` locality heuristic.
8. `08-interfaces-to-observational-cosmology.qmd` — ordered burden map: history, distances, duration/drift, causal reach, flux/Tolman, CMB/thermal history, local metrology, deferred matter growth.
9. `09-what-the-expansion-chapter-establishes.qmd` — closes with exactly what Tier 2 earns and what remains unearned.

## Verification priorities

Run targeted checks for quarantined notation and overclaiming after edits. Expected result: forbidden terms appear only as guardrails in these notes or explicit quarantine language, not as active manuscript mechanisms.
