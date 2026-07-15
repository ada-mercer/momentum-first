# Foundations Author Notes

## Job of this chapter

Foundations is where the book begins to cash out its claims.

It should establish:
- primitive momentum terms and notation
- the physical momentum configuration joining fermic and bosic roles
- ADMC as the directional-positive conservation postulate
- the positive branch magnitudes, positive oriented reading, and exact correspondence map
- the inertial SR correspondence in momentum-first variables
- the stage/actor distinction between space and momentum
- the time / clock / dilation interpretation
- the true-frame stance as an interpretive commitment, not a new inertial equation
- kinematic modifiers as the grammar for departures from the inertial baseline
- a clean closing statement of what Foundations has and has not established

It should **not** develop the gravity program. The Tier 2 gravity chapter owns gravity as the first major engine.

## Local tone target

Foundations should feel:
- explicit
- disciplined
- technically cleaner than the Preface and Introduction
- sparse on rhetoric
- confident about M1's own commitments without overclaiming derivation status

This is where the framework either starts to hold together or it doesn't.

## Rendered file sequence

The Foundations wrapper, `index.qmd`, includes eight rendered section files in this order:
1. `01-core-terms-and-variables.qmd`
2. `02-the-momentum-configuration.qmd`
3. `03-admc.qmd`
4. `04-invertible-mapping.qmd`
5. `05-space-and-momentum-stage-and-actor.qmd`
6. `06-time.qmd`
7. `07-kinematic-modifiers.qmd`
8. `08-what-foundations-establishes.qmd`

Historical note:
- the former minimal-gravity-grammar section is no longer rendered. Keep it out unless the architecture changes again.
- the former scope-and-status section has been replaced by `08-what-foundations-establishes.qmd` as the rendered closer.

## Mode references

Use these as the default stack when writing or revising Foundations prose:
- `modes/roles/book-prose`
- `modes/topics/m1/foundations`
- `modes/artifacts/manuscript`
- `modes/styles/book-mainline`
- `modes/audiences/broad-technical`

## Derivations

If a derivation grows long enough to interrupt the flow, move it to `appendices/derivations/` and reference it by the section-based derivation label.

Derivation 2.3A belongs to the ADMC section under the eight-section structure. No renumbering is required while ADMC remains §2.3. The derivation was reframed around the additive positive oriented reading and its reflected counterpart on 2026-07-15, and §2.3 now carries the restored uniqueness pointer. Preserve the appendix's suggested citation sentence as the scope-safe template: the result is uniqueness within the natural additive and symmetry-compatible axis-wise class, not a global no-alternative theorem.

## Current chapter state

The chapter has a four-step opening dependency order followed by the interpretive and modifier sections:

1. notation
2. physical momentum configuration, branch magnitudes, and positive oriented reading
3. ADMC postulate and conserved positive sum
4. opposite-orientation inversion and inertial correspondence

Preserve this order. It keeps familiar energy and four-momentum language out of the foundational construction until the correspondence section.

### Section ownership

- `01-core-terms-and-variables.qmd` owns the compact primitive vocabulary and terminology note. It defers the physical organization to §2.2.
- `02-the-momentum-configuration.qmd` owns fermionic structure and fermic momentum, perpendicular bosonic geometry, the spherical internal particle cycle, the momentum triangle, swelling and directional asymmetry, the shell figures, limiting configurations, the arbitrary-direction bridge, positive branch magnitudes, the conditional partition, positivity, orientation reversal, and the zero-component convention.
- `03-admc.qmd` owns the ADMC postulate, the conserved $p_{\hat{k}}^\oplus$ sum, its compact algebraic form, the opposite-orientation conservation statement, and the scoped uniqueness pointer to Derivation 2.3A.
- `04-invertible-mapping.qmd` owns inversion of the opposite-orientation readings to `(M, p_k)`, conservation equivalence, four-component alignment, and SR correspondence review.
- `05-space-and-momentum-stage-and-actor.qmd` owns the stage/actor distinction: space as the rule-bearing stage that conditions available kinematic relations, momentum as the actor carrying changing physical content.
- `06-time.qmd` owns the interpretation of time, clocks, inertial dilation, material contraction, and true-frame language.
- `07-kinematic-modifiers.qmd` owns the KM definition and taxonomy: composition modifiers, yield modifiers, and admissibility modifiers.
- `08-what-foundations-establishes.qmd` owns the chapter-level close: what Foundations has established, what it has not established, and why gravity comes next.

### Boundary locks

- Do not restore a separate Foundations gravity-grammar section while the gravity chapter begins with `chapters/02-tier-2-engines/03-gravity-and-structured-spacetime/01-gravity-in-m1.qmd`.
- Foundations may mention gravity only as the next major case of a structured or deformed stage modifying local kinematics.
- Keep the detailed `source -> field -> observer` grammar, gravity-side variables, stationary field packaging, and observer bookkeeping in the gravity chapter.
- The bounded fermionic-cycle, bosonic-geometry, and spherical-cycle language in §2.2 belongs to the reader-facing spine. Do not extend it into torus, winding, detailed chirality, or full internal-geometry machinery without a reviewed theory basis.

### Terminology locks

- Use **fermic** and **bosic** for momentum quantities or momentum roles.
- Use **fermionic** and **bosonic** for structure, geometry, winding, chirality, or state labels.
- In Foundations, use `M = \sqrt{p_f^2 + p^2}` for the inertial composition rule. Present it as an M1 baseline commitment with a momentum-triangle interpretation, not as a result derived from perpendicularity alone.
- Keep `p` as bosic momentum. It has a spherical contribution and an asymmetry with a net direction. Use `p_k` for its directional components. Do not replace `p` with vector notation in the foundational definition; the vector representation is downstream.
- Treat `M` as representative of total momentum content, not as an independent primitive conservation law alongside ADMC.
- The shell extrema `M \pm p/2` belong to the net asymmetry direction, where `|p_k|=p`.
- For an arbitrary chosen direction, the positive branch magnitudes are `M \pm |p_k|/2`.
- For orientation `\hat{k}`, the conditional partition identifies the branch expression equal to `p_{\hat{k}}^\oplus=M+p_k/2`; reversing the orientation gives `p_{-\hat{k}}^\oplus=M-p_k/2`.
- ADMC uses one positive contribution per particle for each oriented direction. Do not say that one particle contributes both branches simultaneously.
- The readings for `\hat{k}` and `-\hat{k}` are complementary applications of ADMC to opposite orientations, not two simultaneous contributions for one orientation.
- At `p_k=0`, the branch magnitudes coincide at `M`; assigning the zero case to the `p_{k^+}` case of the partition is a bookkeeping convention only.
- Treat the `p_f=0` case as the purely bosic boundary of the inertial composition rule unless later reviewed theory supplies its full structural realization.
- M1 may take the directional-positive structure as foundational. Exact invertibility by itself establishes equivalence of the realized bookkeeping; it does not mathematically prove which description is deeper.

### Time / frame locks

- Time is a measure abstracted from physical change, not the actor of change.
- Clock language belongs first to systems with stable internal cycles; the clean primary clock-carrying role is fermic.
- Motion-induced dilation is read through changed fermic-to-bosic organization: `d\tau = dt\,p_f/M` in the inertial overlap regime.
- Gravity-induced dilation is only foreshadowed here; the gravity chapter owns local fermic contextualization by the field.
- The true-frame claim is an interpretive consequence of the momentum/space ontology: frame descriptions are plural, but the underlying physical now is singular. Do not present it as an additional equation derived in §2.6.

### Kinematic modifier locks

- A KM is a structured change in how momentum content becomes physical evolution.
- The reader-facing taxonomy is:
  - **composition modifiers**: change how fermic and bosic momentum are internally related or contextualized;
  - **yield modifiers**: change what directed bosic momentum produces as displacement or frequency-style expression;
  - **admissibility modifiers**: change which kinematic states are available at all.
- Avoid leading with arbitrary KM-A / KM-B / KM-C labels in manuscript prose unless an appendix or technical note needs them.
- Cosmology is the edge-case yield example; do not overdevelop it in Foundations.
- Gravity is the first later developed composition/contextualization case; do not rebuild the gravity chapter inside §2.7.

### Figure ownership

- The minimal momentum triangle belongs in §2.2 only.
- The shell panels belong in §2.2 only.
- §2.3 should not repeat the branch definitions or either figure.
- §2.4 should not repeat the triangle or shell figures unless a genuinely new visual argument is added.
- No gravity pipeline figure belongs in rendered Foundations under the current architecture; that visual grammar belongs in the gravity chapter.

### Figure interpretation locks

- The shell panels are a schematic two-view depiction of one momentum configuration.
- Panel (a) represents isotropic swelling from `p_f` to `M`.
- Panel (b) represents directional deformation of the swollen shell along the net asymmetry direction.
- The two views are representational rather than sequential; physically they belong to one combined momentum configuration.
- The shell deformation encodes the two positive branch magnitudes available along the net asymmetry axis. Do not present it as two simultaneous conserved contributions or as a measured spatial distribution of momentum density.
- Avoid caption or prose language that implies literal temporal evolution or momentum flowing out of the particle.

### Prose and structure guidance

- In §2.1, anchor terms in familiar physics, keep the section compact, and defer physical organization to §2.2.
- In §2.2, develop the physical configuration before choosing a direction, then define the branch magnitudes, conditional partition, positive oriented reading, and positivity bound. Preserve the distinction between bosic momentum `p`, its net asymmetry direction, and an arbitrary component `p_k`.
- In §2.3, state the ADMC postulate and lead with the conserved $p_{\hat{k}}^\oplus$ sum; give `M+p_k/2` second as its compact algebraic form.
- In §2.4, invert the opposite-orientation readings to recover signed `(M,p_k)`. Introduce energy and standard four-momentum here, not earlier.
- In §2.5, keep the stage/actor metaphor; do not replace it with abstract terminology. Make clear that the stage is not empty, rigid, or structureless: space already conditions closure, stability, motion, and local kinematic relations.
- In §2.6, keep the section centered on time, clocks, dilation, contraction, and true-frame status. Do not let it become a full philosophy-of-time essay.
- In §2.7, keep the KM definition lean and grounded in stage deformation modifying kinematics. Do not let the taxonomy become a glossary detached from the inertial baseline.
- In §2.8, close Foundations by naming what is established and what remains downstream. Avoid management language such as “this subsection does.”

### Tone guidance for Foundations

- Keep the prose explicit and reader-anchored.
- Favor confident definitions over repeated cautionary qualifiers.
- Use caution once, sharply, when role or status matters.
- Be careful with mechanistic language around shell figures and clock claims.
- Use interpretation sparingly and only after the formal role of a section is clear.
- End Foundations with a handoff to gravity, not a miniature gravity preview.
