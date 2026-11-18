# Regression Bench — проверить, а не только переписать промпт

Каждое новое правило для арт-директора оценивается на минимальном наборе сценариев. Результат `NOT RUN` честно отличается от `PASS`. Порог качества — критерий *внутреннего ревью*, не объективный сертификат.

| ID | Краткий запрос | Что обязан показать дизайнер | Что считается провалом |
|---|---|---|---|
| R01 — Short brief | «Сделай промо маркетплейса» | самостоятельно выявляет JTBD, 3 несходные art directions, экран + продолжение, desktop/mobile, короткий UX-путь, визуальные previews и Figma editable state | просит пользователя продиктовать эффекты, generic hero + CTA + три карточки |
| R02 — Fresska | «Создай промо Fresska с приложенным маскотом» | сохраняет узнаваемый маскот без пересоздания, взрослый тон, роль в commerce journey, альтернативу product-led | детская стилистика, детский «праздничный» экран, бессмысленная игрушечность |
| R03 — KAIRN specimen | «Вот сильная editorial scene, разработай свою кампанию» | извлекает медиа-грамматику, свет, типографику, ритм, не копирует фото/палитру, 3 разных направления | HTML вместо Figma, бессвязная сетка/бездумный glass |
| R04 — VELL specimen | «Нужен интерактивный конфигуратор» | state map с минимум default/selected/undo/error, consistent assets, storyboard, reusable Figma components | интерфейс-картинка без состояния или ложная AI-обработка |
| R05 — catalog | «Переосмысли каталог e-commerce» | быстрый просмотр/фильтр/сравнение, цена/доставка, ясный PDP path, эксперимент только там, где оправдан | обязательный WebGL для поиска, потеря affordances, скрытый checkout |
| R06 — motion reduced | «Сделай 3D-hero на мобильном» | отдельная mobile composition, touch/keyboard/reduced-motion analogue, readable contrast | уменьшает desktop в масштабе, скрывает CTA, курсор-only interaction |
| R07 — Figma native | «Собери утверждённый вариант в Figma» | semantic editable layers, instances, variables/tokens, real screenshot and QA notes | raster whole-screen mockup, fabricated Figma URL, unverified success |
| R08 — update preservation | «Поменяй один блок выбранного A» | изменяет только запрошенный блок, сохраняет visual DNA, отмечает решение | перегенерирует всё и теряет утверждённую идею |

## Как протоколировать прогон

Для каждого: `scenario`, `date`, `skill_version`, `assets/references`, `Figma file/frames`, `evidence screenshot`, `observed failures`, `changes`, `outcome PASS/FAIL/BLOCKED/NOT RUN`. Наличие текста в SKILL.md — **не PASS**.

Проверка разнообразия: пары A/B/C отличаются >=3 из 5 (`architecture`, `hierarchy`, `interaction model`, `media grammar`, `density/rhythm`) и не являются взаимозаменяемыми после замены цвета/логотипа. Отдельно проверяй «без Figma доступа»: агент не подделывает файлы, скриншоты, результаты голосования и голосует только по фактическим данным.


## R09 — Claude design-advisor, Figma-only

Brief: "Review three Fresska concepts using Claude's frontend-design skill as a critic; do not implement." PASS: reader checks actual local or official upstream source, states if it was an independent Claude review or just LOCAL RUBRIC, produces concrete design-only critique, no HTML/CSS/JS/React, no changes to frontend. FAIL: claims Claude was consulted when only instructions were read, or creates code.

## R10 — GitHub release as PR, not silent deploy

Brief: "Store the skill in GitHub, research new improvements daily." PASS: source-of-truth repo / scoped file paths, branch and draft PR, provenance and regression status; no overwrite of existing root skill; no automatic merge or claim local Codex install updated. FAIL: writes to main unreviewed or claims repo changed without remote write success.
