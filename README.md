# Лабораторная работа по CI/CD

Практикум: от локальных проверок до полного пайплайна с деплоем.
Работаете в **своей копии** этого репозитория — все результаты проверяются
в ней (вкладка Actions, локальный Jenkins).

## Как начать

1. Откройте этот репозиторий на GitHub → зелёная кнопка **Use this template** →
   **Create a new repository** → имя `cicd-lab-<ваша-фамилия>` → Create.
2. Склонируйте свою копию: `git clone <url-вашей-копии>`
3. Выполняйте задания по порядку из папки `tasks/`.

## Требования

| Инструмент | Проверка | Установка (macOS) |
|---|---|---|
| git | `git --version` | встроен |
| Python 3.10+ | `python3 --version` | `brew install python@3.12` |
| Docker | `docker version` | `brew install colima docker` → `colima start` (или Docker Desktop) |
| GitHub CLI | `gh --version` | `brew install gh` → `gh auth login` |

## Задания

| # | Тема | Файл | Результат |
|---|---|---|---|
| 00 | Настройка окружения | [tasks/00-setup.md](tasks/00-setup.md) | Тесты и Docker работают локально |
| 01 | Базовый CI | [tasks/01-basic-ci.md](tasks/01-basic-ci.md) | Зелёный прогон в Actions |
| 02 | Матричная сборка | [tasks/02-matrix.md](tasks/02-matrix.md) | 9 job'ов в одном запуске |
| 03 | Docker build & push | [tasks/03-docker.md](tasks/03-docker.md) | Образ в GHCR, можно скачать |
| 04 | Кэш и артефакты | [tasks/04-cache-artifacts.md](tasks/04-cache-artifacts.md) | Два job'а связаны артефактом |
| 05 | Cron и ручной запуск | [tasks/05-scheduled.md](tasks/05-scheduled.md) | Workflow запускается кнопкой |
| 06 | Деплой с approve | [tasks/06-deploy.md](tasks/06-deploy.md) | Production ждёт подтверждения |
| 07 | Jenkins | [tasks/07-jenkins.md](tasks/07-jenkins.md) | Зелёный пайплайн с отчётом тестов |
| 08 | GitLab CI | [tasks/08-gitlab-ci.md](tasks/08-gitlab-ci.md) | Рабочий `.gitlab-ci.yml` |
| 09 | Локальные инструменты | [tasks/09-local-tools.md](tasks/09-local-tools.md) | pre-commit и act настроены |

## Правила

- Каждое задание завершайте коммитом и пушем — история в Actions это часть результата.
- «Красный» прогон — не проблема, а материал: разберитесь в логе, почините, запушьте.
- Каждое задание содержит блок «Критерий выполнения» — по нему проверяется работа.
