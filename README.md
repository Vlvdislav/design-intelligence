# Visual Art Director — UX / Figma-first + Creative Frontend Engineer

Two independent Codex skills maintained in this repository. **Current baseline: v3.4**.

- [`visual-art-director`](skills/visual-art-director/SKILL.md): senior UX/product research, original art direction, three meaningfully different concepts, **editable Figma** layouts, motion storyboards, hypotheses and user-testing handoff. **Does not build frontend.**
- [`creative-frontend-engineer`](skills/creative-frontend-engineer/SKILL.md): optional separate frontend-only implementation **after a concept is approved**; supports animation and spatial/WebGL when the design requires them. No backend.

## Install on Ubuntu / Codex

```bash
git clone https://github.com/Vlvdislav/design-intelligence.git
cd design-intelligence
python3 scripts/validate_skill.py
bash install.sh designer           # Figma designer only
# or bash install.sh both         # both independent skills
```

Backups live outside Codex's discovered skills directory. Restart Codex and invoke `$visual-art-director`. See [`INSTALL.md`](INSTALL.md) for verification and duplicate cleanup.

## Design-only Claude advice

The [`Claude frontend-design advisor`](skills/visual-art-director/references/claude-frontend-design-advisor.md) distils design critique principles from [Anthropic's published `frontend-design` skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), **without vendor-copying upstream content and without calling Claude automatically**. A genuine independent Claude review is optional and must be available/authorized. **No frontend coding from the designer track.**

## Research and releases

Daily research feeds candidate improvements, not unattended changes to `main`. Use `research/ideas.json` as a source ledger; propose changes in a branch and PR, run structural/regression checks, and only merge after approval. Updating this GitHub repo does not silently change an already installed local Codex copy.

## Documents

- [`CHANGELOG.md`](CHANGELOG.md) and [`INSTALL.md`](INSTALL.md)
- [`research/`](research/) — research ledger and review rules
- [`examples/`](examples/) — KAIRN, VELL, VirtualFit and Fresska-related concept exercise briefs
- [`handoff/`](handoff/) — design → frontend contract for approved concepts
- [`scripts/`](scripts/) — static validation and duplicate-detection helpers

### Security and scope

This repository is **public**. Do not commit GitHub/Figma/API tokens, credentials, proprietary client images, licensed fonts or private assets. Visual quality checks require actual Figma/browser access; static tests alone cannot prove design quality.
