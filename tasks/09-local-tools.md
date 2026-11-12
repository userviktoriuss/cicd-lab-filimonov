# Задание 09. Локальные инструменты: Makefile, pre-commit, act

**Цель:** настроить локальный контур разработчика — проверки ДО пуша.

## Часть 1. Makefile

В репозитории уже есть `Makefile`. Проверьте:
```bash
make test    # pytest app/tests -v
make lint    # ruff check app/
```
Откройте `Makefile` и ваш workflow из задания 01 — убедитесь, что команды
одинаковые. **Принцип: локально и в CI выполняется одно и то же.**

## Часть 2. Pre-commit hooks

1. Установите хуки (конфиг `.pre-commit-config.yaml` уже в репозитории):
   ```bash
   pip install pre-commit   # или уже установлен из requirements
   pre-commit install
   ```

2. Проверьте на всех файлах:
   ```bash
   pre-commit run --all-files
   ```

3. **Эксперимент:** добавьте хвостовые пробелы в любой файл
   (`echo "x = 1   " >> app/calculator.py`), сделайте `git add` и
   `git commit`. Хук `trailing-whitespace` должен упасть и не дать
   закоммитить (и исправить файл сам). Откатите изменения.

## Часть 3. act — GitHub Actions локально

1. Установите: `brew install act` (macOS) или по инструкции
   https://nektosact.com/installation/

2. Посмотрите список job'ов и запустите один:
   ```bash
   act -l
   act push -W .github/workflows/ci.yml
   ```
   При первом запуске act предложит выбрать образ — выберите **Medium**.

3. Поймайте момент: вы только что прогнали GitHub Actions **без GitHub** —
   в локальном Docker-контейнере.

## Критерий выполнения

- `make test` и `make lint` работают
- `pre-commit run --all-files` — все проверки Passed
- Эксперимент с хвостовым пробелом: коммит заблокирован хуком
- `act` успешно прогоняет workflow из задания 01 локально

## Вопросы для самопроверки

1. Почему дешевле поймать ошибку в pre-commit, чем в CI? Чем это отличается
   по времени и ресурсам?
2. Когда act НЕ заменит настоящий запуск на GitHub? (подумайте про секреты,
   environments, матрицу ОС)
3. Какой минимальный набор локальных проверок вы бы сделали обязательным
   в своём проекте?
