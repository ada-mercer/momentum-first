# Figure: Directional source -> field -> observer

Status: draft-approved for gravity-chapter authoring
Created: 2026-04-25
Model: openai/gpt-image-2
Output: `figures/build/gravity-and-structured-spacetime/gravity-directional-source-field-observer.png`
Chapter: `manuscript/chapters/02-tier-2-engines/03-gravity-and-structured-spacetime/01-gravity-in-m1.qmd`
Figure id: `fig-gravity-directional-source-field-observer`

## Purpose

Conceptual, non-mathematical opener for the gravity-chapter grammar. The figure should show a localized directional momentum source, the field-like deformation around it, and a separated observer reading the resulting local conditions.

## Visual constraints

- No equations or mathematical symbols.
- No large title/subtitle inside the image; Quarto supplies the caption.
- Exactly three panels.
- Color continuity: amber/gold = source, cyan/blue = field, violet/purple = observer.
- Keep the source visibly directional, the field visibly around the source, and the observer visibly separated from the source.
- Avoid black-hole, galaxy, planet, star, or rubber-sheet spectacle imagery.

## Exact prompt lineage

The final checked image was produced by editing an earlier GPT Image 2 draft to remove the top title/subtitle while preserving the three-panel composition.

### Final edit prompt

```text
Edit the provided scientific diagram into a manuscript-ready figure without any top title or subtitle. Keep the three-panel layout, colors, panel headings, panel body text, arrows, arrow labels, and footer labels. Remove only the large top title area and subtitle area. Expand or reposition the three panels upward slightly so the figure has balanced margins and no empty top band. Do not add equations or new symbols. Keep exact panel text as much as possible. Maintain white/pale background, crisp vector-like style, amber source panel, blue field panel, violet observer panel. No logos, no watermark.
```

### Base-generation prompt

```text
Create a polished reader-facing scientific concept diagram for a physics book. It should be a conceptual companion to a later mathematical M1 source-field-observer figure, but WITHOUT equations.

Core idea: a specific directional momentum source deforms the surrounding spatial stage; that deformation appears as a structured field; an observer some distance away experiences the distortion through local clocks and motion.

Audience: serious broad-technical readers. Style: clean editorial scientific vector art, calm and authoritative, white/pale background, landscape 16:9, generous margins. Same color language: amber/gold for source/momentum, cyan/blue for field/spatial distortion, violet/purple for observer/local response.

Title at top, exact text:
From directional momentum to local gravity
Subtitle below title, exact text:
a source channel structures space; distant observers read the distortion

Three large rounded panels left-to-right connected by broad clean arrows. No equations, no Greek letters, no mathematical notation.

Panel 1 heading, exact text:
1. Directional momentum source
Panel 1 content, exact text:
A localized source carries momentum with a preferred direction.
Panel 1 footer, exact text:
source side
Visual: amber/gold localized compact source at center-left, with a clear single preferred direction arrow passing through or emerging from it, plus subtle paired flow lines suggesting directional momentum organization. Do NOT show many arrows converging inward like a force field. The emphasis is directional momentum, not attraction.

Arrow label from panel 1 to panel 2, exact text:
structures space

Panel 2 heading, exact text:
2. Field around the source
Panel 2 content, exact text:
The surrounding stage acquires a scalar well and directional shift.
Panel 2 footer, exact text:
field side
Visual: cyan/blue spatial grid around the same source, seen more abstractly. Show a shallow deformation around the source and a subtle sideways/swirl-like directional distortion aligned with the source momentum. It should feel analogous to a source-to-field map: the source is still visible as the cause, but the main object is the field pattern around it. Avoid black holes, event horizons, galaxies, stars, or rubber-sheet cartoon exaggeration.

Arrow label from panel 2 to panel 3, exact text:
sets local conditions

Panel 3 heading, exact text:
3. Distant observer response
Panel 3 content, exact text:
A nearby path and clock are read through the structured background.
Panel 3 footer, exact text:
observer side
Visual: violet/purple observer marker located at a clear distance away from the source/field, not sitting at the center. Show a small clock and a local trajectory/path segment near the observer, subtly affected by the blue field lines reaching that region. The observer should be downstream/outside the source region, reading the distortion locally.

Composition rules:
- Exactly three panels.
- No equations, no mathematical symbols, no Greek letters.
- Use consistent source/field/observer colors.
- Make it feel connected to a following formal source-field-observer diagram.
- Text must be crisp, correctly spelled, and fully legible.
- Use subtle scientific iconography, not cartoon style.
- No logos, no watermarks, no stars, no planets, no galaxies, no black hole event horizon.
- Avoid tiny text.
- The source should visibly have a preferred momentum direction; the field should visibly be around that source; the observer should visibly be separated from the source and affected at a distance.

Final mood: elegant, explanatory, physically intuitive. In five seconds the reader should grasp: directional momentum organizes the source, space carries the deformation as a field, and a distant observer experiences local gravitational conditions.
```

## Review notes

- Header/subtitle removed for Quarto caption control.
- Text is readable and correctly spelled in the checked output.
- Panel 1 includes faint counter-flow lines, but the dominant directional arrow carries the intended source-channel reading.
- Panel 2 remains slightly gravity-well-like; acceptable because the figure is conceptual and the text labels it as field structure rather than literal sinking.
