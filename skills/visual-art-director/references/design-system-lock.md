# Design System Lock — source before invention

**Required** whenever a product has an existing Figma design, component library, user-provided brand rules, tokens, screenshots or an approved direction. This contract overrules generic "creative concept" or "3 novel art directions" instructions in this skill.

**Document-first:** When the user supplies a project `Design.md`, read and review the actual Markdown and referenced resources *before* trying Figma discovery, composing concepts or editing. Follow `design-md-protocol.md`. A real, accessible `Design.md` is sufficient as the normative design-system specification; a published Figma library is an optional implementation source. Do not conflate `DOC_READ` with `FIGMA_MATCH_VERIFIED`.

## Mode classifier

- `DS_LOCKED` — DEFAULT for any existing product/brand with source materials. Existing approved design system is immutable; explore layout, UX, asset direction, interactions and new page structure inside it.
- `DS_EXPLORATION` — only on a user's explicit request for rebranding, a new design system, alternate brand themes, or approval to break the current system. Deliver these variants in **isolated concept frames** with proposed changes and consequences, never overwrite approved components/tokens.
- `GREENFIELD` — brand/new project has no existing approved system. Establish and document one small internally consistent foundation before composing screens; do not mix with an existing product's locked rules.
- `DS_UNVERIFIED` — source is missing/inaccessible/partly observed; show concepts clearly marked unverified, never assert exact token values or library compliance.
- `DS_BLOCKED` — requested write depends on unavailable sources/permissions; do not mutate an approved product and do not fake compliance.

When in doubt, choose locked, not exploratory. "Wow", "premium", "spatial", "experimental" and "three concepts" refer to ART DIRECTION, not implicit permission to rebrand.

## Source hierarchy

1. User's current explicit constraints and approved decisions, including design-system changes if specifically requested.
2. User-designated `Design.md` (actual content, revision and links) plus explicitly approved design-system documentation. If this document is declared authoritative, its rules outrank ambiguous incidental Figma styles.
3. Actual Figma source file/library: published components/variant sets, variables/modes, text/effect styles, approved screens and Code Connect. A mismatch with an authoritative `Design.md` is `DS_CONFLICT`, not permission for silent correction.
4. Documented project conventions and separately supplied brand assets (where the authoritative document does not define the point).
5. External benchmarks, moodboards, MotionSites, Claude/frontend-design critique, generated art assets — INSPIRATION ONLY.

If any of 1–4 conflict, state the conflict precisely rather than silently picking colors or UX; user's explicit direction wins but report any deviation from prior approved rules.

## Non-negotiable preflight before any product Figma mutation

1. Search for the **user-designated project `Design.md` first**, read it completely, inspect referenced accessible assets and note exact path/revision/section anchors. If a `Design.md` is explicitly expected but missing, identify the missing file and do not assert compliance. Also identify Figma fileKey/library names **when actually provided or available**; Figma libraries are not mandatory prerequisites when the approved system lives solely in Markdown.
2. Load official `figma-use` and `figma-generate-design` skills before use_figma writes, and other relevant Figma skills. Follow CURRENT tool schemas. Check tool and edit access.
3. Build the initial inventory from the exact `Design.md` sections. **If a connected Figma file/library exists**, check Code Connect when relevant; call `get_libraries` / `search_design_system` and inspect existing screens for instances/variants/bindings. Cross-check against the document and report conflicts. If no library exists, **do not block** the creation of new native Figma components from the documented specification; record actual newly created component names and their links when available. Do not infer values from screenshots when the document defines them.
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
5. Create a component mapping table **before building**: `UI element → Design.md section → library component/variant if present (or native component to build) → token/style → unknowns`. Reuse matching library instances when available. With `Design.md` only, build named reusable components and variants according to its specification, rather than one-off primitive copies. Do not invent unspecified brand tokens.
6. If the explicitly designated `Design.md` is inaccessible, stop the affected brand-dependent write, state `DS_BLOCKED`, and ask for its exact location. **Do not require a Figma library when `Design.md` provides sufficient rules**; only request Figma access if actual target-file editing or library reuse is the requested deliverable and that access is missing. Exploratory work on incomplete rules stays `DS_UNVERIFIED`.

## Strict behavior while authoring

- No new palette, font family/weight logic, icon family or stroke style, radii, type scale, semantic colors, spacing scale, elevation, breakpoints, logo, mascot stylization or checkout policy without explicit approval.
- Do not invent unsupported component specifications. Use actual library instances and variants where present, or build reusable local Figma components consistent with documented `Design.md` rules if no library counterpart exists. Bind documented tokens to Figma variables/styles where feasible; clearly mark the newly established local tokens as derived from documentation, not published library keys. In-house icons and user-supplied fonts/illustrations outrank generic substitutes.
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
- Authoritative `Design.md`: project path/URL, revision or content hash if accessible, exact sections read, linked visual references inspected/missing; `DOC_READ` and `DOC_RULES_VERIFIED` statuses.
- If Figma used: `FIGMA_MATCH_VERIFIED` only after actual read-back and screenshot; disclose `DS_CONFLICT` where document and Figma disagree.
- Source: Figma file/library/approved frame links (actual, no fake IDs)
- Inventory: reused tokens + component/variant source references, and unknowns
- Variation boundaries: what was deliberately varied versus held invariant
- Proposed extensions: separate table/frames, status pending approval
- Verification: `DS_VERIFIED / DS_UNVERIFIED / DS_BLOCKED` with factual screenshot+read-back evidence
- Design status: `exploring / selected / approved / blocked` — independent of system verification

No claim "made according to your design system" unless verified against the real system; no invented values where evidence is absent.
