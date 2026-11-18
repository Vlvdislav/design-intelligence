# Research ledger for Visual Art Director

`ideas.json` — небольшой versioned реестр подтверждённых находок и предлагаемых изменений. Он **не** автоматически синхронизируется с ChatGPT automation или установленным Codex скиллом. Когда появится GitHub-репозиторий, храни изменения в ветке / pull request и применяй после проверки регрессий и одобрения.

JSON format: top-level `version`, `updated_at`, `records[]`; у записи обязательны `id`, `title`, `source_url`, `source_type`, `observed`, `proposal`, `status`, `test_scenario`. Разрешённые статусы: `candidate`, `tested`, `accepted`, `rejected`, `superseded`. Дата в `source_date` может быть `null`. Не добавляй каждый visual demo в главный SKILL — сначала evidence и тесты.

Перед ежедневным обзором читать ledger, если он физически доступен; при отсутствии доступа пометить источник как недоступный и предложить текст патча без заявления об автоматическом обновлении.
