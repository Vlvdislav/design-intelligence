# Inter-skill contract — Design → Frontend

Canonical JSON template: `references/design-handoff.template.json` inside this installed skill. The kit additionally includes a standalone `scripts/validate_handoff.py` for static checks.

- `status`: exploring / selected / approved / blocked; only approved proceeds by default. Direct user instruction to build an explicitly selected target can override the gate, with this documented.
- `figma.file_url`, `figma.frames[].node_id` and image assets: populate from ACTUAL records only; otherwise null and list blockers.
- `visual_dna`: what may not change: page architecture, key proportions, palette/type, main interactions and signature moment.
- `design_system`: include a separately linked DS Inventory/source file, selected library/source frame IDs, relevant component/variant keys, variable/text style references, confirmed modes, extension requests and verification state (`DS_VERIFIED | DS_UNVERIFIED | DS_BLOCKED`). If unavailable, record blockers. Engineer must not silently replace tokens/components with custom substitutes.
- `UX-FLOW.md`: screen IDs, tasks, states, edge cases, content rules.
- `MOTION-SPEC.md`: triggers, timing/easing when measured, behaviors, scroll mapping, reduced motion, mobile fallback, performance limits.
- `acceptance`: verifiable browser outcomes; not aspirational labels like 'wow'.
- `hypotheses`: status as hypothesis, research results only if observed.
- `open_questions`: never disguise unknown feature/business policy as design fact.

Handoff priority: user-approved Figma target > approved interactions/flows > design tokens/assets > notes > illustrative reference websites. If conflicts occur, report them rather than quietly redesigning.

For projects with authoritative `Design.md`, handoff must include its relative path/URL, revision/hash when obtainable, referenced sections for selected tokens/components, any `DS_CONFLICT`, and separate document/Figma verification statuses. The frontend engineer must read the same project `Design.md` before implementing the approved Figma design; a frontend handoff is not permission to redefine tokens.
