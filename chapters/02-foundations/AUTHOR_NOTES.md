# Foundations Author Notes

## Job of this part

Foundations is where the book begins to cash out its claims.

It should establish:
- primitive momentum terms and notation
- ADMC as the directional-positive conservation postulate
- the realized directional split and its inverse map
- the inertial SR correspondence in momentum-first variables
- the stage/actor distinction between space and momentum
- the time / clock / dilation interpretation
- the true-frame stance as an interpretive commitment, not a new inertial equation
- kinematic modifiers as the grammar for departures from the inertial baseline
- a clean closing statement of what Foundations has and has not established

It should **not** develop the gravity program. Part III now owns gravity as the first major engine.

## Local tone target

Foundations should feel:
- explicit
- disciplined
- technically cleaner than the Preface and Introduction
- sparse on rhetoric
- confident about M1's own commitments without overclaiming derivation status

This is where the framework either starts to hold together or it doesn't.

## Rendered file sequence

Current rendered Foundations sequence in `_quarto.yml`:
1. `02-01-core-terms-and-variables.qmd`
2. `02-02-admc.qmd`
3. `02-03-invertible-mapping.qmd`
4. `02-04-space-and-momentum-stage-and-actor.qmd`
5. `02-05-time.qmd`
6. `02-06-kinematic-modifiers.qmd`
7. `02-07-what-foundations-establishes.qmd`

Historical note:
- `02-07-minimal-gravity-grammar.qmd` is no longer rendered. Keep it out unless the architecture changes again.
- `02-08-scope-and-status.qmd` has been replaced by `02-07-what-foundations-establishes.qmd` as the rendered closer.

## Mode references

Use these as the default stack when writing or revising Foundations prose:
- `modes/roles/book-prose`
- `modes/topics/m1/foundations`
- `modes/artifacts/manuscript`
- `modes/styles/book-mainline`
- `modes/audiences/broad-technical`

## Derivations

If a derivation grows long enough to interrupt the flow, move it to `appendices/derivations/` and reference it by the section-based derivation label.

## Current rewrite state (2026-04-25)

The chapter now has a clearer division of labor across seven rendered files.

### Section ownership

- `02-01-core-terms-and-variables.qmd` owns the primitive vocabulary, the momentum triangle, and the terminology note.
- `02-02-admc.qmd` owns the ADMC postulate and its realized directional-positive split.
- `02-03-invertible-mapping.qmd` owns the forward/inverse map, conservation equivalence, four-component alignment, and SR correspondence review.
- `02-04-space-and-momentum-stage-and-actor.qmd` owns the stage/actor distinction: space as the rule-bearing stage that conditions available kinematic relations, momentum as the actor carrying changing physical content.
- `02-05-time.qmd` owns the interpretation of time, clocks, inertial dilation, material contraction, and true-frame language.
- `02-06-kinematic-modifiers.qmd` owns the KM definition and taxonomy: composition modifiers, yield modifiers, and admissibility modifiers.
- `02-07-what-foundations-establishes.qmd` owns the part-level close: what Foundations has established, what it has not established, and why gravity comes next.

### Boundary locks

- Do not restore a separate Foundations gravity-grammar section while Part III begins with `03-01-gravity-in-m1.qmd`.
- Foundations may mention gravity only as the next major case of a structured/deformed stage modifying local kinematics.
- Keep the detailed `source -> field -> observer` grammar, gravity-side variables, stationary field packaging, and observer bookkeeping in Part III.
- Do not let torus/cycle/chirality machinery enter Foundations except as hidden context for the writer; it is not part of the reader-facing Foundations spine.

### Terminology locks

- Use **fermic** and **bosic** for momentum quantities or momentum roles.
- Use **fermionic** and **bosonic** for structure, geometry, winding, chirality, or state labels.
- In Foundations, prefer `M = \sqrt{p_f^2 + p^2}` when presenting the baseline composition relation in prose.
- Keep `p` as bosic momentum magnitude and `p_k` as directional components of `\vec p`.
- Treat `M` as representative of total momentum content, not as an independent primitive conservation law alongside ADMC.

### Time / frame locks

- Time is a measure abstracted from physical change, not the actor of change.
- Clock language belongs first to systems with stable internal cycles; the clean primary clock-carrying role is fermic.
- Motion-induced dilation is read through changed fermic-to-bosic organization: `d\tau = dt\,p_f/M` in the inertial overlap regime.
- Gravity-induced dilation is only foreshadowed here; Part III owns local fermic contextualization by the field.
- The true-frame claim is an interpretive consequence of the momentum/space ontology: frame descriptions are plural, but the underlying physical now is singular. Do not present it as an additional equation derived in 2.5.

### Kinematic modifier locks

- A KM is a structured change in how momentum content becomes physical evolution.
- The reader-facing taxonomy is:
  - **composition modifiers**: change how fermic and bosic momentum are internally related or contextualized;
  - **yield modifiers**: change what directed bosic momentum produces as displacement or frequency-style expression;
  - **admissibility modifiers**: change which kinematic states are available at all.
- Avoid leading with arbitrary KM-A / KM-B / KM-C labels in manuscript prose unless an appendix or technical note needs them.
- Cosmology is the edge-case yield example; do not overdevelop it in Foundations.
- Gravity is the first later developed composition/contextualization case; do not rebuild the gravity chapter inside 2.6.

### Figure ownership

- The minimal momentum triangle belongs in `02-01` only.
- The shell panels belong in `02-02`, not in `02-01`.
- `02-03` should not repeat the triangle figure unless it is doing genuinely new work.
- No gravity pipeline figure belongs in rendered Foundations under the current architecture; that visual grammar belongs in Part III.

### Figure interpretation locks

- The shell panels in `02-02` are a schematic two-stage depiction.
- Panel (a) represents an isotropic swelling from `p_f` to `M`.
- Panel (b) represents directional deformation of the swollen shell.
- The two stages are representational rather than sequential; physically they belong to one combined momentum configuration.
- Avoid caption or prose language that implies literal temporal evolution unless the framework text explicitly locks that stronger claim.

### Prose/structure guidance now locked

- In `02-01`, anchor terms in familiar physics before introducing M1 reinterpretation.
- In `02-02`, state the postulate first, then unpack it.
- Distinguish clearly between the deeper ADMC postulate and the present realized split used in the book.
- In `02-03`, invoke the momentum triangle as already established rather than re-teaching it.
- In `02-04`, keep the stage/actor metaphor; do not replace it with abstract terminology. Make clear that the stage is not empty, rigid, or structureless: space already conditions closure, stability, motion, and local kinematic relations.
- In `02-05`, keep the section centered on time/clocks/dilation/contraction/true-frame status. Do not let it become a full philosophy-of-time essay.
- In `02-06`, keep the definition lean and grounded in stage deformation modifying kinematics. Do not let the taxonomy become a glossary detached from the inertial baseline.
- In `02-07`, close the part by naming what is established and what remains downstream. Avoid management language such as “this subsection does.”

### Tone guidance for Foundations

- Keep the prose explicit and reader-anchored.
- Favor confident definitions over repeated cautionary qualifiers.
- Use caution once, sharply, when role/status matters.
- Be careful with mechanistic language around shell figures and clock claims.
- Use interpretation sparingly and only after the formal role of a section is clear.
- End the part with a handoff to gravity, not a miniature gravity preview.
