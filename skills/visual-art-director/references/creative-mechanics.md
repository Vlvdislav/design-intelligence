# Creative mechanics + scene precision

Use ideas below as raw material, **never as copy-and-paste templates**:

- **Product immersion:** a strong hero object, background word, foreground cutouts, depth and controlled parallax.
- **Editorial story:** asymmetric image framing, large typography, varied section rhythm and intentional whitespace.
- **Spatial discovery:** selection changes the scene or foreground object; browsing is still clear without animation.
- **Kinetic type:** movement supports content hierarchy and transitions, not decoration.
- **Interactive explanation:** diagrams, annotations and meaningful changing states replace walls of marketing copy.

## Scene specification (internal, not a substitute for visuals)

For each artboard, work out:

```text
Scene: name + message + CTA
Canvas: desktop dimensions / mobile dimensions
Composition: main subject (x,y,w,h); text anchors; spacing/grid
Images: actual sources or art-directed assets; crops; layer order; shadows
Type/color: font, weights, sizes, contrast, reusable tokens
Interaction: trigger -> outgoing state -> incoming state
Motion: duration, easing, foreground/background travel, fallback
Figma: editable layers + keyframe/variant frames
QA: real screenshot checked at desktop and mobile
```

**Why exact prompts work:** they remove ambiguity with assets, coordinates, typography, state changes and acceptance checks. When given such a prompt, reproduce it faithfully. With an open brief, *invent and validate* equally concrete scene decisions before drawing.

If an asset or font is unavailable, report the specific substitution. Do not pretend that invented measurements were observed. Create variants for important hover/select/transition frames only if relevant. Do not use code to replace design work.
