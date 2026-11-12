# Задание 03. Docker build & push в GHCR

**Цель:** пайплайн собирает Docker-образ и публикует его в GitHub Container
Registry. Артефакт пайплайна — готовый образ.

## Шаги

1. Создайте `.github/workflows/docker.yml`:
   - `on: push` в main
   - job `docker` на ubuntu-latest, с `permissions: contents: read, packages: write`
   - шаги:
     1. `actions/checkout@v4`
     2. `docker/setup-buildx-action@v3`
     3. `docker/login-action@v3` — registry `ghcr.io`, username `${{ github.actor }}`,
        password `${{ secrets.GITHUB_TOKEN }}`
     4. `docker/build-push-action@v6` — `context: app`, `push: true`,
        теги `ghcr.io/${{ github.repository }}:latest` и `...:${{ github.sha }}`

2. Запушьте. Откройте лог шага build — найдите строку
   `pushing manifest for ghcr.io/<вы>/<репо>:latest ... done`.

3. Откройте свой профиль GitHub → вкладка **Packages** → ваш пакет.
   Зайдите в **Package settings** → внизу **Change visibility** → **Public**.

4. Проверьте скачивание образа:
   ```bash
   docker pull ghcr.io/<ваш-логин>/<ваш-репо>:latest
   docker run --rm ghcr.io/<ваш-логин>/<ваш-репо>:latest python -c "import calculator; print(calculator.add(2, 3))"
   ```

5. *(Опционально)* Добавьте кэширование слоёв:
   `cache-from: type=gha` и `cache-to: type=gha,mode=max` в build-push-action.
   Запушьте дважды и сравните время шага сборки.

## Критерий выполнения

- Workflow зелёный, в логе есть `pushing manifest ... done`
- Пакет виден в профиле в разделе Packages
- `docker pull` образа работает на вашей машине без авторизации (пакет публичный)
- Образ имеет два тега: `latest` и SHA коммита

## Вопросы для самопроверки

1. Откуда берётся `secrets.GITHUB_TOKEN`? Почему его не надо создавать руками?
2. Чем тег `latest` отличается от тега по SHA? Когда какой удобнее?
3. Что даёт `type=gha` кэш и где он хранится?
