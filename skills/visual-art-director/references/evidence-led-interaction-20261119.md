# Evidence-led interaction design — 2026-11-19 research candidate

Scope: design-only, Figma-first. No HTML/CSS/JS/React/GSAP/WebGL production or prototype builds.

## Verified source mechanics (not claims of Fresska outcomes)

1. Stripe Elements (https://stripe.com/payments/elements): modular payment, address and express-checkout UI with accessibility, validation, autofill and mobile-specific controls. **Transferable principle:** high-trust conversion states should be composable and clearly validated, not turned into visual theater. **Limit:** Stripe's performance claims are about Stripe integrations, not Fresska.
2. Rive production use cases (https://rive.app/use-cases): Spotify Wrapped 2025 uses listener-data-driven motion; Duolingo Lily video-call animation responds via state machine; LinkedIn Year in Review has many user journeys. **Transferable principle:** motion maps data or user intent to meaningful state change. **Limit:** Rive runtime behaviors cannot be assumed to exist in a Figma prototype.
3. Official Figma MCP guide (https://github.com/figma/mcp-server-guide): remote write-to-canvas can create/modify native frames, components, variables and auto layout; official workflow-skills/video-interaction-mapper converts recordings to annotated storyboards. Rate limits, rights and tools vary. **Transferable principle:** inspect actual tool availability, then choose native edit vs storyboard. **Limit:** docs do not establish that a specific local agent has working write permission.
4. Anthropic frontend-design skill (https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): ground visual language in subject matter, make typography structural, avoid default eyebrow labels/card kits and meaningless staggered fades; critique screenshots. This is **reading a design rubric, not consulting Claude**.

## Candidate rule A: motion semantics (references/figma-motion-storyboard.md)

Before animating, record for each proposed motion: trigger → changed system state → information revealed/confirmed → reduced-motion alternative → Figma proof type (verified prototype vs static storyboard). Reject non-triggered repeated reveal animations that convey no information. Spatial/3D interaction must improve comparison, orientation, product understanding or navigation; provide a flat equivalent.

## Candidate rule B: conversion-state coverage (references/ux-flow-protocol.md)

For a checkout, selection or payment concept, deliver at least one normal state and one meaningful exception/validation state per concept. Audit labels, error recovery, selected state, trust cues and mobile reachability. Preserve existing delivery/payment rules. A visually impressive checkout without a credible failure/recovery path is not complete.

## Candidate rule C: Figma capability handshake (references/figma-mcp-production.md)

At the start of a design-only run, record the actual MCP tool inventory, whether native write/edit is permitted, whether variables/components can be read, and whether screenshots can be obtained. Prefer native editable frames and components. Do not route through code-to-canvas when the task prohibits frontend; do not infer write access from a successful read call. If writing is blocked, mark deliverable blocked, not completed.

## Regression brief and acceptance

**Test:** “Design three distinct Fresska checkout concepts in Figma; only CDEK pickup, no courier, no date picker, single unified product list, separate contact/payment sections; preserve approved tokens. Include desktop/mobile and an invalid/missing pickup-point state. No frontend.”

- Three materially distinct task/interaction architectures, not color skins.
- Correct delivery/payment constraints; critical validation/recovery state shown.
- Native editable Figma text/controls; screenshot-based critique and revision.
- Motion storyboard identifies trigger/state change and reduced-motion alternative.
- Actual MCP tools and verified links recorded; no invented write/prototype claim.
- No frontend source files created.
- Any claim of user/conversion improvement explicitly labeled hypothesis.

## Rejected

- 3D or parallax as a default art direction without a user benefit.
- Generic full-page animation or childish mascot treatment as an attention shortcut.
- Treating reading the Anthropic design skill as an independent Claude model review.
- Claiming that a Figma screenshot proves editability or that remote MCP docs prove local tool access.
