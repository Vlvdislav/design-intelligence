# Visual Art Director — GitHub adoption proposal

This repository already contains a separate `design-intelligence` skill at the root. Do not overwrite it.

## Goal
Maintain the Figma-first `visual-art-director` as a **separate, versioned Codex skill**. It must own UX research, three genuinely different concepts, native editable Figma, motion storyboards and user-testing hypotheses. `creative-frontend-engineer` is a separate optional skill, invoked only **after** the user has approved a visual direction.

## Source-of-truth layout (planned)
- `skills/visual-art-director/SKILL.md` and `references/`: complete designer skill.
- `skills/creative-frontend-engineer/`: optional separate development skill.
- `docs/visual-art-director/research/`: sourced ideas and their statuses.
- `docs/visual-art-director/handoff/`: approved design contracts.
- `docs/visual-art-director/scripts/`: static checks and guarded release tooling.

**State:** This draft PR contains the review/release policy, **not** the complete 3.4 skill sources. The full verified package is available as a standalone archive in the user's ChatGPT conversation and can be added by the included `scripts/publish_to_github.sh` script from a local authenticated Git clone.

Do not merge until full sources are published and static checks pass. The existing root skill is intentionally unchanged.

## Design-only consultation
See `CLAUDE-ADVISOR.md`. Anthropic's `frontend-design` **skill document is a rubric, not an independent Claude model invocation**. If actual Claude Code is not connected, do not claim that Claude was consulted.

## Release flow
Research → candidate patch → test on KAIRN/VELL/Fresska + no-frontend constraints → **draft PR** → user review → merge → explicit Codex skill update. No unattended merge and no claim of local runtime update.
