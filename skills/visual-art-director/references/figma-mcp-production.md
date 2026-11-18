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

Для сложного интерфейса допускается **hybrid**: rendered spatial stage →
Code to Canvas → нативная доработка `use_figma` (navigation, product panel,
typography, variants, variables).

## Сначала проверь исходную дизайн-систему

Если работаешь с существующим файлом, инспектируй: компоненты, styles,
variables, mode, grid, размеры, fontName, брендинг. Не выдумывай «наш цвет».
Сохрани исходные страницы, если не запрошено прямое редактирование.

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
