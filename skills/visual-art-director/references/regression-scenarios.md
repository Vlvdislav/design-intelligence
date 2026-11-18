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

## R15 — Interactive discovery where a UX choice matters

Brief: "Я хочу промостраницу, но не решил, должна ли она сразу вести в каталог или знакомить с брендом. Давай вместе продумаем."

PASS: inspect project and Design.md first; ask **one** meaningful question, with 2–3 UX strategies, short tradeoff and recommendation. If `request_user_input` exists and is allowed in the current Codex mode, use the actual tool for product-planning questions; otherwise one plain-text question. On reply, update UX flow and Decision Ledger, avoid repeated questions. FAIL: fake tool, ten-question form, guessing major unresolved goal, asking for hex values or GSAP settings.

## R16 — No redundant questions on fully specified brief

Brief: "Вот Design.md и Figma. Всё описано, просто делай три концепции, без вопросов."

PASS: choose FAST, read known materials, proceed with justified assumptions, don't ask what page/product/font/color already specified. FAIL: asks the same thing again, delays work with unneeded questionnaire or ignores Design.md.

## R17 — Workshop collaboration over iterations

Brief: "A нравится, но фильтры неудобные. Хочу обсудить и выбрать другой подход."

PASS: preserve selected A, present a specific alternative filter UX and meaningful tradeoffs, ask one user decision, record it, change only the requested behavior. FAIL: silently rebrands, restarts all design, treats a preference as final approval.

## R18 — Mode/tool gate for question cards

Brief: "Спроси меня через карточку с вариантами, если это доступно в Codex."

PASS: check available tools and active collaboration mode. Use `request_user_input` only if available/allowed; pass valid question with 2–3 options and a real recommendation, no made-up invocation. If unavailable, ask one plain question and state limitation. Skip/empty answer must not cause a loop. Never use a design-choice prompt for file/system permission approvals. FAIL: promises a native card unconditionally or invents a UI API.

## R19 — Connected commerce journey, not hero-only
Brief: "Разработай 3 концепции маркетплейса: главная, каталог, карточка товара, корзина. Не меняй Design.md."
PASS: three genuinely different connected UX journeys inside one design system; Figma overview shows screens together, with consistent product/price/variant, clear CTA destination and mobile flow; records first-click task and error recovery. FAIL: three unrelated hero posters or imaginary conversion claims. Negative control: one-page campaign should not force four unnecessary commerce screens.

## R20 — Figma 3D capability and fallback
Brief: "Хочу spatial-hero с поворотом продукта в Figma, но без frontend."
PASS: checks actual Figma MCP/3D skill availability; only promises editable native perspective if supported and verified; otherwise provides coherent image asset + native UI and interaction storyboard with touch/reduced-motion alternatives, and correct status. FAIL: invented transform3d access, pretends static image is live 3D, writes frontend or blocks shopping without 3D. Negative control: plain catalog filters should not gain mandatory 3D.
