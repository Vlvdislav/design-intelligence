# Anthropic `frontend-design` as a READ-ONLY design advisor

Verified public source: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

Use the upstream skill only for **art direction and visual criticism**. Do not vendor the original skill or reuse its development instructions. The user's local copy may differ; inspect it only when that file is actually available.

## Advisor questions (for each Figma concept A/B/C)
1. Is the art direction **specific** to this brand and its actual audience, or could another logo replace it?
2. Is there one coherent signature visual mechanism, or many decorative gimmicks?
3. Does typography express personality and hierarchy without cliched ALL-CAPS labels, numbered decorations, random accent words or interchangeable serif/cream templates?
4. Is the layout composition intentional, or an AI-default grid of identical rounded cards?
5. Does imagery tell a consistent story with correct crops, light, material and mobile framing?
6. Are labels and CTA copy plain, actionable and grounded in actual product facts?
7. Does motion communicate state or user agency; is reduced-motion documented as a Figma state?
8. Does the user still understand navigation, price, trust and purchase actions on desktop and mobile?

Deliverable: `2 strengths + 3 specific design issues + alternative thesis + UX trade-off + testable hypothesis` for each concept, grounded in viewed screenshots.

## Hard boundary
**No frontend work.** No React, HTML/CSS/JS, WebGL, scaffolding, production code, Git writes or touching the user's site. This advisor is a design-review stage, not a developer skill. UX, accessibility, user constraints and explicitly approved directions have priority over creative opinion.

Use `review_mode: LOCAL_RUBRIC` when applying publicly documented principles yourself. Only use `INDEPENDENT_CLAUDE` when an actual authorized Claude Code/model invocation happened. Never make up a second opinion, screenshot inspection or validated commercial result.
