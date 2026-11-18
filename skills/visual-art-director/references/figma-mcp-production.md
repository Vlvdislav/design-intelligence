# Figma MCP Production — Visual → Editable

## Prerequisites (проверить при каждом запуске)

- Codex app: официальный Figma plugin + авторизация.
- Codex CLI: remote MCP `https://mcp.figma.com/mcp`; официальный Figma skill
  устанавливается отдельно, если клиент его не добавил.
- Remote и desktop MCP — разные: desktop может читать данные, но remote-only
  `use_figma`, `generate_figma_design`, `html_to_figma` и `create_new_file`
  недоступны через него.
- Проверяй реальные функции, доступную схему вызова, план/seat и права edit.
  `whoami` поможет при проблемах с аккаунтом, если доступен.
- **ОБЯЗАТЕЛЬНО** загрузи `figma-use` перед каждым `use_figma`. Для записи
  экрана дополнительно используй инструкции `figma-generate-design`, если
  они доступны; для нового файла — `figma-create-new-file`.
- Если у skills и инструментов меняются названия/параметры, приоритет у
  инструкций и API текущего Figma-плагина. Не выдумывай успешные вызовы.

## Выбор маршрута

| Маршрут | Реальный выход | Для чего годится | Ограничение |
|---|---|---|---|
| `use_figma` native | Фреймы/текст/фигуры/компоненты/variables | Production-ready UX/UI | Арт-эффекты сложнее |
| `generate_figma_design` | Редактируемые **плоские** слои с работающего UI | Сложная визуальная сцена, code → canvas | JS и component tree не переносятся |
| `html_to_figma` | Слои из HTML без запуска UI | Статические web compositions | Динамические состояния надо разложить |
| `send_code_to_figma` | Code layer / Figma Make | Когда прямо нужен код в Figma | **Не** эквивалент design layers |

Для сложного интерфейса допускается **hybrid**, если он явно разрешён пользователем; для системного UI конечный deliverable всё равно собирается нативными экземплярами существующих компонентов и системными variables/styles. Code to Canvas — визуальный ориентир, но не разрешение заменить библиотеку плоскими слоями. В режиме `DS_LOCKED` приоритет у `use_figma` native.

## Сначала проверь исходную дизайн-систему (HARD GATE)

**Выполни `references/design-system-lock.md` до первого mutating Figma call.** Увидеть цвета на скриншоте недостаточно: найди источник истины и собери Design System Inventory с IDs/keys, компонентами, variants, modes, переменными и styles.

В актуальном Figma MCP workflow:
1. Если доступен source code — найди релевантный Code Connect для требуемых UI-компонентов.
2. Вызови `get_libraries`, выбери явно указанные пользователем библиотеки. Затем `search_design_system` с областью selected library; проверь whole-view composite.
3. Одним read-only inspection существующего утверждённого фрейма собери instances/variants, bindings/styles, spacing/layout, fontName, icon grammar, responsive.
4. Для каждого будущего UI-блока сформируй `Element → Library component/variant → Token/style → Source reference`; в итоговом дизайне создай **instances**, а не похожие самодельные кнопки/поля. Variables/styles связывай с токенами, не хардкодь цвета или радиусы при наличии системных значений.
5. Если библиотека/права/источник недоступны, объяви `DS_BLOCKED` или `DS_UNVERIFIED`. Не заменяй отсутствующие факты на догадки. Не затрагивай утверждённые экраны.

**Запрещено:** в существующем бренде самовольно вводить другие цвета, новые семантические tokens, шрифты, компоненты, варианты форм, толщину иконок, радиусы или брейкпоинты только потому, что новая концепция кажется эстетичнее. Нововведения — отдельный `PROPOSED EXTENSION`, не часть утверждённого design baseline. Если компонента нет, ищи близкий шаблон; если действительно нет — сообщи gap и предложи extension, но не скрывай факт.

После записи проверь итоговые узлы (instance keys, bindings, fonts, icons) и screenshot against source. До подтверждения source-backed evidence не маркируй дизайн `DS_VERIFIED`.

## Native Figma Rules

1. Раздели `Stage / Hero` (возможное свободное позиционирование) и
   `UI overlay` (auto layout, constraints, flex-like поведение).
2. Делай настоящие текстовые слои, не вшивай стоимость и CTA в картинки.
3. Asset fills допустимы для фотографий, иллюстраций, текстур и предметов;
   raster snapshot **всего интерфейса** запрещён в роли «редактируемого дизайна».
4. Повторные карточки, кнопки, tabs, чипы и точки цвета превращай в
   components/instances, если доступные инструменты позволяют это сделать.
5. Для дизайна с темами используй семантические variables/modes, а не
   случайные цвета. Если существующая система есть, переиспользуй её.
6. Иконки — SVG/vectors, не emoji placeholders.
7. Проверь доступность font families/weights и кириллицы; недоступные
   гарнитуры заменяй с пояснением, не молча.
8. Имена слоёв и фреймов описательные, например:

```text
Spatial Try-on / Desktop / 00 Idle
Spatial Try-on / Desktop / 01 Card Hover
Spatial Try-on / Desktop / 02 Item Selected
Spatial Try-on / Desktop / 03 Scan 50%
Spatial Try-on / Desktop / 04 Settled
Spatial Try-on / Mobile / 00 Idle
Spatial Try-on / Mobile / 04 Settled
Components / Product Card / Default & Active
Components / Buy Bar / Size & Color
Notes / Motion Spec
```

9. Для `FIGMA-NATIVE` без кода сложное движение передавай через набор
   редактируемых keyframes/states; подключай native prototype features
   только если реально доступны и ты их настроил.
10. После записи прочти структуру/получи screenshot. Не ограничивайся
    проверкой, что tool завершился без ошибки.

## Code to Canvas procedure

1. Удостоверься, что пользователь хочет записать в Figma, и есть URL/доступ
   или пользователь явно разрешил создать новый файл.
2. Подготовь временный прототип с читаемой семантической структурой:
   отдельные DOM nodes для hero, text, buttons, garment cards, overlay.
3. Открой рабочую страницу через доступный браузер; проверь фактический рендер.
4. При наличии `generate_figma_design` захвати последовательно нужные состояния
   в один Figma-файл (используй документированную операцию, без вымышленных
   аргументов). Для статичного HTML возможно `html_to_figma`.
5. После захвата не считай работу завершённой: открой результат, проверь слои,
   текст, масштаб, визуальную близость, потерянные эффекты, испорченные кропы.
6. При доступном `use_figma` собери native components для коммерческих контролов,
   группируй слои, перенеси возможные токены и создай storyboard вариантов.
7. Повтори screenshot QA; передай реальный Figma URL и честное описание
   `captured flat layers` vs `native components`.

## Как документировать motion в Figma

Делай два уровня артефакта:

- `Composition frames`: кадры с фактическими статичными состояниями;
- `Interaction notes`: trigger, cursor/pointer/touch, expected timing,
  easing, ordering, interrupt policy, reduced motion.

Опционально: интерактивный прототип/анимация в самой Figma, только если
доступные средства и реальная реализация это поддерживают. Browser physics
не возникает автоматически при захвате.

## Acceptance checklist

- Файл/страница/фреймы действительно созданы и идентификаторы получены
  из результата Figma MCP.
- Исходный дизайн не затёрт.
- Text remains selectable/editable, buttons and cards are separate layers.
- Keyframes не спутаны с работающей анимацией.
- Нет пустых фото/сломанных background crops, удалённых gradient/blur.
- UI overlays читаемы, цена/вариант/CTA синхронны с выбранной карточкой.
- Desktop и mobile проверены визуально отдельно.
- Если Figma capture дал только flat layers, это указано; если созданы
  компоненты, указано какие, без преувеличений.

## Официальные источники

- https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/
- https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/
- https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/
- https://developers.figma.com/docs/figma-mcp-server/create-skills/
- https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/

## Document-defined design systems (without a published Figma library)

A project `Design.md` can be the authoritative specification for brand typography, colors, spacing, controls and responsive behavior. Follow `design-md-protocol.md` **first**. If a Figma library exists, inspect and reuse it; if it does not, build semantic reusable native Figma components from the specification. Do **not** insist on `get_libraries` results as an unconditional prerequisite when the Figma library does not exist. No arbitrary alternative fonts/brand colors/controls. Check actual created text, component variants, variable bindings and screenshots against the documented values. Report `DOC_READ` independently from `FIGMA_MATCH_VERIFIED`.

## Spatial capability & fallback gate (candidate, 2026-11-18)

Before proposing a **Figma-authored 3D pose** as an actual editable deliverable, inspect current Figma MCP skills/tools. Official `figma-use` says to load `figma-3d-transforms` for static perspective/tilt only **when available**; verify that its gated APIs are actually present in the session. A 3D concept may still be communicated with an approved image asset plus editable UI overlay and before/after frames. Never promise native 3D transforms, continuous 3D, physics, or working WebGL in Figma without an observed capability and real read-back. Label one of: `NATIVE_3D_VERIFIED`, `STATIC_ASSET_STORYBOARD`, `3D_UNAVAILABLE`. Keep a touch/keyboard/reduced-motion equivalent and ensure purchase controls remain usable without the spatial effect.

Reference: https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use/SKILL.md (retrieved 2026-11-18); tool names and access may change.
