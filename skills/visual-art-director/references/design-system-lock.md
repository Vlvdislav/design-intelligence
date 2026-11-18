# Design System Lock — source before invention

**Required** whenever a product has an existing Figma design, component library, user-provided brand rules, tokens, screenshots or an approved direction. This contract overrules generic "creative concept" or "3 novel art directions" instructions in this skill.

## Mode classifier

- `DS_LOCKED` — DEFAULT for any existing product/brand with source materials. Existing approved design system is immutable; explore layout, UX, asset direction, interactions and new page structure inside it.
- `DS_EXPLORATION` — only on a user's explicit request for rebranding, a new design system, alternate brand themes, or approval to break the current system. Deliver these variants in **isolated concept frames** with proposed changes and consequences, never overwrite approved components/tokens.
- `GREENFIELD` — brand/new project has no existing approved system. Establish and document one small internally consistent foundation before composing screens; do not mix with an existing product's locked rules.
- `DS_UNVERIFIED` — source is missing/inaccessible/partly observed; show concepts clearly marked unverified, never assert exact token values or library compliance.
- `DS_BLOCKED` — requested write depends on unavailable sources/permissions; do not mutate an approved product and do not fake compliance.

When in doubt, choose locked, not exploratory. "Wow", "premium", "spatial", "experimental" and "three concepts" refer to ART DIRECTION, not implicit permission to rebrand.

## Source hierarchy

1. User's current explicit constraints and approved decisions, including design-system changes if specifically requested.
2. Explicit source-of-truth Figma file and selected library: published components/variant sets, variables and modes, text/effect styles.
3. Approved product screens and verified Code Connect mappings, component documentation, supplied brand assets.
4. Consistent project conventions and documented tokens (when actual source above is incomplete).
5. External benchmarks, moodboards, MotionSites, Claude/frontend-design critique, generated art assets — INSPIRATION ONLY.

If any of 1–4 conflict, state the conflict precisely rather than silently picking colors or UX; user's explicit direction wins but report any deviation from prior approved rules.

## Non-negotiable preflight before any product Figma mutation

1. Identify **exact** Figma fileKey, library name/keys, relevant approved page(s)/screen node ID(s) and user-supplied requirements. Do not assume they were loaded merely because the user mentioned Figma.
2. Load official `figma-use` and `figma-generate-design` skills before use_figma writes, and other relevant Figma skills. Follow CURRENT tool schemas. Check tool and edit access.
3. Check matching Code Connect files when the project has a codebase, then call `get_libraries` and `search_design_system` for the selected library(s) (include a whole-view search and missing named components). Inspect a real existing screen to recover component/variant keys, bound variables, modes, text and effect styles, and asset sources. Never infer values from a screenshot where the source is available.
4. Produce **Design System Inventory**, with evidence not guesses:

   | Domain | Capture | Proof |
   |---|---|---|
   | Brand | logo/mascot assets, canonical palette | source asset, color variable keys |
   | Typography | family, weights, styles, hierarchy, Cyrillic support | text style ID/fontName |
   | Color/themes | semantic tokens and light/dark modes | variable collection, key, mode |
   | Layout | container widths, grids, padding/spacing, breakpoints | approved screen IDs, spacing variables |
   | Controls | button/input/tabs/chips/cards and states | component/set key and variant properties |
   | Icons/effects | family, stroke, shadows, radii | library component/style keys |
   | UX/business | navigation rules, CTA location, catalog and checkout constraints | approved frames, user brief |
   | Responsive | mobile/tablet state patterns | approved mobile frame IDs |

   For each domain mark `VERIFIED / UNVERIFIED / NOT_AVAILABLE`. Include source file link and version/date when available. **Do not synthesize a nonexistent token library.**
5. Create a component mapping table **before building**: `UI element → matched system component/variant → relevant style/variable → source key/ID → unknowns`. Reuse matching composite/library instances first; do not draw buttons/inputs/cards from primitive rectangles if library counterparts exist.
6. If an essential source is inaccessible, stop the affected mutating step, state `DS_BLOCKED` and request the specific Figma file/library access. Visual explorations can continue separately but are `DS_UNVERIFIED`.

## Strict behavior while authoring

- No new palette, font family/weight logic, icon family or stroke style, radii, type scale, semantic colors, spacing scale, elevation, breakpoints, logo, mascot stylization or checkout policy without explicit approval.
- Do not invent system components. Use actual component instances and variants for recurring product UI; bind values to existing variables/styles. In-house icons and user-supplied fonts/illustrations outrank generic substitutes.
- An unbound raw value is allowed only when there is **no applicable token**, it is measured from an approved source or a proposed local composition (e.g. hero image crop), and the rationale is documented. Brand controls cannot use unexplained hardcoded values.
- Do not fix a design system's weaknesses in place. Record them as `PROPOSED EXTENSION`, with problem, alternatives checked, precise new component/token proposal, where it would be used, impact, accessibility, migration risk and approval status. Build proposals away from approved frames.
- If the request is "three concepts", diversify content architecture, product storytelling, media direction, attention route, and interaction states; **not** the brand foundation.
- Never paste a flattened screenshot as the page; use editables, linked instances and bound variables.
- Do not overwrite approved pages. Work in named duplicate/exploration frames or a scoped target with explicit permission.

## Two-stage QA — appearance AND implementation provenance

**A. Visual review:** compare desktop/mobile Figma screenshots against approved reference frames: brand recognition, type scale, spacing, responsive behavior, tone, visual hierarchy, content and action affordances. A screenshot alone cannot prove token compliance.

**B. Structural DS Diff:** query the resulting Figma node hierarchy and verify:
- expected library instances and correct variant/state keys (no hand-drawn facsimiles);
- palette/typographic variable bindings and text/effect styles;
- system component radii, icon strokes, layout constraints, responsive modes;
- approved logo/mascot and actual asset sources;
- no unexpected hardcoded tokens or unauthorized global variables;
- unchanged approved source screen(s) and libraries.

Classify every mismatch `P0 = unauthorized brand/system drift`, `P1 = existing component replaced by primitive or broken responsive convention`, `P2 = local composition variance requiring rationale`. Fix P0/P1 before claiming complete; P2 can be documented. If source cannot be inspected, report **`DS_UNVERIFIED` / `DS_BLOCKED`**, not PASS.

## Proof format in every design-system-aware delivery

- Mode: `DS_LOCKED / DS_EXPLORATION / GREENFIELD`
- Source: Figma file/library/approved frame links (actual, no fake IDs)
- Inventory: reused tokens + component/variant source references, and unknowns
- Variation boundaries: what was deliberately varied versus held invariant
- Proposed extensions: separate table/frames, status pending approval
- Verification: `DS_VERIFIED / DS_UNVERIFIED / DS_BLOCKED` with factual screenshot+read-back evidence
- Design status: `exploring / selected / approved / blocked` — independent of system verification

No claim "made according to your design system" unless verified against the real system; no invented values where evidence is absent.
