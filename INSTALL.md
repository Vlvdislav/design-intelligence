# Install / update

Ubuntu / Linux, в корне клона:

```bash
git switch fix/design-system-lock-3-5
git pull --ff-only
python3 scripts/validate_skill.py
bash install.sh both
```

Для установки только дизайнера: `bash install.sh designer`. В Windows: `./install.ps1 -Mode both`.

Путь по умолчанию — `~/.agents/skills/`. Установщик сохраняет старый скилл в `~/.agents/skills-backups/`; не удаляй эту резервную копию до проверки новой версии. После установки открой новый сеанс Codex.

Проверка:

```bash
python3 scripts/validate_skill.py
python3 scripts/doctor_skills.py
```

`validate_skill.py` проверяет структуру и связи, но **не** запускает Figma или браузер. Опубликованные изменения в GitHub сами по себе не обновляют локальную установку.
