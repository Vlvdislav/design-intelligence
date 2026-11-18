# Design Intelligence — два скилла для Codex

- **[visual-art-director](skills/visual-art-director/SKILL.md)** — новый компактный арт-директор: по короткому брифу создаёт оригинальную концепцию сайта, лендинга или Figma-дизайна; учитывает имеющуюся дизайн-систему и готовит сцены, motion и visual target.
- **[creative-frontend-engineer](skills/creative-frontend-engineer/SKILL.md)** — отдельно реализует frontend и проверяет его в браузере. Не строит backend.

## Установка (ветка с текущим обновлением)

```bash
git clone --branch fix/design-system-lock-3-5 https://github.com/Vlvdislav/design-intelligence.git
cd design-intelligence
python3 scripts/validate_skill.py
bash install.sh both
```

Для существующего клона: `git switch fix/design-system-lock-3-5 && git pull --ff-only && bash install.sh both`.
Установщик архивирует прежний скилл **вне** папки обнаружения. Открой новый сеанс Codex после установки.

## Примеры

- `$visual-art-director Сделай необычный storytelling-лендинг для Fresska с маскотом.`
- `$visual-art-director Предложи три разные концепции главной в Figma.`
- `$visual-art-director Спроектируй и передай в реализацию промо-сайт технологичного бренда.`

В режиме концепций frontend не создаётся. Прямой запрос на готовый сайт разрешает дизайнеру выбрать visual target и передать работу инженеру. Figma и browser QA выполняются только при реально доступных инструментах.

Старые примеры и research в корне репозитория оставлены как архивные материалы; **новый** скилл их автоматически не загружает.

Репозиторий публичный: не добавляй приватные ассеты, токены, клиентские файлы и лицензируемые шрифты.
