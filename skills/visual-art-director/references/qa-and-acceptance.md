# Visual QA — реальные проверки, а не самопохвала

## Gate 1 — концептуальное качество до рендера

- Сценарий пользователя и CTA сохранены.
- Количество направлений соответствует запросу, default = 3.
- У каждой пары концептов минимум 3/5 различий по creative-method.
- Есть визуальная метафора, источник вдохновения и собственный вклад.
- Для complex scene есть Scene Blueprint с позициями, состояниями,
  активными объектами, mobile и reduced-motion.
- Заданные пользователем цены/названия/URL/тайминги не заменены наугад.

## Gate 2 — реальный preview/prototype

Оцени каждый **увиденный** снимок по 7 критериям:

1. **Distinctiveness:** рисунок экрана узнаваем при размытии или удалении текста?
2. **Hierarchy:** один главный объект, виден главный CTA, вторичное не спорит.
3. **Space:** глубина реальная — последовательные scale, blur, overlap,
   lighting/shadows, а не random floating cards.
4. **Type:** понятны имя товара, цена, навигация; кириллица не ломается.
5. **Craft:** нет мусорных градиентов, случайных радиусов, нестыковок медиа.
6. **Usability:** видимые controls, keyboard/touch fallback, понятные состояния.
7. **Continuity:** identity/pose/object не прыгает при смене ассета.

Если видишь дефект — одна адресная корректировка и повторная проверка. Если
проверить снимком нельзя — честно пометь статус `not visually verified`.

### Spatial-specific evidence

| Снимок | Что проверить |
|---|---|
| Desktop Idle | герой, глубина, навигация, различимый CTA |
| Desktop Hover/Drag | feedback, не закрыта карточка, управляемость |
| Desktop Mid-transition | визуальная логика сканирования/reveal |
| Desktop Settled | цена/товар/размер/цвет соответствуют новому выбору |
| Mobile Idle | карточки и панели не конфликтуют, responsive не кропает героя |
| Mobile Selected | touch alternative, CTA, размер hit areas |
| Reduced Motion | важная информация доступна без эффектов |

## Gate 3 — Figma-native / hybrid

- Пользователь действительно запросил Figma write; есть edit access.
- Перед `use_figma` был прочитан официальный `figma-use` skill.
- Для новой Figma Design — актуальный `figma-create-new-file`.
- Реальные Figma frames/IDs и screenshot существуют.
- Всё критическое UI — редактируемые слои, не один bitmap.
- В hybrid различены capture flat layers и native components.
- Имена слоёв и структура осмысленны, элементы сгруппированы.
- Нет отрезанного CTA, переполнения, ошибочной кириллицы, пустых ассетов.
- Анимации представлены честно: `storyboard` или `interactive if verified`.
- Файл/фреймы связаны с рабочими состояниями и нужными устройствами.

## Приёмка вариантов

- Три концепта различаются **геометрией**, а не фильтром/цветом.
- В новых концептах нет copy-paste чужих логотипов/брендинга.
- Один сильный эксперимент лучше трёх почти одинаковых серых скетчей.
- Проверяемость лучше декларации: по каждому важному решению есть
  наблюдаемый результат и объяснение UX-компромисса.

## Ответ после задачи

**Explore:** «Вариант A — [механика + ценность]; B — [...]; C — [...].
Превью показаны; Figma не изменена.»

**Figma-native:** «Созданы N фреймов и M компонентов в [реальный URL].
Сохранены [ограничения]. Проверено: [...]. Движение: storyboard/настроенное
прототипирование/нет. Ограничения: [...].»

**Hybrid:** «Сцена визуально проверена в локальном прототипе; в Figma
перенесены [конкретные состояния] как редактируемые слои и доработаны
[реальные native components]. JS-анимация в Figma не переносилась.»

**Audit:** P0/P1/P2, `проблема → наблюдение → воспроизводимый фикс`.

## Test cases

1. «3 варианта без Figma» → три реальных визуальных концепта, без записи.
2. «Придумай spatial hero и сразу в Figma» → blueprint, experimental либо
   native, screenshot QA, 5+ state frames, editable Figma.
3. «Никакого HTML, только Figma» → native flow, storyboard вместо JS.
4. «Сделай так же, как техзадание VirtualFit» → заданные crop/strings
   не изменяются, ограничения интерактивной Figma названы.
5. «Перенеси HTML» → Code to Canvas / HTML to Figma, не кодовый слой.
6. «Покажи варианты и не записывай» → никакой Figma-записи.
7. «Нет Figma remote или edit rights» → не заявлять, что файл создан.
8. «Сделай дизайн с доступностью и reduced motion» → без анимации
   сохраняются варианты/цены/CTA.
9. «Простая форма логина» → без ненужного dev-сервера.
10. «Fresska, редизайн каталога» → ключевая бизнес-логика сохранена,
    визуальная дивергенция подтверждена.

## MotionSites-inspired acceptance (design-first)

1. `KAIRN` prompt as inspiration → decode hero plate, typography and choreography; invent different brand-specific campaign art; show Figma frames/keyframes, **not** a working HTML page.
2. `VELL` prompt as inspiration → decode main stage, controlled interactions and history; show native state screens + asset continuity; **not** a fake interactive JS system.
3. `Fresska with mascot` → visual maturity + coherent original mascot use + realistic commercial path, 3 distinctly different editorials; no junior mascot-and-tiles hero.
4. `Make just concepts, not frontend` → no code/scaffold or background server; if tools cannot write to Figma, report blocker and supply honest visual concepts, not a fabricated Figma URL.
5. Assets → single coherent scene plate when art-led, controls/editable text separated from image, mobile framing independently composed.
6. Comparison → 3 desktop shots on comparable canvas + mobile sample + motion state + explicit preference/UX hypotheses.
