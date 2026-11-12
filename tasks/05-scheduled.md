# Задание 05. Запуск по расписанию и вручную

**Цель:** workflow — не только реакция на push. Научиться запускать пайплайны
по cron и по кнопке с параметрами.

## Шаги

1. Создайте `.github/workflows/scheduled.yml`:
   ```yaml
   on:
     schedule:
       - cron: "0 6 * * *"        # каждый день в 06:00 UTC
     workflow_dispatch:
       inputs:
         suite:
           description: "Набор тестов"
           type: choice
           options: [all, smoke]
           default: all
   ```
   - job с двумя шагами тестов:
     - smoke: `pytest app/tests -v -k test_add`,
       условие `if: github.event.inputs.suite == 'smoke'`
     - полный: `pytest app/tests -v`,
       условие `if: github.event_name == 'schedule' || github.event.inputs.suite == 'all'`
   - не забудьте checkout, setup-python и установку зависимостей

2. Запушьте. Затем запустите вручную **двумя способами**:

   **Через UI:** Actions → выберите workflow слева → справа кнопка
   **Run workflow** → выберите `smoke` → Run workflow.

   **Через CLI:**
   ```bash
   gh workflow run <имя-вашего-workflow> -f suite=smoke
   gh run list --limit 3
   gh run watch     # наблюдать за выполнением в терминале
   ```

3. Откройте завершённый запуск и убедитесь по логу, что выполнился только
   smoke-шаг (один тест), а полный прогон был пропущен (skipped).

## Критерий выполнения

- Кнопка **Run workflow** есть у workflow и предлагает выбор `suite`
- Запуск с `suite=smoke` выполняет ровно 1 тест (видно в логе)
- Запуск с `suite=all` выполняет все 5 тестов

## Вопросы для самопроверки

1. Расшифруйте `0 6 * * *`. В каком часовом поясе работает cron в Actions?
2. Какое событие будет в `github.event_name` при ручном запуске? А по cron?
3. Приведите два реальных сценария для cron-workflow в проекте.
