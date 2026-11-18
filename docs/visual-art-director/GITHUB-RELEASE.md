# GitHub release policy for Visual Art Director

Repository: `Vlvdislav/design-intelligence` (currently **public**). Keep the original root `SKILL.md` and `agents/` untouched; the new skill is isolated under `skills/visual-art-director/`.

## From research to production skill
- Daily research adds **candidate** ideas with URL, date, observation, design rationale, counterexample, regressions and test scenarios.
- Creative critique consults the read-only Anthropic `frontend-design` rubric; it is not a request to generate frontend and not a fake Claude consultation.
- Proposed changes are made on `research/YYYY-MM-DD-topic` or `feat/visual-art-director-vX.Y` branches.
- Run structure, source-ledger and design-handoff validators, plus Figma smoke checks when actual access exists. State clearly when live Figma checks were **not run**.
- Create a draft PR; require review/approval before merging. No automated merging, no silent rewriting of the existing skill.
- Update the local Codex installation explicitly after merge; GitHub itself does not update `~/.agents/skills`.

## Publish full kit
Run from the extracted v3.4 kit on Ubuntu with GitHub credentials, using a clean clone of this repository:

```bash
git clone https://github.com/Vlvdislav/design-intelligence.git
cd visual-art-director-kit-v3.4
python3 scripts/validate_skill.py
python3 scripts/validate_research.py
bash scripts/publish_to_github.sh ../design-intelligence --push
```

The helper creates its own separate topic branch, copies complete sources and reports the staged diff. Then open a PR to `main`. It does not overwrite the root skill.

**Privacy:** Never publish Figma credentials, private mockups, user data, licensed fonts or secret API keys to this public repository. A private repository requires separate user selection.
