# GitHub as source of truth — proposals, not silent self-modification

Canonical source: https://github.com/Vlvdislav/design-intelligence . The repository now contains **two independent skills** under `skills/visual-art-director/` and `skills/creative-frontend-engineer/`. The root `README.md` describes installation; the root of this repository is *not* a third skill. Keep the designer's no-frontend rule intact.

## Research lifecycle

1. Inspect the actual GitHub `main` branch at the time of a proposed change: latest `SKILL.md`, changelog and `research/ideas.json`; do not assume a prior download is current.
2. Verify new primary sources and record UX mechanism, evidence, Figma applicability, source date and potential accessibility/performance trade-offs. No copyrighted copied assets or source-code cloning.
3. Apply the design-only Claude `frontend-design` rubric **as a source of critique principles**, not as a model call. Only label a review independent when an authorized Claude agent actually completed it.
4. Propose 1–3 bounded changes with exact paths, acceptance criteria and regression scenario IDs. Change UI/UX design skills only for designer improvements; frontend engineering remains a separate skill.
5. Work in a branch `research/YYYY-MM-DD-topic` or `feat/visual-art-director-vX.Y`, then open a **draft PR** for human review; never auto-merge. Run `python3 scripts/validate_skill.py`, `python3 scripts/validate_research.py`, and applicable functional checks, explicitly distinguishing static vs live Figma checks.
6. After approval and merge, users must refresh their Codex installation (for example `git pull && bash install.sh designer`). GitHub source updates and ChatGPT recurring research **do not retrain the model or update installed local copies automatically**.

## Safety

This repository is public. Never upload tokens, licensed fonts, confidential user designs or proprietary artwork without permission. Preserve Git history and use reviewable commits. Prefer visible Figma comparison frames and explicit UX trade-offs over artificial score inflation. The recurring ChatGPT task produces research proposals; any writes require a supported authenticated connector or normal Git push permissions.
