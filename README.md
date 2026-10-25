# Design Intelligence

Universal AI Design Director for digital products. Combines product strategy, UX research, competitive benchmarking, visual identity exploration, motion design, critical evaluation and editable Figma work. **No brand or product assumptions are baked into the main skill.**

## Installation
For Codex: clone to `~/.agents/skills/design-intelligence/`, with `SKILL.md` at its root. For Claude Code: use `~/.claude/skills/design-intelligence/` or `.claude/skills/design-intelligence/` within a project. Figma MCP must be separately connected and authorized.

## Modes
- Audit an existing design (read-only)
- Research competing products and UX patterns
- Map user journeys
- Explore three distinct creative concepts
- Redesign with editable native Figma layers
- Specify functional and expressive motion
- Validate outcomes and risks

## Start
> Используй skill design-intelligence. Проанализируй текущий макет в Figma: пользовательские цели, UX, визуальную иерархию, доступность, узнаваемость и креативные возможности. Проведи исследования доступных источников, предложи три разные концепции. Сначала только аудит, исходный макет не меняй.

## Modular structure
`SKILL.md` universal orchestrator, `agents/` expert procedures, `references/` methods and research sources, `workflows/` full process, `templates/` output formats, `projects/` optional isolated briefs, `examples/` generic prompts.

## Optional projects
Project-specific preferences and non-negotiables belong **only** in `projects/<project-name>.md`. A profile is loaded when that project is explicitly in scope; it must not affect other tasks. A project profile for Fresska is included as one optional example, not as a skill dependency.

## Mobbin
Mobbin is optional. Use it only with authorized access or openly available pages. No subscription is required to use the core skill, though private Mobbin MCP content can require a paid account. Alternatives include actual accessible product sites and public UX sources.

## Limitations
This repository contains agent guidance, not a standalone GUI plugin. To actually modify Figma, connect the Figma integration. Research findings are not substitutes for user testing; make evidence and assumptions visible.
