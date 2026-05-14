# Figure: Stationary gravity grammar

Status: draft-approved for gravity-chapter authoring
Created: 2026-04-25
Model: openai/gpt-image-2
Output: `figures/build/gravity-and-structured-spacetime/stationary-gravity-grammar.png`
Chapter: `chapters/02-tier-2-engines/03-gravity-and-structured-spacetime/01-gravity-in-m1.qmd`
Figure id: `fig-stationary-gravity-grammar`

## Purpose

Formal companion to the conceptual directional-source figure. The figure shows the gravity-chapter stationary grammar as a reader-facing source -> field -> observer pipeline with the minimal variables the chapter introduces.

## Visual constraints

- No large title/subtitle inside the image; Quarto supplies the caption.
- Exactly three panels.
- Use the same visual language as the conceptual figure: amber/gold source, cyan/blue field, violet/purple observer.
- Keep formulas sparse and legible; do not add derivation detail.
- The image is a manuscript diagram, not a derivation trust layer. Exact derivations remain in prose/appendix support.

## Exact prompt lineage

The final checked image was produced by editing an earlier detailed source -> field -> observer diagram to remove the top title/subtitle and normalize the panel text.

### Final edit prompt

```text
Edit the provided three-panel scientific diagram into a manuscript-ready figure without any top title or subtitle. Keep the three-panel source -> field -> observer structure and color language, but remove the large top title/subtitle. Expand or reposition the panels upward for balanced margins.

Keep only panel-level text and short labels. The final diagram should have exactly three panels:

Panel 1 heading: 1. Source layer
Panel 1 contents:
Directional channels: J_k^+ , J_k^-
Even channel: M_k = (J_k^+ + J_k^-)/2
Odd channel: P_k = J_k^+ − J_k^-
Footer: source side

Panel 2 heading: 2. Stationary field layer
Panel 2 contents:
Scalar well: θ_0
Shift field: A_i
Flux: B_ij = ∂_i A_j − ∂_j A_i
Clock factor: G = √(1 − 2θ_0)
Footer: field side

Panel 3 heading: 3. Observer bookkeeping
Panel 3 contents:
Contextual fermic scale: p_f,c = p_f G
Transport momentum: Π_i
Local magnitude: M_g,loc
Stationary generator: H_g,stat
Footer: observer side

Arrow label from panel 1 to 2: sources drive fields
Arrow label from panel 2 to 3: fields modify local kinematics

Hard requirements: no top title, no subtitle, no extra panels, no extra formulas, no logos, no watermark. Keep text crisp, legible, and math-like. Use white/pale background. Keep the style clean, refined, vector-like, scientific, and book-ready.
```

### Base-generation prompt

```text
Create a polished, reader-facing scientific book diagram for a physics manuscript titled Momentum First. The figure explains the M1 stationary gravity grammar as a three-stage pipeline: SOURCE LAYER → STATIONARY FIELD LAYER → OBSERVER BOOKKEEPING.

Audience: serious broad-technical readers. The figure should be elegant, precise, uncluttered, suitable for inclusion in a Quarto/PDF physics book. It should look like high-quality editorial scientific vector art, not a flashy poster.

Canvas: landscape 3:2 or 16:10 composition, clean light background, ample margins, high contrast, vector-like edges, no photorealism. Use three large rounded panels arranged left-to-right, connected by clear arrows. Use subtle color coding: warm amber for Source, cool blue/cyan for Field, muted violet for Observer. White or very pale background. Thin grid or faint spatial-stage texture may appear behind the panels, but keep it subtle.

Main title at top, exact text:
“M1 stationary gravity grammar”
Subtitle below title, exact text:
“source → field → observer bookkeeping”

Panel 1 heading, exact text:
“1. Source layer”
Panel 1 content, exact text, typeset cleanly:
“Directional channels”
“J_k^+ , J_k^-”
“Even channel:  M_k = (J_k^+ + J_k^-)/2”
“Odd channel:   P_k = J_k^+ − J_k^-”
Small caption at bottom of panel 1:
“organized momentum content”

Panel 2 heading, exact text:
“2. Stationary field layer”
Panel 2 content, exact text, typeset cleanly:
“Scalar well:  θ_0”
“Shift field:  A_i”
“Flux:  B_ij = ∂_i A_j − ∂_j A_i”
“Clock factor:  G = √(1 − 2θ_0)”
Small caption at bottom of panel 2:
“structured spacetime background”

Panel 3 heading, exact text:
“3. Observer bookkeeping”
Panel 3 content, exact text, typeset cleanly:
“Contextual fermic scale:  p_f,c = p_f G”
“Transport momentum:  Π_i”
“Local magnitude:  M_g,loc”
“Stationary generator:  H_g,stat”
Small caption at bottom of panel 3:
“local clocks and transport”

Between panel 1 and 2 place a clean arrow labelled:
“sources drive fields”
Between panel 2 and 3 place a clean arrow labelled:
“fields modify local kinematics”

Visual metaphors, subtle only:
- In the source panel, show small paired directional arrows or plus/minus source streams merging into even and odd channels.
- In the field panel, show a gently curved spatial grid or shallow well plus a faint rotational swirl to represent scalar well and shift without looking like a black hole illustration.
- In the observer panel, show a small clock glyph and a small trajectory/transport line near a local observer marker.

Style constraints:
- Clean mathematical typography; formulas must be legible and not crowded.
- Plenty of whitespace inside each panel.
- No dense paragraphs.
- No random extra formulas.
- No unrelated physics symbols.
- No logos, watermarks, decorative stars, planets, galaxies, or photorealistic objects.
- Do not add extra panels or additional stages.
- Do not use dark-mode slide styling.
- Avoid tiny text; every label should be readable at book-column scale.
- If perfect formula rendering is difficult, prioritize clean layout and leave formulas minimal rather than inventing incorrect equations.

Composition goal: A calm, authoritative diagram that makes the reader immediately understand that M1 gravity is layered: source bookkeeping first, field structure second, observer-side local readout third.
```

## Review notes

- Header/subtitle removed for Quarto caption control.
- Figure is visually strong and pairs well with the conceptual source-field-observer figure.
- AI-rendered formulas are legible and broadly correct, but should be treated as draft-approved rather than final publication typography.
- If this becomes a final publication figure, rebuild deterministically as SVG or manually typeset the formula labels.

## Revision — 2026-04-25, no header + directional-channel tail markers

Updated the checked output to remove the internal title/subtitle and correct source-layer arrow iconography:
- `J_k^+` arrows point right with the plus marker at the left tail: `⊕ --->`.
- `J_k^-` arrows point left with the minus marker at the right tail: `<--- ⊖`.
- The same tail-marker convention is used in the directional, even-channel, and odd-channel source mini-icons.

### Revision prompt

```text
Edit the provided scientific figure. Preserve the successful three-panel layout, colors, typography, formulas, panel headings, icons, and arrows as much as possible.

Make only these changes:

1. Remove the large top title and subtitle entirely:
- Remove “M1 stationary gravity grammar”
- Remove “source → field → observer bookkeeping”
Then move the three panels upward slightly or rebalance vertical spacing so there is no empty top band. Keep a clean manuscript-ready figure without an internal header.

2. In the SOURCE LAYER panel only, revise the small plus/minus channel arrow icons so each circular plus/minus marker sits at the TAIL / START of its arrow:
- For J_k^+ / positive channel arrows that point RIGHT, draw the plus circle at the LEFT tail, like: ⊕ --->
- For J_k^- / negative channel arrows that point LEFT, draw the minus circle at the RIGHT tail, like: <--- ⊖
- Do this consistently in the Directional channels, Even channel, and Odd channel mini-icons.
- Keep J_k^+ arrows pointing right.
- Keep J_k^- arrows pointing left.
- Do not place the minus circle in the middle of the arrow; it should be at the right-side tail/start of the left-pointing arrow.

Keep all mathematical text unchanged and legible.

Hard constraints:
- Exactly three panels.
- No title/subtitle inside the image.
- No extra equations, no added labels, no logos, no watermark.
- Keep the refined physics-book style.
- Preserve the panel footers: organized momentum content, structured spacetime background, local clocks and transport.
- Preserve arrow labels between panels: sources drive fields; fields modify local kinematics.
```

## Revision — 2026-04-25, clearer source packaging + calmer field/observer panels

Updated the checked output to the packaging-cleaner version after review. This version improves the source-side visual semantics and reduces decorative clutter in the field/observer panels:
- Even channel now reads more clearly as symmetric/additive packaging into a central `M` package.
- Odd channel now reads more clearly as directional imbalance/difference packaging into `P`.
- Field and observer icons are lighter and more subordinate to the formulas.

Output adopted:
`figures/build/gravity-and-structured-spacetime/stationary-gravity-grammar.png`

Source generation artifact before adoption:
`/home/arne/.openclaw/media/tool-image-generation/stationary-gravity-grammar-packaging-cleaner---cae9949c-b5e7-461d-8d4d-b0cc2ac1eac4.png`

### Revision prompt

```text
Edit the provided scientific figure with two focused improvements. Preserve the successful overall style: three tall rounded panels, light manuscript background, amber source panel, cyan stationary field panel, violet observer panel, serif-like typography, no top title/subtitle, clean connecting arrows.

Improvement 1: Make the SOURCE LAYER mini-icons explain the M and P packaging better.
- Keep J_k^+ arrows pointing RIGHT with plus marker at the left tail: ⊕ --->
- Keep J_k^- arrows pointing LEFT with minus marker at the right tail: <--- ⊖
- Directional channels section: show the two opposite directional channel arrows cleanly and separately.
- Even channel section: make the two opposite channel arrows feed symmetrically into a central rounded/merged package labelled M. It should visually read as balanced addition / symmetric packaging, not two loose arrows simply colliding. Use a small central merge node or bracket if helpful. Keep the equation M_k = (J_k^+ + J_k^-)/2.
- Odd channel section: make the two opposite channel arrows feed into a difference/imbalance package labelled P. It should visually read as directional imbalance / difference channel, distinct from the M packaging. A brace or offset imbalance marker is fine, but it should be cleaner than the current version. Keep the equation P_k = J_k^+ − J_k^-.

Improvement 2: Calm the visual clutter in panels 2 and 3.
- Keep all formulas and headings unchanged and legible.
- Make icons in panels 2 and 3 smaller and more subordinate to the math labels.
- In panel 2, reduce decorative clutter: the scalar well, shift swirl, flux marker, and clock factor should be simple and airy. Remove unnecessary extra strokes if needed.
- In panel 3, keep the clock/trajectory/local magnitude/stationary generator icons, but make them lighter and less visually dominant.
- Preserve generous whitespace and avoid crowding.

Do not change these texts:
Panel headings: 1. Source layer; 2. Stationary field layer; 3. Observer bookkeeping.
Panel footers: organized momentum content; structured spacetime background; local clocks and transport.
Arrow labels: sources drive fields; fields modify local kinematics.
Formulas: J_k^+ , J_k^- ; M_k = (J_k^+ + J_k^-)/2 ; P_k = J_k^+ − J_k^- ; θ_0 ; A_i ; B_ij = ∂_i A_j − ∂_j A_i ; G = √(1 − 2θ_0) ; p_f,c = p_f G ; Π_i ; M_g,loc ; H_g,stat.

Hard constraints: exactly three panels, no top title/subtitle, no extra equations, no logos, no watermark, no black holes or planets. Keep it book-ready and crisp.
```

## Current review note

This is the current adopted formal gravity-chapter stationary grammar figure. It is authoring-grade and visually improved over the previous version. As with all prompt-backed figures, formula text should still receive final publication review before locking a print-ready edition.
