# Design Intelligence

**Universal AI Design Director** for Codex/Claude/Figma. It combines product strategy, UX research, marketplace expertise, visual direction, motion, and repeatable design review. Fresska is the first, deeply documented project profile; the skill itself works for other product archetypes.

## Installation
Codex: clone the repository to `~/.agents/skills/design-intelligence/` so that the `SKILL.md` file sits at that root path. Claude Code: use `~/.claude/skills/design-intelligence/` or a project's `.claude/skills/design-intelligence/`. Install and authorize Figma MCP separately; skill instructions do not install or authorize integrations.

## Modes
- `design-intelligence audit` — read-only UX/UI review.
- `design-intelligence benchmark` — real examples and evidence.
- `design-intelligence journey` — task-based journey analysis.
- `design-intelligence explore` — three distinct visual concepts.
- `design-intelligence redesign` — editable Figma variants alongside originals.
- `design-intelligence motion` — functional and brand motion specs.

## Example
> Используй design-intelligence. Проведи UX/UI-аудит главной Fresska в Figma. Проверь поиск, навигацию, пользовательские задачи, визуальную концепцию, брендинг, доступность и мобильный опыт. Изучи реальные паттерны, найди три оригинальных направления и объясни риски. Сначала сделай read-only аудит; не изменяй исходный макет.

## Mobbin
Mobbin is **optional**. Its API/MCP may require authorization or paid access. The skill can inspect legitimately available screens, flows and website sections and collect canonical links. Without access it falls back to openly viewable examples and actual competitor sites; it never pretends to have inspected private content.

## Repository structure
`SKILL.md` orchestrator; `agents/` expert procedures; `references/` evaluation and source rules; `workflows/` orchestration; `projects/fresska.md` product brief; `templates/` output schemas; `examples/` example execution.

## Boundaries
This is a collection of procedures, not a standalone Figma plugin or guarantee of hands-free quality. Research and design output should be validated with real users and connected tools where available.
