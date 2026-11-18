Наследие v3.3: после установки скилл **не** запускает ежедневную задачу самостоятельно. Запланированная ChatGPT automation существует отдельно и присылает предлагаемые изменения; без авторизованного постоянного репозитория локальная установка Codex не меняется автоматически. Версия 3.3 также добавляет `python3 scripts/validate_research.py` для проверки формата source ledger.

# Install & verify

1. Распакуй ZIP, открой терминал в корне клонированного репозитория `design-intelligence`.
2. `python3 scripts/validate_skill.py`
3. `bash install.sh` на Ubuntu/Linux/macOS; `./install.ps1 -Mode both` в PowerShell.
4. Если Codex открыт, перезапусти или открой новый сеанс.
5. ` $visual-art-director ...` для UX/концептов/Figma; ` $creative-frontend-engineer ...` для frontend.

Default: `~/.agents/skills/` (Codex). Installer backs up installed versions under `.backup-YYYYMMDD...`. `CODEX_SKILLS_DIR=/your/skills/path bash install.sh` for alternate target. No remote services contacted by installer.

Check:
```bash
python3 scripts/validate_skill.py
python3 scripts/validate_handoff.py handoff/design-handoff.template.json
```

The example contract is intentionally `exploring` / `figma.file_url: null`; this is correct until the real Figma work is done. The static validator verifies structure only. Do not interpret it as a live Figma MCP/browser QA test.


## Duplicate cleanup and backups (v3.2)

Backups are now stored outside the skills scan path (normally `~/.agents/skills-backups/`). Existing duplicates from older installers are NOT automatically deleted. Check first:

```bash
python3 scripts/doctor_skills.py
```

If output names only unwanted Visual Art Director duplicates, move them to an external archive with:

```bash
python3 scripts/doctor_skills.py --apply
```

To inspect another Codex skill folder: `--root "$HOME/.codex/skills"`. The script keeps canonical `visual-art-director` and `creative-frontend-engineer` intact; archived skill copies can be restored manually. Restart Codex afterward.

## v3.4 GitHub

См. README.md: репозиторий — основной источник. Изменения в GitHub не обновляют локальную установку Codex; нужны `git pull` и повторная установка. Дизайнерский skill не запускает Claude frontend coding.
