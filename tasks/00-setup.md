# Задание 00. Настройка окружения

**Цель:** убедиться, что приложение работает у вас локально, прежде чем
автоматизировать его проверку.

## Шаги

1. Создайте свою копию репозитория: **Use this template** → Create a new repository.
   Склонируйте её:
   ```bash
   git clone <url-вашей-копии> && cd cicd-lab-*
   ```

2. Установите зависимости и запустите тесты:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r app/requirements.txt
   pytest app/tests -v
   ```

3. Соберите Docker-образ и запустите приложение:
   ```bash
   docker build -t calc-app app/
   docker run -d --name calc-app -p 5000:5000 calc-app
   curl "http://localhost:5000/calc?op=mul&a=6&b=7"
   curl "http://localhost:5000/health"
   ```

4. Остановите контейнер: `docker rm -f calc-app`

## Критерий выполнения

- `pytest` выводит `5 passed`
- `curl .../calc?op=mul&a=6&b=7` возвращает `{"result":42.0}`
- `curl .../health` возвращает `{"status":"ok"}`

## Вопросы для самопроверки

1. Что делает `pytest.ini` в корне репозитория? Попробуйте удалить его и
   запустить тесты — что изменится и почему?
   - Этот pytest позволяет 1) не делать сложные импорты при разработке тестов за счеть pythonpath; 2) ускоряет запуск тестов и помогает не запускать лишнего, т.к. testpaths указывает, где искать тесты
2. Какие слои есть в Dockerfile и почему `requirements.txt` копируется отдельно?
   - слои от debian + python, + 3 слоя: слой под copy, под run и снова под copy.
   - requirements.txt копируется отдельно от приложения, чтобы ускорять сборку за счет кеширования слоя
