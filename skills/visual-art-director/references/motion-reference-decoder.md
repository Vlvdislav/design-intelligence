# Motion / interaction specimen decoder — from impressive examples to original Figma concepts

## Purpose

Users may supply MotionSites-style recreation prompts, demo URLs, screenshots, GIFs or videos. A specification for a coded hero is **not** a command to code it. Treat it as a reference revealing how an experienced director defines art, scene, assets, screen hierarchy, interaction and acceptance. Extract the *design grammar*, then create a new concept for the actual product.

Do not silently replicate copyrighted media, another brand's interface, URL-specific resources, exact copy or proprietary visual identity. If a user explicitly requests a faithful reproduction and has permission, distinguish that scope from original ideation; otherwise be inspired by principles, not the copy.

## Decode to a seven-part Creative Scene Card

For each relevant reference produce a short structured analysis:

1. **Hero thesis** — a one-line promise + specific moment the user should experience. Why is this more than a decorative hero?
2. **Visual anchor** — person/object/scene, positioning, shot size, camera angle, negative space, lighting, texture, material, palette and contrast. Identify *what must be a genuine asset*: hero plate, product, transparent person, video/3D render, crop variants.
3. **Page choreography** — order of seeing: anchor → brand promise → microproof → interaction → CTA. The composition must direct attention even as a static image.
4. **Information architecture** — main labels, buying tasks, navigation, controls and where the visitor can recover if the scene is confusing.
5. **Interaction signature** — input → visible response → state change → next action; decide whether depth, scan, scroll, cursor follow or reveal has meaning. Specify keyboard/touch/low-motion equivalents.
6. **States and device strategy** — identify idle, hover/focus, activated, 50% transition, settled and exceptional states. Phone layout is **re-authored**, not 1440px shrunk.
7. **Evidence and risk** — screenshot or timestamp that supports observation, UX risk, implementation complexity and what remains unverified.

Label observations `[OBSERVED]`, user-provided instructions `[USER]`, proposed mechanics `[PROPOSED]`. A long exact-recreation prompt alone is not proof the referenced site has been built, behaves as described or achieves conversion.

## Case A — KAIRN-style editorial campaign (from user-provided example)

Useful grammar:

- **One authored photographic plate + optional motion plate:** the dramatic image carries the composition. The interface is subordinate, placed in available negative space. Photo/video coherence is deliberate; do not solve everything with decorative CSS layers.
- **Highly structured editorial hierarchy:** distinct display face (wide headline, outline word), restrained UI font, a contrast accent (ice cyan), restrained secondary color (cream), and precise placement of navigation, product, lens story and CTA.
- **Content cluster is a visual device:** asymmetrical tile set juxtaposes story, model/product, circular progress and typography. Different information densities may coexist.
- **Choreography belongs to concept:** sequential arrival and drifting photo detail communicate pace. In Figma, show keyframes/timing annotations, not claims of a working MP4 loop.
- **Portrait adaptation is a redesign:** headline, hero image, tiles, story and CTA change priority rather than merely scale.

**Not to copy:** KAIRN name, source imagery, exact measurements, cyan palette or same 2×2 cards by default. These are attributes of the example, not a universal template.

## Case B — VELL-style character studio (from user-provided example)

Useful grammar:

- **A persistent centre-stage subject** + utility panels around it. User sees the change in context instead of navigating away.
- **Registered asset consistency:** the same person, pose, crop, lighting and scale across visual states; otherwise a swap animation will break the illusion.
- **Control-system design:** top tabs, subnavigation, outfit grid, details, history, adjustments and save are an **interaction model**, not merely floating glass decoration.
- **Explicit state machine:** choosing a look changes the hero, corresponding avatar, row details, selection indicator and history; undo/redo must be reflected in the designed states.
- **Signature reveal:** scan-line/wipe has states that need storyboard frames, exact layer relationships and product continuity; describing a scan is not enough.

**Not to copy:** the person's identity, appearance, preset text, 1600×900 coordinates or 8-look dataset. For commerce, only surface controls that the user's use case actually requires.

## Reference-to-concept transformation

Never go `reference prompt → React/HTML → screenshot → call it a concept`. Go:

`reference → Creative Scene Cards → distinct brand-specific theses → asset plan → visual thumbnail frames → native editable Figma screens → state storyboard → screenshot critique → comparison board`.

Use a *translation statement* for each concept:

> “Borrowed principle: cinematic full-bleed plate / persistent object-state hub. Original application: [specific product goal]. Different art direction: [not reference colors/type/layout]. Reason it works: [task or brand narrative]. Risk: [discoverability/performance/accessibility].”

The user should not need to provide animation curves, precise layer positions, library names or image crop percentages to get a serious first concept. The designer proposes, renders, checks and iterates those choices.
