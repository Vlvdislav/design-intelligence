# Spatial / Motion Playbook — «вау»-эффект с понятным UX

## Что делает spatial визуально убедительным

1. Один физический мир: совпадают направление света, качество теней,
   перспективные сокращения и масштаб объектов.
2. Контролируемая глубина: foreground, active, receding, background;
   исчезновение на периферии подчиняется одному закону.
3. Правдоподобная композиция: человек/товар — главный объект, управляющие
   элементы не спорят с ним по контрасту и масштабу.
4. Оптика: sharp focal plane, а не равномерный blur на всём экране.
5. Материал: стекло/металл/ткань имеют характерные блики и контраст; glass
   не читается без подходящего фона и границы.
6. Движение соответствует метафоре: не нужен большой параллакс просто для
   ощущения «интерактивности».

## Archetypes — выбирай как источник, не как шаблон

- **Spatial arc:** товары окружают героя по дуге; крайние меньше/тише;
  active state по центру или рядом с ним.
- **Layered atlas:** крупный товар, вокруг контекстные плавающие метки
  характеристик; глубина показывает связи.
- **Editorial kinetics:** мощная типографика движется в такт смене коллекции;
  особое внимание cropped imagery и иерархии.
- **Scan / material reveal:** свет/маска обнажает новый цвет, фактуру или форму;
  никогда не выдавать обычную замену изображения за реальную AI-примерку.
- **Interactive styling desk:** предметы сочетаются в композиции, выбор/сборка
  работает без потери цены и CTA.

## Пять motion-состояний (обязательно для сложного hero)

1. `00 / Idle`: положение объекта, читаемость hero и CTA.
2. `01 / Hover or drag`: реакция на пользователя, визуальная подсказка.
3. `02 / Selected`: фокус, выбранная карточка и состояние контролов.
4. `03 / Transition midpoint`: главный эффект наиболее выразителен.
5. `04 / Settled`: новая информация синхронизирована, CTA актуален.

При mobile добавь `05 / Mobile idle` и `06 / Mobile selection`; если есть другой
важный breakpoint, снимай его отдельно. Для Figma каждый кадр — отдельный
редактируемый frame/variant; подпиши событие, длительность, easing.

## Motion specification card

```text
Interaction: click garment card
Source: arc item 1; model outfit 1
Destination: arc item 2; model outfit 2
Stage A (0–N ms): arc moves with smoothing, input still available
Stage B (after settle): scan line descends, new state revealed via mask
Stage C: buy card details roll, selected color/size reset as specified
Interrupt: new selection cancels stale transition safely
Reduced motion: immediate swap, keep selection/price accurate
Mobile: touch drag with accessible fallback buttons
Evidence: idle, 50% scan, settled, mobile 390px screenshots
```

**Важное разделение:** `motion intended` vs `motion actually implemented`
vs `motion represented as Figma states`. Не путай эти три статуса.

## Геометрия плавной карусели

Проверяй на каждом кадре: `position`, `target`, normalized distance,
`x`, `y`, scale, z, rotation, opacity, blur. Сглаживание желательно
делать с учётом delta time:

```js
const dt = Math.min(0.05, (now - prev) / 1000); // seconds
const alpha = 1 - Math.exp(-10 * dt);
position += (target - position) * alpha;
```

Так движение ближе к одинаковому на 60 и 144 Гц. Для exact recreation
не заменяй заданную пользователем формулу без разрешения, а отметь
технический компромисс. При перетаскивании velocity и flick должны иметь
ограничения; залипания и «прыжки» карточек недопустимы.

## Логика визуального сканирования

- Два слоя согласованных изображений одной модели/объекта.
- Новый слой раскрывается сверху вниз маской; световая линия следует за
  границей маски.
- Сетка/шлейф затухают, а не остаются постоянно.
- Пока переход идёт, очередной запрос либо ставится в очередь, либо
  отменяет предыдущий; нельзя одновременно держать два несогласованных
  состояния карточки покупки и модели.
- Для reduced-motion — без сканирования, мгновенная смена состояния.

## Сервисные и UX-правила

- Действия, подсказки и главный CTA видимы без эффекта наведения.
- На тач-устройствах не рассчитывай на кастомный курсор; остаются
  обычные индикаторы и кнопки/жесты.
- Не прячь критический контент позади человека/героя.
- Интерактивный райлинг может быть необычным, но размер touch target
  и keyboard focus должны оставаться достаточными.
- Не генерируй псевдо-реалистичное значение товара, не соответствующее
  выбранной вещи. Цена/вариант/цвет/название синхронизируются со стейтом.
- Если Figma не воспроизводит CSS clip-path, perspective или физику —
  собери storyboard и укажи ограничение; для демонстрации движения
  оставь отдельный прототип лишь по запросу.

## Anti-patterns

`random floating cards`, `blur everything`, `oversized glass pills`,
`3D only on desktop`, `five duplicate concepts`, `unclear focus`,
`impossible motion promises`, `AI try-on claim based on sprite swap`,
`single full-page screenshot labeled editable`.
