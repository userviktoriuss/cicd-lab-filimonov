# Задание 06. Деплой-пайплайн с ручным approve

**Цель:** построить цепочку `test → staging → production`, где production
деплоится только после ручного подтверждения.

## Подготовка (один раз)

1. Репозиторий → **Settings** (шестерёнка вверху) → слева **Environments** →
   **New environment**
2. Создайте `staging` — без защиты
3. Создайте `production` → включите галочку **Required reviewers** →
   добавьте себя → **Save protection rules**

## Шаги

1. Создайте `.github/workflows/deploy.yml` с тремя job'ами:
   - `test` — checkout, setup-python, install, pytest (как в задании 01)
   - `deploy-staging` — `needs: test`, `environment: staging`,
     шаг-заглушка `run: echo "deploy to staging"`
   - `deploy-production` — `needs: deploy-staging`,
     `environment:` с `name: production` и `url: https://example.com`,
     шаг-заглушка `run: echo "deploy to production"`

2. Запушьте и сразу откройте запуск в Actions.

3. Наблюдайте: `test` и `deploy-staging` станут зелёными, а
   `deploy-production` **остановится жёлтым** с надписью "Waiting" —
   пайплайн ждёт вас.

4. Нажмите на жёлтый job → **Review deployments** → отметьте `production` →
   **Approve and deploy**. Job добежит до зелёного.

5. Откройте в репозитории вкладку **Environments** (или Settings →
   Environments) — там история деплоев с указанием коммитов.

## Критерий выполнения

- Запуск показывает цепочку из трёх job'ов со стрелками
- Есть скриншот/запись момента, когда production ждёт approve (жёлтый)
- После approve весь пайплайн зелёный
- Во вкладке Environments виден деплой production с вашим коммитом

## Вопросы для самопроверки

1. В чём разница между continuous delivery и continuous deployment?
   Что из этого у вас получилось?
2. Что такое секреты окружения и чем они лучше секретов репозитория?
3. Как сделать так, чтобы production деплоился только по тегам `v*`, а не по push в main?
