# Scene continuity and product truth — 2026-11-23

## When to use
Only for visually led commerce, spatial product storytelling, or campaigns where one product/scene is reused across multiple screens. Do not require 3D for ordinary commerce.

## Scene continuity contract
Before composing Figma screens, record: (1) confirmed product/source asset; (2) product shape, material, proportions and identifiable details that must not change; (3) scene camera, lighting, scale and crop strategy; (4) desktop, mobile and PDP compositions; (5) the factual status of each image: actual product photo / verified 3D / illustrative generated concept. Do not imply a generated image proves real product specifications.

## Proof of continuity
For each concept, build a compact Figma contact sheet containing wide editorial scene, mobile crop and PDP close-up. Compare product identity, silhouette, material, lighting and crop. If inconsistent, revise the weakest image/crop before finalizing. The scene can be a static plate; Figma UI must remain native editable layers. Use 3D only when inspection, configuration or scale materially improves the user's decision; offer standard photo/gallery fallback.

## Spatial interaction storyboard
If spatial interaction is chosen, annotate user question, trigger, viewpoint/selection change, resulting information, exit/back, keyboard/touch fallback, and reduced-motion static equivalent. Do not describe an interactive 3D runtime as implemented by Figma storyboard.

## Source evidence
- ALL3D Spatial 3D launch, 2026-10-14: https://blog.all3d.ai/spatial-3d-official-launch/ — vendor-reported ability to reuse one spatial scene across formats; no independent conversion evidence.
- Miris retail demo: https://www.miris.com/solutions/retail-and-e-commerce — vendor presentation of shared 3D assets across ad, PDP and AR; performance claims not independently validated.
- Figma MCP guide: https://github.com/figma/mcp-server-guide — write-to-canvas exists subject to tool, seat and file permissions.
- Anthropic design rubric: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md — design-only reference, not an external Claude review.

## Regression R29 — single-product visual identity
Brief: "Create three distinct Figma-first discovery concepts for one premium desk lamp, with editorial hero, mobile entry and PDP. The supplied catalog contains one verified product photo and dimensions; do not invent variants. One concept may use spatial inspection if justified."
PASS: three different discovery/interaction models; same confirmed lamp silhouette/material/dimensions throughout; each concept has wide/mobile/PDP contact sheet; labels distinguish factual vs illustrative media; static fallback and storyboard for spatial concept; native Figma UI and actual visual QA; no frontend.
FAIL: three color skins, inconsistent generated product details, fake AR implementation, 3D without a decision benefit, or unverified claims of completed Figma work.
