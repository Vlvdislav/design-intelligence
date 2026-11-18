# Figma gates — exploratory and approved

## Before write

**HARD GATE: прочти `design-system-lock.md`, составь source-backed DS Inventory и карту компонентов/токенов; без неё не начинай mutating writes в утверждённую продуктовую страницу.** Inspect current document and tokens if accessible. Read current official Figma skills: `figma-use`, `figma-generate-design`; `figma-create-new-file` for new file. For standalone components also relevant Figma library skill. Confirm permissions and actual tools. Create an isolated page/section for new concepts. No destructive changes to approved frames.

## Concept delivery

- A/B/C concept boards with hypothesis tags, what differs, advantages, risks and design rationale.
- For each requested concept: comparable desktop framing, mobile reinterpretation, critical interaction state(s); actual photos/objects as permitted assets.
- Meaningful names, editable text and shapes, repeated items as components/instances where appropriate, tokens and Auto Layout for functional UI.
- Storyboards for complex motion, spatial transforms where supported, and clear implementation notes where the dynamic effect exceeds Figma's prototype capability.

## Approval and promotion

Concept boards are EXPLORING. User chooses B → SELECTED. Incorporate feedback. Only explicit confirmation → APPROVED. Record frame IDs, version and asset list in handoff. Reusing editorial mood is not permission to overwrite old design.

## Design-system compliance verification

Обязательна отдельная проверка: для системных buttons/inputs/tabs/cards — main component/variant key; для текста — fontName и text style; для цветов/отступов/радиусов — связанные variables или одобренные значения; для иконок — та же библиотека и толщина линий; для responsive — действующие constraints. Сопоставляй с конкретным source frame и source token, не с интуицией. Любое отклонение = `DS_DIFF`, исправить или вынести на approval как `PROPOSED EXTENSION`. Статус `DS_VERIFIED` допустим только после фактического Figma read-back.

## Visual verification

Capture screenshots of actual Figma frames (if possible); look for clipped text, off-canvas elements, broken hierarchy, compression on mobile, missing hover/focus/error/empty states. Confirm editable layer tree; don't claim screenshot-only as editable. If tools are unavailable mark specific gate blocked.


## Creative acceptance gate for landing / promo

Refer to `creative-quality-gate.md`. Must prove with screenshot: brand-specific hero, original art-directed asset strategy, two or more meaningful sections, mobile reinterpretation, strong focus and CTA, and story that connects the composition to product discovery. Reject a generic 2-minute layout even if it is technically clean, properly componentized and fully editable. No unsupported claims of objective premium quality or conversion.

## Document-only design-system QA

For a `Design.md`-led project, compare actual generated Figma node values and screenshots against specific document sections even if the project has no published Figma library. Require evidence for colors, type, spacing, icons, controls, variants and responsive states; report remaining gaps separately. `DOC_RULES_VERIFIED` is a source-reading status; use `FIGMA_MATCH_VERIFIED` only after live Figma read-back and visual proof. No unsupported claims of compliance from static tests.
