# Design Intelligence

**Универсальный AI Design Director** — набор навыков для исследования цифровых продуктов, UX/UI-аудита, анализа конкурентов, визуальных концепций, motion-дизайна и работы с редактируемыми макетами Figma.

Основной skill **не привязан к конкретному продукту**. Дополнительные сведения о проектах хранятся отдельно в `projects/`. Например, `projects/fresska.md` загружается только при работе над Fresska.

## Требования

- Git (для команд установки ниже).
- Codex Desktop/CLI **или** Claude Code.
- Для реального изменения макетов — отдельно подключённый и авторизованный **Figma MCP**. Skill сам по себе не создаёт Figma-подключение.
- Mobbin необязателен: используются доступные публичные материалы и/или авторизованное подключение, когда оно разрешено тарифом.

## Быстрая установка через npx (рекомендуется)

Требуется **Node.js 22.20+** (проверьте `node -v`). Отдельно устанавливать CLI не нужно: `npx` запускает официальный пакет `skills`.

### Codex Desktop / Codex CLI — глобально

```bash
npx skills add Vlvdislav/design-intelligence --skill design-intelligence -g -a codex -y
```

### Claude Code — глобально

```bash
npx skills add Vlvdislav/design-intelligence --skill design-intelligence -g -a claude-code -y
```

### Codex и Claude Code одновременно — глобально

```bash
npx skills add Vlvdislav/design-intelligence --skill design-intelligence -g -a codex -a claude-code -y
```

### Только для текущего проекта

Выполни команду из папки нужного проекта (без `-g`):

```bash
npx skills add Vlvdislav/design-intelligence --skill design-intelligence -a codex -a claude-code -y
```

### Проверка и обновление

```bash
npx skills add Vlvdislav/design-intelligence --list
npx skills ls -g
npx skills check
npx skills update -g
```

**Примечание:** `-g` означает доступность во всех проектах, `-a` выбирает AI-агента, `--skill` выбирает конкретный навык из репозитория, `-y` убирает интерактивные вопросы. Команды одинаковы для Windows PowerShell, macOS и Linux при установленном Node.js.

Справка: [Vercel skills CLI](https://github.com/vercel-labs/skills).

## Альтернативная ручная установка через Git — Codex Desktop / Codex CLI

Codex читает пользовательские skills из `~/.agents/skills/`. Установленный здесь skill доступен во всех проектах.

### macOS / Linux (Terminal)

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Vlvdislav/design-intelligence.git ~/.agents/skills/design-intelligence
```

### Windows (PowerShell)

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
git clone https://github.com/Vlvdislav/design-intelligence.git "$HOME/.agents/skills/design-intelligence"
```

Проверка:

```bash
test -f ~/.agents/skills/design-intelligence/SKILL.md && echo "Skill installed"
```

Windows PowerShell:

```powershell
Test-Path "$HOME/.agents/skills/design-intelligence/SKILL.md"
```

В Codex запусти `/skills` либо введи `$design-intelligence` в запросе. Codex обычно обнаруживает изменения автоматически; если skill не появился, перезапусти приложение/сессию.

**Альтернатива:** попроси встроенный `$skill-installer` установить skill из `https://github.com/Vlvdislav/design-intelligence`. Прямая установка через Git выше обеспечивает удобное обновление с `git pull`.

### Только для одного проекта Codex

Открой терминал в корне проекта и выполни:

```bash
mkdir -p .agents/skills
git clone https://github.com/Vlvdislav/design-intelligence.git .agents/skills/design-intelligence
```

Это создаёт локальную копию для текущего репозитория (на Windows PowerShell команда `mkdir` также доступна).

## Альтернативная ручная установка через Git — Claude Code

Claude Code читает пользовательские навыки из `~/.claude/skills/`.

### macOS / Linux (Terminal)

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Vlvdislav/design-intelligence.git ~/.claude/skills/design-intelligence
```

### Windows (PowerShell)

```powershell
New-Item -ItemType Directory -Force "$HOME/.claude/skills" | Out-Null
git clone https://github.com/Vlvdislav/design-intelligence.git "$HOME/.claude/skills/design-intelligence"
```

Проверка в терминале:

```bash
test -f ~/.claude/skills/design-intelligence/SKILL.md && echo "Skill installed"
```

Windows PowerShell:

```powershell
Test-Path "$HOME/.claude/skills/design-intelligence/SKILL.md"
```

В Claude Code запроси `/design-intelligence` либо напиши «Используй skill design-intelligence ...». При необходимости перезапусти Claude Code.

### Только для одного проекта Claude Code

Из корня нужного проекта:

```bash
mkdir -p .claude/skills
git clone https://github.com/Vlvdislav/design-intelligence.git .claude/skills/design-intelligence
```

## Обновление установленного skill

### Codex — macOS / Linux

```bash
git -C ~/.agents/skills/design-intelligence pull --ff-only
```

### Claude Code — macOS / Linux

```bash
git -C ~/.claude/skills/design-intelligence pull --ff-only
```

### Codex — Windows PowerShell

```powershell
git -C "$HOME/.agents/skills/design-intelligence" pull --ff-only
```

### Claude Code — Windows PowerShell

```powershell
git -C "$HOME/.claude/skills/design-intelligence" pull --ff-only
```

Для копий в конкретном проекте замени путь на `.agents/skills/design-intelligence` или `.claude/skills/design-intelligence` соответственно. Если вручную изменял файлы в клоне, Git может попросить сначала сохранить изменения.

## Использование

### Универсальный аудит

> Используй design-intelligence. Проанализируй мой Figma-макет, определи продуктовые задачи, проверь навигацию, UX, визуальную иерархию, доступность и узнаваемость. Предложи приоритетные улучшения и три действительно разные концепции. Сначала только аудит — исходный макет не изменяй.

### Концепции Fresska

> Используй design-intelligence и профиль projects/fresska.md. Проведи аудит главной страницы Fresska. Изучи доступные UX-исследования и визуальные референсы, затем предложи три нетиповых, но удобных направления. Сохрани ограничения проекта. Перед изменениями Figma покажи план.

### Редактирование в Figma

> Используй design-intelligence и подключённый Figma MCP. Продублируй выбранный экран и создай рядом два редактируемых варианта с использованием существующих компонентов и токенов. Оригинал не изменяй. После создания проверь скриншоты и структуру слоёв.

## Модули

| Папка | Содержание |
|---|---|
| `SKILL.md` | Главный универсальный оркестратор |
| `agents/` | Product Strategy, UX Research, UX Audit, Creative Direction, Motion, Figma |
| `references/` | Типы продуктов, источники исследований, критерии качества |
| `workflows/` | Сквозной процесс: изучение → аудит → идеи → реализация → проверка |
| `templates/` | Шаблоны аудита, концепций и исследовательского журнала |
| `projects/` | Необязательные независимые профили, включая Fresska |
| `examples/` | Примеры запросов |

## Ограничения

Это набор инструкций для AI-агента, **не самостоятельный Figma-плагин**. Для работы с живыми файлами необходимы права доступа и соответствующие инструменты. Сведения из галерей дизайна не доказывают эффективность UX; исследования и гипотезы следует различать. Без подписки Mobbin его закрытые материалы не становятся доступными.

## Официальная документация

- [OpenAI: Build Skills](https://learn.chatgpt.com/docs/build-skills)
- [Anthropic: Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
