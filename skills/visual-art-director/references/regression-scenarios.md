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

## R11 — existing design system, experimental brief

Brief: "Вот действующая Figma дизайн-система и продуктовый экран. Предложи три смелые концепции новой страницы, но в нашем стиле."

PASS: сначала Figma discovery (get_libraries, search_design_system, existing screen and variable bindings, Code Connect if present), source-backed Inventory; A/B/C differ by UX/composition, NOT by inventing brand palettes/type/buttons; each reused component instance carries source key; native read-back and DS Diff QA. If source inaccessible, honest DS_UNVERIFIED/DS_BLOCKED and no claim of compliant implementation. FAIL: invented tokens, random type, raw primitives despite library components, fictitious components, or "3 new design systems" by default.

## R12 — extension or missing DS token

Brief: "В существующей дизайн-системе нет такого паттерна. Хочу новый блок, но не менять бренд."

PASS: inventories existing analogues, documents missing component/variant or token, builds proposed extension solely from inherited foundations in isolated proposal area, asks for approval before adding to approved library, status PROPOSED EXTENSION. FAIL: silently adds new global token/font/color/breakpoint and treats it as already-approved DS.

## R13 — Design.md is the only design-system source

Brief: "В проекте лежит Design.md. Прочитай и придумай 3 разные страницы в рамках нашего стиля. Никакой Figma-библиотеки нет."

PASS: agent resolves and reads the exact project file before ideation; inspects linked visuals; cites the relevant headings for fonts/colors/components/responsive; creates distinct compositions using the same documented visual rules, and if asked to create in Figma builds reusable native components from the document without pretending a published library exists. Reports document and Figma QA independently. FAIL: requests mandatory Figma library instead of reading Design.md, makes up brand values, silently overrides explicit rules, or marks results verified without live inspection.

## R14 — Design.md conflicts with existing Figma

Brief: "Design.md задаёт шрифт A, но в старом макете стоит B. Сделай новую страницу."

PASS: reads both real sources, clearly flags `DS_CONFLICT`, follows any explicit priority indicated by the user, otherwise reports unresolved implementation mismatch before making brand-affecting writes. Fails if it silently follows whichever style is visually appealing or replaces the document with a guessed rule.
