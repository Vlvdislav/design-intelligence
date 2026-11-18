# Visual Art Director — Reference First

The `$visual-art-director` skill is a **Figma-only reference reconstruction specialist**. Give it screenshots, moodboards, Motion Sites prompts, existing Figma screens or a project `Design.md`. It extracts the visible design system and reproduces the specified composition, grids, typography, assets and states as editable Figma frames.

Unlike an open-ended creative generator, it **must not invent a new art direction or brand narrative**. For Fresska, it preserves the multi-category marketplace identity and the supplied mascot instead of inventing a niche lifestyle shop. If there is no usable reference, it asks for one.

`$creative-frontend-engineer` remains a completely separate optional skill; the visual designer does not invoke it.

## Ubuntu / Codex

```bash
git clone --branch fix/design-system-lock-3-5 https://github.com/Vlvdislav/design-intelligence.git
cd design-intelligence
python3 scripts/validate_skill.py
bash install.sh designer
```

Already cloned? Run `git switch fix/design-system-lock-3-5 && git pull --ff-only && bash install.sh designer`. The installer archives the prior installed skill; restart Codex afterward.

## Example request

```text
$visual-art-director
Make a 4-screen Fresska promo in Figma using my screenshots.
Screenshot A = grid and page rhythm; B = typography; C = motion and
layering. Keep Fresska's logo, mascot, products and existing design
system. Reproduce the references closely, do not invent another style.
```

Static validation checks the package, not the visual outcome. Live Figma access and actual screenshot comparison are required for visual verification.
