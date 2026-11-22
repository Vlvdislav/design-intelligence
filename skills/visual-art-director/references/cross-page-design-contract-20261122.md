# Cross-page Design Contract & Contact Sheet (2026-11-22)

Use for a multi-page marketplace, e-commerce journey, or editorial storytelling system. **Design-only, Figma-first.** This is a proposal for the existing art-director workflow, not an instruction to build Shopify Canvas or production code.

## Evidence
- Shopify Canvas (2026-10-01): store-wide visual workspace, side-by-side page review, screenshots and iterative agent design; Shopify describes a per-theme "design contract" and opinionated evaluation data. https://www.shopify.com/news/introducing-canvas
- Figma official `figma-generate-library`: scoped inventory, variables/variants, structural validation and one visual review per coherent composition phase. https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-library/SKILL.md
- Rive website use cases: state machines can explain interaction, but our designer only specifies Figma storyboards, not Rive runtime. https://rive.app/use-cases/websites
- Anthropic frontend-design: content-specific design, purposeful structure/typography, motion only when meaningful; this is a rubric, not a Claude model review. https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

## Rule 1 — Scoped design contract, before Figma mutation
For each requested concept, create a compact, *concept-specific* contract:
- Real product/user task, page/flow inventory, source of truth and approved constraints.
- Visual thesis: subject-specific imagery/materials, type role, grid logic, density, tone and one meaningful interaction signature.
- Stable cross-page invariants: navigation location, product facts, price presentation, action hierarchy, mobile access and brand tokens.
- Deliberate exceptions: where the concept changes navigation, layout or motion, and why that change improves a user decision.
- Rejection criteria: 3 visual clichés that would make this concept generic or misleading.
Do not lock arbitrary colors/radii before seeing the source design system. Preserve already approved tokens. This is a **brief contract**, not an extra lengthy report.

## Rule 2 — Cross-page contact-sheet gate
Before claiming a multi-screen concept complete, arrange the requested native Figma screens side by side as a *contact sheet* (or provide a verified overview screenshot if a board cannot be created). Compare at equal zoom:
1. Does the user recognize the same product and brand across landing, category, PDP and mobile?
2. Does each screen maintain action hierarchy and information continuity, without visual monotony?
3. Are page-specific compositions meaningfully different, while system components stay consistent?
4. Does the mobile composition reorganize content instead of shrinking desktop?
5. Do motion storyboards explain a user decision, preserve orientation and offer a reduced-motion/static state?
Mark `NOT VERIFIED` if the actual screenshot cannot be retrieved. Inspect, make a targeted correction and recheck only affected screens. Do not add speculative pages beyond the brief.

## Rule 3 — Figma component integrity
When creating repeated elements, inspect available libraries, variables and existing components first. Reuse compatible foundations. If missing, create only the minimal tokens/variants needed for the scoped concept. Semantic layer names and native editable text/controls are required. Never represent a whole UI screen as one image. Treat available Figma MCP capabilities as session-dependent; record actual tools and read/write success.

## Regression R28 — Cross-page coherence vs concept diversity
Prompt: "Create three distinct Figma-first design directions for a premium marketplace, each with a homepage, category entry, PDP and mobile adaptation; no frontend."
PASS: A/B/C differ by interaction/IA, each has a short design contract, real editable Figma frames, a verified cross-page overview, a corrected defect and preserved product data; mobile is recomposed; no code.
FAIL: three color skins, inconsistent product facts or CTA placement without rationale, a screenshot pasted as a frame, unverified claims of Figma edits, or a beautiful homepage whose PDP contradicts its own visual system.

## Explicit exclusions
No mandatory 3D, parallax, Rive export, auto-generated frontend or performance claims. This rule complements existing screenshot QA and direct-PDP entry tests; it does not duplicate them.
