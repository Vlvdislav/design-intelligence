# Claude `frontend-design` — read-only design advisor (no frontend)

## Provenance, boundaries and truthfulness

- Primary public reference: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md (read and verified 2026-11-18). This document paraphrases **design guidance**, not the upstream skill's code-writing instructions. Do **not** copy or vendor Anthropic's original file: it has its own license terms.
- The user's locally installed copy may differ. First look for explicitly available `frontend-design/SKILL.md` in their Codex/Claude workspace; read it only when actually accessible. Never assert you examined local files you cannot access.
- A *skill* is instructions, **not** another LLM. Reading the file does not equal asking Claude or obtaining an independent assessment. A genuine second opinion requires an authorized Claude Code/model integration; if unavailable, label the pass `LOCAL RUBRIC REVIEW`, not `CLAUDE REVIEW`.
- Designer track is *always* UX, art direction and Figma. Never scaffold or edit HTML/CSS/JS/React, never call a frontend builder, never ask Claude to code, and do not modify the user's website. Consultation returns observations and concept recommendations only.

## Consult point

Use only after you have: audience/JTBD, brand constraints, UX flow, the three concept theses, and visible concept previews. Do it **before** Figma release/approval and after an independent UX heuristic check, so visual spectacle cannot overrule usability.

## Design-only question to an available external Claude reviewer (optional)

> You are acting solely as a read-only design critic using your `frontend-design` design principles. Review three Figma concept screenshots for [brand, audience, user task]. Do not write code, components, CSS, JS, React or implementation instructions. Do not edit files or design frames. Identify brand-specific strengths, signs of generic AI styling, typography and composition weaknesses, comprehension and accessibility risks. For each concept provide 2 strengths, 3 actionable observations, 1 alternative visual thesis and 1 UX trade-off. Indicate uncertainty when screenshots hide interactions. Do not assume business success or real user validation. Output a concise structured critique in Russian.

Supply screenshots or Figma view links the reviewer can actually inspect. If independent Claude has no image or URL access, it must say so and review only provided evidence. Never report an independent review that was not run.

## Local creative rubric distilled from the upstream guidance

Review each concept against these **brand-specific** questions; record concrete screen evidence, not vague claims:

1. **Subject-specific aesthetic.** Does the art direction emerge from product materials, buyer motivations and brand values? Replace a generic hero if it could carry a different logo unchanged.
2. **One signature move.** Find one memorable composition/interaction with a clear purpose. Cut other competing gimmicks; do not increase visual density just to appear advanced.
3. **Non-template composition.** Reject interchangeable symmetric cards, arbitrary number labels (01/02), vague eyebrows, default gradient washes, identical shadows, boilerplate serif/cream/terracotta or black/neon themes *unless motivated by the subject*.
4. **Typographic hierarchy.** Select typefaces and width/weight/spacing deliberately; test Cyrillic, contrast and text crop. Large headline size alone is not art direction.
5. **Information semantics.** Frames, borders, dividers and labels should encode real structure. Does each CTA say what happens, and are price, trust, delivery and actions legible in commerce?
6. **Motion as meaning.** Prefer one coherent reveal or intentional feedback; reject repetitive entrance animation everywhere. Show `start → interaction → feedback → settle` in Figma storyboard and provide reduced-motion fallback.
7. **True content.** User-facing text is concrete and natural, not filler. Do not fabricate reviews, availability, benefits or conversion uplift.
8. **Multi-device reality.** Evaluate the *recomposed* mobile layout, touch targets, readable controls, keyboard focus states, contrast and interactive alternatives. No shrinking desktop indiscriminately.

## Structured review record

```
review_mode: LOCAL_RUBRIC | INDEPENDENT_CLAUDE | UNAVAILABLE
source: local Claude skill path (if opened) OR official public source URL
visual_evidence: Figma frames/screenshots actually inspected
concept: A | B | C
brand_specificity: 0..5 (+ concrete evidence)
visual_hierarchy: 0..5 (+ evidence)
product_comprehension: 0..5 (+ evidence)
originality: 0..5 (+ evidence)
mobile_accessibility: 0..5 (+ evidence)
top_3_changes: [...]  # precise layer/region and reason
rejected_idea: ...      # why it harms this user task
recommended_test: ...  # task and predicted failure mechanism
review_status: proposed | applied_and_verified | not_implemented
```

## Authority and decision

Suggestions are not directives. Preserve constraints, product truth, the user's existing approvals, accessibility and core UX. Show visual before/after when acting on a suggestion. Never treat two models agreeing as user research. For public marketplace examples, keep discovery, item detail and checkout paths clear; keep editorial experiments optional. No code before deliberate handoff to `$creative-frontend-engineer`.
