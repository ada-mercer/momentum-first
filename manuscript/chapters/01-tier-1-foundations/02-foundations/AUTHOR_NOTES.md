# Author notes — Chapter 02 Foundations

Status: current working chapter-local state notes; prepared for v0.4.2
Mode stack: roles/book-prose + topics/m1/foundations + artifacts/manuscript + styles/book-mainline + audiences/broad-technical

## Chapter burden

Foundations turns the Introduction's momentum-first wager into a usable grammar. It must name the primitive momentum roles, assemble the inertial particle configuration, state ADMC as the conservation principle, recover familiar inertial four-momentum, and then give the interpretive grammar for space, time, clocks, and structured departures from inertial motion.

The chapter should establish:

- the reader-facing reason Foundations is needed before later engines;
- fermic momentum `p_f`, bosic momentum `p`, and core momentum `M`;
- directional notation: `\vec p`, `p_k`, `p^\pm`, `p_k^\pm`, and `p^\perp`;
- the physical momentum configuration joining fermic and bosic roles;
- the inertial composition rule `M=\sqrt{p_f^2+p^2}` and its momentum-triangle interpretation;
- directional shell readings as positive scalar readings;
- ADMC as conservation of one positive shell reading per particle for each oriented direction;
- inversion from opposed readings back to `(M,p_k)` and the exact inertial correspondence with special-relativistic four-momentum;
- space as the stage and momentum as the actor of physical change;
- time as measured physical change, with clocks treated as physical systems sustained by internal cycles and interactions;
- the true-frame stance as interpretive, not an extra inertial equation;
- kinematic modifiers as the foundation-level vocabulary for structured changes in how momentum configuration yields motion;
- a close that names what Foundations establishes and what later engines must still supply.

Foundations should not build the gravity, quantum, expansion, or Part 0 geometry programs. Those chapters own their mechanisms. Foundations supplies the grammar that lets the reader recognize what those engines are doing.

## Active rendered structure

`index.qmd` renders nine included sections:

1. `01-what-foundations-must-fix.qmd` — chapter burden and reader contract.
2. `02-core-momentum-terms-and-directional-notation.qmd` — compact notation gateway.
3. `03-the-momentum-configuration.qmd` — physical configuration, momentum triangle, shell readings, positivity.
4. `04-admc.qmd` — ADMC postulate and conserved positive shell-reading sum.
5. `05-invertible-mapping.qmd` — inversion and inertial SR correspondence.
6. `06-space-and-momentum-stage-and-actor.qmd` — stage/actor interpretation and SMC entry.
7. `07-time.qmd` — time, clocks, inertial dilation, contraction, true-frame stance.
8. `08-kinematic-modifiers.qmd` — structured changes in momentum-to-motion relation.
9. `09-what-foundations-establishes.qmd` — chapter synthesis and downstream boundary.

Preserve this sequence. The first five sections build the formal inertial grammar. Sections 6–8 interpret the grammar and prepare later engines. Section 9 closes the chapter without importing a miniature gravity chapter.

## Section ownership

- `01-what-foundations-must-fix.qmd` owns the opening contract: primitive quantities, conservation language, inertial recovery, stage/actor interpretation, clock stance, and the boundary between Foundations and later engines.
- `02-core-momentum-terms-and-directional-notation.qmd` owns the table-style symbol gateway. It should remain compact and defer physical construction to §2.3.
- `03-the-momentum-configuration.qmd` owns the particle momentum configuration: fermic cycle, bosic role, perpendicular composition, core momentum, shell representation, net asymmetry, arbitrary-direction readings, and positivity.
- `04-admc.qmd` owns the ADMC postulate: for an isolated system and chosen orientation, the conserved quantity is the sum of one positive shell reading per particle.
- `05-invertible-mapping.qmd` owns the return from shell readings to familiar inertial quantities, including the exact correspondence with the standard energy-momentum package.
- `06-space-and-momentum-stage-and-actor.qmd` owns the first interpretive order: space supplies structured conditions; momentum carries change; forces are space-mediated momentum coupling.
- `07-time.qmd` owns clock language, inertial dilation, material contraction, and the true-frame commitment.
- `08-kinematic-modifiers.qmd` owns the definition of a kinematic modifier as a physical feature of space that changes how a particle's momentum configuration yields motion.
- `09-what-foundations-establishes.qmd` owns the synthesis and the handoff to gravity as the first later engine.

## Stable distinctions and terminology

- Use **fermic** and **bosic** for momentum roles and quantities in Foundations.
- Reserve **fermionic** and **bosonic** for later geometry, winding, chirality, or state labels. Section 2 may state this terminology boundary, but section 3 should otherwise stay with fermic/bosic language.
- `p_f` is identity-associated fermic momentum. It is fixed at the inertial baseline by `p_f=m_0c`.
- `p` is bosic momentum. It contributes to the spherical shell and, when directionally imbalanced, gives the particle translational momentum.
- `M` is core momentum: the total momentum content of the inertial configuration, with baseline composition `M=\sqrt{p_f^2+p^2}`.
- At the foundation level, perpendicularity is read from the Pythagorean composition rule: fermic and bosic roles enter as independent legs of one configuration. Do not introduce Part 0 manifold language here.
- The spherical shell is a representation of one internal momentum configuration, not a temporal mechanism, measured density, or external momentum flow.
- Along the net asymmetry direction, the positive readings are `p^\pm=M\pm p/2`.
- Along an arbitrary oriented unit direction `\hat{k}`, the signed component is `p_k=\vec p\cdot\hat{k}` and the positive readings are `p_k^\pm=M\pm p_k/2`.
- `p^\perp=M` is the perpendicular reading when `p_k=0`.
- Superscripts `+` and `-` label opposed positive readings; they are not signs attached to negative scalar values.
- Reversing `\hat{k}` exchanges `p_k^+` and `p_k^-`.
- ADMC uses one positive shell reading per particle for a chosen orientation. Do not describe one oriented ADMC sum as containing both readings from the same particle.
- The side-by-side pair `(p_k^+,p_k^-)` belongs to inversion, comparison, and orientation reversal, not to a single oriented conservation sum.
- Treat massless or purely bosic cases only at the level supported by the current text. Do not use Foundations to build their full internal geometry.

## Time, clocks, and frame status

- Time is a measure abstracted from physical change, not an actor that drives change.
- Clock language belongs to physical systems with repeatable cycles. A material clock counts a process sustained by interactions among constituents.
- Fermic momentum does not by itself fix an absolute cycling rate in every setting. Motion can slow a fermic cycle relative to a reference while `p_f` remains fixed.
- In the inertial overlap regime, `d\tau = dt\,p_f/M` gives the moving ideal-clock rate relative to the chosen inertial frame.
- Gravity can change the resting cycle comparison itself. Foundations may foreshadow that distinction; the gravity chapter owns its mechanism and material-clock scope.
- The true-frame claim is interpretive: frame descriptions are plural and operationally usable, but the underlying physical now is singular in the momentum/space ontology. Do not present it as an additional inertial equation.

## Kinematic modifiers

The current reader-facing definition is:

> A kinematic modifier is a physical feature of space that changes how a particle's momentum configuration yields motion.

A modifier is a role that later engines fill with specific structure. Foundations should keep the concept lean: a structured physical setting can leave a particle's momentum content recognizable while changing translation rate, local cycling, light propagation, or material equilibrium.

Use gravity and expansion as examples of the shared question, not as a merged mechanism. Gravity changes the local stage through organized momentum. Expansion dresses the bosic slot in the homogeneous stage model. Possible state-space effects remain open and should not be promoted to established modifier mechanisms.

## Boundaries

- Do not restore a separate Foundations gravity-grammar section. Gravity owns source, deformation, particle response, field dynamics, and GR correspondence.
- Do not move energy or standard four-momentum into the initial definition of the momentum roles. They enter after the shell-reading structure has been built and inverted.
- Do not turn non-particle-bound momentum into a completed gravity source in Foundations.
- Do not introduce torus, manifold, winding, chirality, or full internal-geometry machinery into the mainline Foundations prose.
- Do not use defensive guardrail clusters. State the positive physical role first; give only the local boundary needed to prevent a concrete misunderstanding.

## Figure ownership and interpretation

- The momentum triangle belongs in §2.3 as the visual interpretation of `M=\sqrt{p_f^2+p^2}`.
- The shell panels belong in §2.3 as two views of one internal momentum configuration: symmetric swelling from `p_f` to `M`, and directional asymmetry whose opposed readings differ by `p`.
- The directional-readings figure belongs in §2.3 near the transition from net-axis readings to arbitrary chosen direction.
- Figure prose should teach what the reader should see, not police every possible misuse. Keep necessary boundaries compact: shell deformations represent internal momentum organization, not measured external density or momentum flowing out of the particle.

## Tone target

Foundations should be direct, explicit, and spare. It is more technical than the Introduction, but it should still teach by physical sequence:

physical role -> symbol -> equation -> consequence -> boundary.

Prefer concrete physical wording over administrative phrases such as “the term names a job” or “this section introduces.” Avoid review-report language and repeated “not X” guardrails. The chapter should sound like the framework is being built in front of the reader, one stable commitment at a time.
