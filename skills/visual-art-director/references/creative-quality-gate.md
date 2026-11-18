# Creative Quality Gate — stop generic landing pages before user review

> Mandatory for promo pages, brand campaigns, editorial landings and experimental storefronts. Read this at brief intake AND before making the first Figma composition. This is an internal art-direction review, not a validated conversion predictor or guarantee of user delight.

## What counts as failure

A visually tidy screen can still be conceptually weak. Reject a draft before showing it if the dominant composition could plausibly be produced for dozens of unrelated brands by swapping the logo and hero image. Typical failure pattern:

- centered mascot/character within a plain circular badge or glow
- generic H1 of the form “Welcome to <brand>”, two standard CTAs
- three identical icon benefit cards below, gradients or glass around everything
- decorative bubbles, floating emojis, sparkles, confetti, pill tags without meaningful relation to product
- blank hero with no clear reason to explore, buy, subscribe or learn
- 3D/WebGL added as a rotating decoration with no impact on comprehension or interaction
- huge text compensating for weak art direction; stock typography and random effects
- mascot looks like a toddler/children's brand because of cartoon props or toy-like pastel treatment without a brief that calls for it
- all three concepts share the same central hero + 3-card architecture and differ by colors or wording

**Do not fix a failed concept by adding particles, gradients, corner radius, shadows, WebGL or more text. Recompose the scene from its structural idea.**

## The KAIRN/VELL lesson: polished experience is not a component count

A cinematic premium campaign must derive its hero quality from **a strong photographed or art-directed scene**, deliberate text/negative-space relationship, and coordinated layers. A control-rich interactive experience must have **real product states** and content consistency rather than decorative glass panels. Source examples may arrive as 500-line recreation prompts; treat them as end-state blueprints and extract the *design grammar*, never as a request to implement their HTML or to copy their layouts. See `motion-reference-decoder.md`, `asset-led-concept-production.md` and `figma-motion-storyboard.md`.

Reject if:

- a stack of unrelated generated product images is substituted for one coherent hero plate;
- all the creative effort goes into a rounded white info card while scene, camera and lighting remain generic;
- the mascot has no designed relationship to commerce actions (only smiles/waves);
- the design promises 3D/parallax/try-on but has no storyboard or matching selected state;
- the Figma deliverable is only a screenshot of a generated UI;
- the designer produced code instead of the requested concept or Figma frames.

## Before illustration or Figma, author a one-page Concept DNA

1. Brand truth: user-supplied facts vs assumptions. State what should be felt about this specific brand, not “modern and premium”.
2. Hero proposition: what the visitor understands in 5 seconds, and what action follows.
3. Distinctive organizing metaphor: marketplace as gallery / room / journey / curated ecosystem, etc. One justified metaphor, not a default.
4. Art-direction rules: subject scale, spatial layers, shot angles, lighting, material palette, contrast, cropping, empty-space behavior, typographic relationship to imagery.
5. User behavior: the gesture that advances the story (scroll, choose, drag, hover, category tap), why it helps, and touch / keyboard / reduced-motion analogue.
6. Full-page rhythm: hero -> proof/discovery -> trust/CTA. Compose at least two consecutive sections; do not judge only an isolated hero.
7. Asset strategy: exact mascot/photo/product asset sources; which need image generation; whether photography, product imagery, and mascot visually belong in same scene.
8. One intentionally rejected cliche and the specific choice replacing it.

## A/B/C must be different creative directions

All three may share the same product truth but MUST differ in storytelling and page structure. Do not assign fixed default variants across projects. A useful experimental set for a marketplace promo is:

- **Narrative / Cinematic**: mascot as guide in a curated multi-layer product world; purposeful depth, sequential scene changes; strong identity.
- **Object-led / Commerce**: products as spatial protagonists, explicit shoppable zones and category discovery; visually bold without hiding intent.
- **Editorial / Modular**: surprising visual crops, strong pacing, graphic index and photographic surfaces; dense useful content balanced by large moments.

These are possible examples, not templates. The designer must invent specific compositions from project assets and research. If two directions share hero silhouette and CTA placement, redo one before presenting.

## Visual QA gate (inspect screenshots, never grade imagined output)

Evaluate each rendered desktop and mobile draft 0=absent/problem, 1=basic, 2=strong/evidenced for:

1. Brand specificity: removing logo does not make it generic.
2. Distinctive compositional idea: obvious focal point and authored relationships.
3. Material / asset coherence: believable light, scale, crops, product/mascot integration.
4. Functional narrative: value -> discover/proof -> CTA path.
5. Interaction intent: purposeful action rather than spectacle alone.
6. Typographic craft: justified scale, rhythm, line breaks, legibility, not default AI headings.
7. Emotional maturity: tone fits brand/audience and avoids accidental kids/toy aesthetics.
8. Screen pacing: 2+ meaningful sections; no repetitive cards masquerading as a story.
9. Mobile art direction: rearranged composition, not a shrunk desktop screenshot.
10. Accessibility / feasibility: contrast, focus/touch targets, motion alternatives, no blocked purchase paths.

**Reject and rework** if any of 1/2/3/4/7 is 0 or if the draft is visually indistinguishable from a generic landing template. 16/20 is a useful internal escalation threshold, not objective quality proof. Record at least 3 concrete screenshot-grounded faults and corresponding changes. At least one re-render after corrections. If tools cannot render/screenshot, state `NOT VISUALLY VERIFIED`, do not say quality passed.

## Quality workflow

- Start with art-directed thumbnails/storyboards (rough is fine), but **do not confuse rough concept sketches with polished deliverables**.
- Generate/source consistent, high-quality key assets; do not create random unrelated images to fill rectangles.
- Make one authored desktop hero + first continuation section for EACH direction before detailed component work.
- Place concepts side-by-side at comparable scale, label with intent/interaction/risks, no winner declared.
- Render screenshot proof. Ask: “Would this look materially different for another marketplace?” If not, redo composition.
- Critique against the whole-page narrative and UX goals; revise weakest concept **before** client presentation.
- Only then turn into native editable Figma frames and states, with real asset images and reusable UI components.
- After user feedback, preserve selected direction's visual DNA and record precise decisions; never silently revert to a generic scaffold.

## Mascot-led brands

- **Preserve user-supplied mascot identity**: silhouette, facial features, proportion, canonical colors and distinctive marks. Any stylization, 3D conversion or facial transformation requires explicit direction or approval.
- A mascot is a **brand protagonist**, not proof the target audience is children. The context, typography, photography, lighting and commerce details determine maturity.
- Integrate it with commerce meaning: guiding product exploration, moving between categories, revealing benefits, providing wayfinding or introducing a branded world.
- Avoid sticking it dead center above a button; consider asymmetry, oversized crop, occlusion by real product layers, controlled gaze, sense of scale and cinematic lighting where appropriate.
- Keep at least one alternative concept in which products/real-world moments carry the main visual and mascot becomes a supporting signature, unless the brief explicitly requires mascot-first.

## Evidence and honesty

Do not claim an effect will improve conversion just because it looks bold. A preference vote measures preference. Task tests measure usability. A/B validates impact only if properly deployed. Never fabricate real Figma screenshot URLs, asset files, research or votes.

## Research-to-design stress test

Новая рекомендация из ежедневного исследования должна повышать качество хотя бы одного из R01–R08 (`regression-scenarios.md`) и не ломать соседние сценарии. Продемонстрируй как кандидат помогает brief-only ситуации; если без длинного точного prompt нововведение бесполезно — это не улучшение art-direction skill. Запрет на автоматический «стиль недели» как новый default.
