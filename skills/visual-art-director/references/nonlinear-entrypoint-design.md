# Non-linear commerce entry points — evidence review (2026-11-20)

Scope: design-only Figma work, no frontend, no unverified conversion promises. This rule complements UX-flow-protocol and does NOT replace the existing three-concept requirement when requested.

## Primary-source evidence
- Shopify, "The New Rules of Brand Discovery" (October 2026): https://www.shopify.com/enterprise/blog/ai-brand-discovery — Shopify reports more than half of AI-referred sessions land directly on a product page; observational platform data, not a Fresska forecast.
- Shopify, "Ecommerce UX: Design Strategies and Best Practices" (2026): https://www.shopify.com/blog/ecommerce-ux — Society6/Pattern case study: discovery by inspiration and revised IA, reported improvement in add-to-cart/mobile conversion; cannot generalize to other marketplaces.
- Linear, "UI refresh" (2026-03-12): https://linear.app/changelog/2026-03-12-ui-refresh — consistent navigation/view controls and calmer sidebar as a scanability strategy; not a commerce performance experiment.
- Anthropic frontend-design rubric: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md — brand-specific content, purposeful type/motion, plain UX copy, anti-template; guidance only, NOT a Claude model review.

## Rule A — Entry-point parity
For any marketplace concept, model at least two independent entry points: (1) home/category discovery and (2) deep-link directly to product or collection (e.g. search, social, AI recommendation). Each entry must let the user establish product identity, variant/compatibility, price, delivery/trust and the next action without requiring a homepage visit. Mark missing real data as [ASSUMED] rather than inventing it. Produce one annotated Figma state for the second entry point when the brief includes product discovery. Do not add quick-add to a catalog where the project prohibits it.

## Rule B — Distinctness measured by user decisions
For A/B/C, specify the *first meaningful user decision* and *path to product confidence* for each. Three different visual treatments with the same decisions and IA fail. For each concept show a compact decision map: entry → choice → evidence → PDP → next step. At least two concepts must differ in the first choice or evidence sequence, not just hero/media treatment. Preserve brand and approved tokens.

## Figma QA
- Verify frames are editable; record actual MCP permissions and screenshot evidence.
- Compare home-entry and deep-link comprehension at mobile width.
- Inspect whether product, price, options, trust and primary next action remain understandable.
- Critique typography, content and unnecessary motion using the Anthropic rubric without claiming a Claude invocation.
- No frontend until approval; no claim of measured uplift without user research.

## Regression prompt
"Fresska: three distinct Figma-first product discovery concepts for a multicategory marketplace. Entry can be homepage, search result, social link or AI recommendation directly to PDP. No quick-add in catalog. Show desktop/mobile, a product-decision path and a deep-link state. Use existing approved design system. No frontend."

PASS: three decision-distinct IA models; at least one deep-link frame per requested concept; explicit product-confidence evidence and mobile legibility; real Figma screenshots with critique/fix; editable frames. FAIL: three color themes, deep link requiring home, invented product facts, fake Figma verification, or frontend.
