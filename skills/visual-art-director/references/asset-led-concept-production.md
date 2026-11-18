# Asset-led art direction — visual quality must be designed before decorative UI

## The key observation

For cinematic landing pages the impressive effect is often **80% source composition, lighting, photography/CG and coherent art direction**, not clever CSS. A large transparent mascot or product on a generic gradient cannot replace a compelling scene. Design the *media system* and interface together.

## Asset dossier (required for promo/brand/visual-heavy concepts)

Record for each principal asset:

| Field | What to specify |
|---|---|
| Role | hero plate, model/mascot, product close-up, transition layer, proof image |
| Source | user-provided / licensed / original generated / placeholder (clearly marked) |
| Camera | wide or portrait, focal length feel, angle, crop, placement, eyeline, perspective |
| Continuity | subject identity, light direction, surface, product texture, palette, shadow, pose |
| Stage fit | negative space reserved for actual UI, desktop/mobile crops, object-safe area |
| Native Figma | image fill/cropped image layer; UI remains editable text/vectors/components |
| Motion relation | static plate, separate loop/video, keyframe variant or simulated still state |
| Risk | uncanny anatomy, off-brand mascot, fake product, licensing, missing mobile crop |

## Make the art before polishing the UI

1. Draft **3 materially different scene thumbnails**. Name the primary subject, framing, amount of negative space, information density and eye path. Reject generic centre-object + symmetric benefit-cards composition before rendering.
2. Generate/source the **hero composition for each concept**, not a random pack of unrelated product photos. Preserve the user's mascot silhouette, marks and colors if supplied. A brand mascot is not permission to turn a marketplace into a children's property.
3. Critique the 3 plates as **art direction without UI**: realism, scale, coherent shadows, visual specificity, foreground/midground/background, product recognizability, legibility zones, mobile crop. Rework a broken plate before Figma assembly.
4. Design the type system in relation to the asset. Choose display family based on language, brand tone and glyph support; use a distinct UI family only when it improves readability. Avoid defaulting to Inter/oversized bold for every project.
5. Assemble **editable interface layers** over the plate using Figma. Buttons, words, navigation, price, descriptions, controls and cards must not be baked into the generated image.
6. Make a distinct **mobile art-directed layout**. Where necessary use different crop and content order; do not force a desktop plate into a narrow screen.
7. Add storyboard frames for meaningful micro-interactions and scene transitions. Mark simulated effects explicitly.

## Coherence tests

- **Remove the UI:** is the hero image still distinctive, visually meaningful and specific to the brand?
- **Remove the image:** do hierarchy, CTA, labels and navigation still make sense?
- **Blur everything:** is the attention path clear from major shapes and contrast?
- **Remove the mascot:** is the brand still recognizable through a distinct visual system?
- **Replace the logo:** if the result works unchanged for ten unrelated brands, the art direction is generic.
- **Show on a phone:** is the important product/object and CTA still visible without relying on hover?

## Figma best practice for expressive layouts

- Use **absolute layout / layered frames** for scenes, art-directed overlays and intentionally overlapping objects, not Auto Layout for every decorative element.
- Use **Auto Layout and real component instances** for structured controls, repeated tiles, tabs, cards, forms, navigation and product summaries.
- Keep text selectable and vector icons editable; do not use a screenshot of a completed UI as a substitute for native design.
- Store image variants, masks and crop decisions in named groups. Add focus-safe areas and contrast overlays as editable shapes.
- For hero video, provide a poster still and a storyboard or linked reference. Figma does not inherit continuous video physics from code by virtue of layered images.

## Consumer commerce priority

A striking scene must not hide search, category navigation, price/benefits, delivery constraints, trust or purchase path where the task requires them. A speculative 3D orbital carousel may belong in a curated promo or product experience, not as a mandatory navigation replacement for a 40,000-item catalogue. Record the normal task-flow alternative explicitly.
