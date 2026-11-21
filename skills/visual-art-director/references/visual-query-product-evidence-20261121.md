# Visual query → product evidence (2026-11-21)

## Purpose and boundaries
Use this reference only when the brief includes inspiration-led discovery, multi-object scenes, look/room composition, or visual product search. Do not add AI, camera upload, 3D or AR by default. This is a Figma-first design protocol; do not implement APIs or frontend.

## Evidence (primary sources)
- Google Circle to Search multi-object search, announced 2026-02-25: a single image can yield separately identified products and related results. https://blog.google/products-and-platforms/products/search/circle-to-search-february-2026/ . Observed feature; its effectiveness on Fresska is untested.
- Google Pay India fashion discovery pilot, announced 2026-11-02: inspiration feed, visual similarity and try-on, with merchant-site purchase; limited pilot. https://blog.google/intl/en-in/products/introducing-a-new-fashion-and-lifestyle-experience-in-google-pay-in-india/ . Do not generalize rollout or performance.
- Rive Figma-to-Rive: documents agent-assisted rebuild into interactive Rive components; separate design/implementation workflow, not a Figma MCP capability. https://rive.app/figma-to-rive . Use as conceptual reference for state graphs only; no Rive implementation in designer track.
- Figma MCP official guide: native canvas write is remote-only and subject to permissions and changing beta conditions. https://github.com/figma/mcp-server-guide . Verify the actual session before claiming editable output.

## Rules
1. **Scene decomposition, not decorative hotspots.** If an editorial image contains multiple shoppable objects, explicitly identify which are real catalog items, which are contextual props, and which are non-interactive. Every hotspot has an accessible text alternative and a destination; no phantom inventory. In the prototype show an object-selection state, product identity/price evidence and a reversible exit. Do not infer real SKU, price or availability from generated imagery.
2. **Provenance and confidence.** In Figma annotate `REAL CATALOG`, `ILLUSTRATIVE`, or `UNVERIFIED MATCH` for each visual product match. Never present an AI-suggested match as an exact product or claim try-on proves fit. Use product photos or approved assets where possible. Distinguish observed third-party capability from proposed Fresska behavior.
3. **Dual navigation.** Every inspiration-led flow must provide an ordinary searchable/browsable catalog alternative. In the concept board show: visual entry → object choice → verified PDP → next step, and catalog entry → same PDP. Mobile must not require precision tapping on tiny objects; provide a text/list fallback.

## Visual QA checklist
- [ ] 2+ objects are distinguishable and their selection states are visible
- [ ] Interactive objects map to actual catalog data or are explicitly labelled illustrative
- [ ] No misleading exact-match, fit or stock assertions
- [ ] Alternative list/search path works in wireflow
- [ ] Mobile touch targets and focus order are legible
- [ ] Each concept has a distinct interaction model, not just different art
- [ ] Native editable Figma frames and at least one state storyboard, with verified screenshot if tools permit
- [ ] No frontend code, no compulsory AI/AR/3D

## Regression R27 — editorial multi-object discovery
Prompt: `Fresska: three different Figma-first concepts for finding a lamp, chair and rug from one interior inspiration image. The actual catalog only has a lamp and rug; chair is a prop. Include mobile and ordinary catalog fallback.`
PASS: chair is clearly non-shoppable; two verified product targets, selection and return states, no fabricated inventory, distinct IA for A/B/C, editable Figma layers, actual visual inspection. FAIL: invented chair SKU, hotspot-only navigation, AI-generated exact matches passed as fact, three color skins, or frontend.
