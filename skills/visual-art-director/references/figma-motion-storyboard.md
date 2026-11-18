# Figma motion storyboard — design the experience without building frontend

## Default contract

When asked for concept/interface design, produce Figma deliverables. **Do not scaffold an HTML, React, GSAP or Three.js project by default**, even if source inspiration was written as executable web instructions. Use visual state frames, prototype links and annotations to represent motion. A separate frontend skill consumes the approved design later.

If the user explicitly asks for a runnable motion experiment, a limited non-production proof can be authorized. It must not displace the Figma outcome or make the designer silently become a frontend engineer.

## Minimum state set for an experimental hero

Design the set relevant to the idea (not every state for every screen):

| Figma frame | What it proves | Example |
|---|---|---|
| `01 / Entry` | initial crop, anchor, contrast, readable navigation | scene poster + not-yet-revealed type |
| `02 / Idle` | fully composed hero, hierarchy and CTA | editorial portrait + tiles |
| `03 / Intent` | visible hover/focus/tap affordance | product focus, ring, card tilt as still pose |
| `04 / Transition 50%` | spatial/motion choreography | scan line across new outfit, intermediate crop |
| `05 / Settled` | resulting information and action | new look selected + updated price/label |
| `06 / Mobile Idle` | re-composed narrow-layout hero | image reframed + primary action available |
| `07 / Mobile Selected` | touch behavior and resulting state | selected card or filter state |
| `08 / Reduced Motion` | same action without kinetic effects | instant transition, no loop |

For campaign-style content with an entrance sequence, show storyboard frames keyed by stage (`00`, `hero ready`, `headline on`, `tiles on`, `CTA on`) and annotate order/duration in a `MOTION-SPEC.md`. For state-heavy apps, show an interaction-state graph and the states after selection, undo, error and reset.

## Frame-level notes

Each meaningful transition must specify:

- **User trigger**: pointer/keyboard/touch/scroll or timed entrance.
- **Before → after**: affected editable layers (IDs or semantic names), not only 'magic animation'.
- **Choreography**: order, direction, start/end geometry, opacity, masks, depth, light cues and motion intent. Timings are designed proposals, not observed fact unless sourced.
- **Content sync**: which labels, thumbnails, variants, prices or progress indicators update in the same state.
- **Accessibility**: reduced motion behavior, focus/keyboard action, touch replacement for hover, semantic feedback.
- **Constraints**: what is Figma-prototypable versus requires runtime (WebGL physics, camera tracking, continuously animated assets).

Do not label a static Figma screenshot as an interactive prototype. Prototype links count only when actually wired and verified.

## Figma organization

`00 / Creative Strategy` (Concept DNA + user task) → `01 / Concepts A-B-C` (comparable thumbnails + desktop continuation) → `02 / Screens` (native desktop/mobile) → `03 / Interaction States` (motion/story frames) → `04 / Design System` (tokens/components) → `05 / Decision Board` (hypotheses, votes, tradeoffs) → `06 / Handoff` (only when selected/approved).

Names are a suggested convention, not fixed tool API instructions. **If a design system already exists, reuse its tokens, components and variants from the first draft, not only after art direction.** Three concepts should differ in spatial/media storytelling and user flow without creating three incompatible design systems. Only greenfield/explicit rebranding may propose alternate visual systems.

## What counts as done in design mode

- The visual concept is actually viewable and meaningfully different from alternatives.
- Figma artboards contain primarily editable UI layers; imagery is appropriately image-filled.
- Desktop/mobile are art-directed separately.
- At least one meaningful interaction has before/transition/after frames.
- A source-grounded review identifies 3 concrete faults and the revised screenshot.
- Status remains `exploring` until the user selects; never start frontend just to make the design appear dynamic.
