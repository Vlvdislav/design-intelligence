# Design Intelligence — independent Codex skills

**Visual Art Director** is a design-only skill. It turns a short request into finished, detailed Figma screens with original art direction, consistent brand assets, desktop/mobile compositions and motion storyboards. It does **not** build websites or call a frontend engineer.

**Creative Frontend Engineer** is a separate, opt-in coding skill for requests that explicitly need implementation.

## Install or update (Ubuntu / Codex)

```bash
git clone --branch fix/design-system-lock-3-5 https://github.com/Vlvdislav/design-intelligence.git
cd design-intelligence
python3 scripts/validate_skill.py
bash install.sh designer
```

Already cloned? Use `git switch fix/design-system-lock-3-5 && git pull --ff-only && bash install.sh designer`. The installer backs up the previous installed skill outside the skills folder. Start a new Codex session afterward.

## Try

```text
$visual-art-director Design one cinematic storytelling page for Fresska
with our existing mascot. Create editable desktop/mobile screens in Figma.
Do not implement a site.
```

```text
$visual-art-director Recreate this supplied visual prompt precisely in Figma,
including layout, assets, layers and transition storyboard states.
```

The designer chooses one direction by default; request two or three explicitly if needed. It never treats static Figma frames as functioning web animation. Real Figma access and screenshots are required for verified visual work.
