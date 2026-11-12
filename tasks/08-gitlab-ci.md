# Задание 08. GitLab CI — сравнение синтаксиса

**Цель:** перенести знания на другую CI-систему: написать `.gitlab-ci.yml`,
повторяющий логику из заданий 01–06.

## Шаги

1. Напишите в корне репозитория `.gitlab-ci.yml` со стадиями и job'ами:
   - `test` — образ `python:3.12-slim`, установка зависимостей, pytest
     с `--junitxml=report.xml` и публикацией отчёта через
     `artifacts:reports:junit`
   - `test` на двух версиях Python одновременно — через `parallel:matrix`
   - `build-docker` — образ `docker:27`, сервис `docker:27-dind`,
     сборка и пуш в `$CI_REGISTRY_IMAGE` (только для ветки main: `rules:` или `only:`)
   - `deploy` — `environment: production`, ручной запуск (`when: manual`),
     только для main

2. Проверьте синтаксис локально (YAML должен парситься):
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('.gitlab-ci.yml'))" && echo OK
   ```

3. *(Опционально, если есть аккаунт на gitlab.com)* Создайте пустой проект на
   GitLab, запушьте туда копию репозитория и посмотрите прогон:
   ```bash
   git remote add gitlab https://gitlab.com/<вы>/<проект>.git
   git push gitlab main
   ```
   CI/CD → Pipelines — сравните интерфейс с GitHub Actions.

## Критерий выполнения

- `.gitlab-ci.yml` в репозитории, YAML валиден
- В конфиге есть: stages, junit-отчёт, matrix, dind-сборка, manual-деплой
- Вы можете устно сопоставить каждый элемент с аналогом из GitHub Actions

## Таблица соответствий (для самопроверки)

| Концепция | GitHub Actions | GitLab CI |
|---|---|---|
| Шаг верхнего уровня | job | job |
| Порядок этапов | `needs:` | `stages:` |
| Исполнитель | `runs-on` | `image` + tags раннера |
| Условия | `if:` | `rules:` / `only:` |
| Матрица | `strategy.matrix` | `parallel:matrix` |
| Артефакты | upload-artifact | `artifacts:` |
| Ручной шаг | environment + reviewers | `when: manual` |
| Docker-сборка | build-push-action | `docker:dind` |

## Вопросы для самопроверки

1. Что такое docker-in-docker (dind) и зачем он при сборке образов в GitLab?
2. Как GitLab показывает junit-отчёт в Merge Request? Почему это удобно?
