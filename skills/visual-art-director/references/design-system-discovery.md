# Design System Discovery & Ownership

## Mandatory preflight before any visual concept
1. Search the active project (not the skill repository alone) for `design.md`, `DESIGN.md`, `design-system.md`, brand guidelines, existing tokens, and accessible Figma libraries. Search case-insensitively; report paths actually inspected. Do not claim remote or local access you lack.
2. Read discovered sources, identify their version and authority, and record decisions as `APPROVED`, `PROPOSED`, or `UNKNOWN`. Existing approved brand and UX decisions override inspiration and generic advice.
3. Inspect accessible Figma styles, variables, components, and screens; if unavailable, mark `NOT INSPECTED` and continue with explicitly provisional recommendations.
4. If no usable design system exists, research three relevant real design systems from primary sources (for example Shopify Polaris, Adobe Spectrum, Atlassian Design System). Extract interaction, accessibility, typography, layout and component principles, not branded visuals. Record source URLs and dates, observed facts vs proposed adaptations, and licensing constraints.
5. Propose a project-specific `design.md`: brand thesis, audience/JTBD, typography including Cyrillic, semantic color roles, spacing/grid/breakpoints, components and states, accessibility, motion/reduced-motion, asset rules, desktop/mobile patterns, version and decision log. Do not silently overwrite existing files. Seek approval before marking the proposal `DS_LOCKED`.
6. If an existing system is partial, propose a minimal delta instead of regenerating it. Preserve approved tokens, components and responsive behavior.
7. If write access exists and the user requested creation, write the proposed file at the agreed project path, explicitly labeled `DRAFT / NOT APPROVED`. Otherwise provide the complete draft and note the write limitation.

## Research quality
- Choose sources based on the product's actual domain, not visual popularity. Record `OBSERVED`, `USER`, and `PROPOSED` separately.
- Never infer a performance lift or claim a Figma component exists without verification.
- Avoid copying another brand's identity or proprietary assets.
- The outcome is an evidence-backed system and design decisions, not a collage of references.

## Preflight output
```
design_source: path | missing | inaccessible
design_source_read: true | false
figma_library_inspected: true | false
system_status: APPROVED | PARTIAL | PROPOSED | UNKNOWN
reference_sources: [url]
proposed_changes: [...]
approval_required: true | false
```
