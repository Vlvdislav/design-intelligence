# ImageGen playbook: концепт вместо декорации

## Когда использовать

На стадии исследования дизайна — для полноэкранных UI-мокапов. В Figma можно использовать ImageGen для предметных фото, текстур, иллюстраций, маскота, но не для подмены редактируемых фреймов скриншотом. Предпочитай штатный инструмент/официальный `$imagegen` при наличии.

## Переменные каждого задания

`PRODUCT`, `USER_JOB`, `DEVICE`, `CONTENT`, `ART_DIRECTION`, `PAGE_ARCHITECTURE`, `TYPOGRAPHY_ROLES`, `MEDIA_GRAMMAR`, `UI_BEHAVIOR`, `BRAND_CONSTRAINTS`, `NEGATIVE_PATTERNS`, `OUTPUT`.

**Составлять отдельный промпт с нуля для каждого направления** — не создавать варианты A/B/C через «same layout, different color». Общие только бизнес-функции и брендовые ограничения.

## Шаблон задания генерации (адаптировать, не копировать буквально)

```text
Create ONE premium, fully composed, straight-on flat UI screenshot concept
for [screen, mobile/desktop] of [product]. This is a real, usable product
interface, NOT a Dribbble presentation or device mockup.

Design intent: [distinct artistic thesis].
Layout architecture: [concrete structure, major zones and reading path].
Information hierarchy: [what users see first, second, third].
UI structure: [all necessary controls, actions, content, states].
Typography: [font characteristics, display vs UI contrast, Cyrillic].
Imagery: [image direction, crop and lighting consistent with brand].
Color and material system: [intentional palette and use cases].
Density/rhythm: [how negative space and content density change].
Product constraints: [navigation, no quick-add, price, checkout steps, etc.].
Use realistic content, readable labels, clear product and price information.
Show the entire selected screen composition within the canvas; crisp and
high-detail, with consistent grid and polished spacing.

Avoid: generic app dashboard template, same-size cards everywhere,
gradient blobs, meaningless pills, fake glow, random icon styles,
exaggerated corner radii, repeated lorem ipsum, cut-off navigation,
third-party logos, decorative device framing, unrealistic tiny text.
```

Если доступен параметр качества/размера, запрашивай максимально подходящий допустимый режим; **не выдумывай ключи `quality=high` или имя модели**, если API его не описывает.

## Контроль качества ImageGen

- На изображении должна быть **структура интерфейса**, а не фотопостер/несколько маленьких карточек на сером фоне.
- Должны читаться продукт, навигация, CTA и связь блоков.
- Не всё должно быть одинаково крупным/ярким; нужны контраст и визуальный ритм.
- Проверить, что три концепции структурно отличаются; если похоже, генерировать заново наиболее слабую.
- В imagegen точное воспроизведение выбранной гарнитуры, кириллицы и мелких UI-текстов не гарантировано. Помечай превью как направление, а конечную типографику делай native Figma text.
- Уникальные подписи направлений держи в обычном сообщении, а не внутри изображения.
- Если пользователь приложил маскота/логотип, сохраняй узнаваемость, не «перегенерируй» айдентику по догадкам.

## Минимальный deliverable

По умолчанию: 3 отдельные визуальные концепции + по 1–2 предложения про необычность и UX-компромисс. Не заменять визуальный результат текстовыми описаниями, если генерация реально доступна.

## Ошибка инструмента

Если ImageGen отсутствует, недоступен или вернул ошибку: объясни, что именно не удалось; отдай арт-направления и готовые точные промпты на каждое, но НЕ называй их сгенерированными картинками. Не переходи к frontend как случайному запасному пути из-за сбоя ImageGen.
  Временный HTML/CSS/JS допускается **только** по отдельным критериям experimental-first
  из `references/experimental-prototyping.md` и не заменяет конечную Figma.
