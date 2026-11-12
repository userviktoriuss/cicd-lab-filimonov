# Задание 07. Jenkins

**Цель:** поднять self-hosted CI и написать пайплайн на Jenkinsfile —
почувствовать разницу с SaaS-подходом GitHub Actions.

## Шаги

1. Поднимите Jenkins (всё нужное уже в репозитории):
   ```bash
   cd jenkins
   docker compose up -d --build
   ```
   Первая сборка займёт несколько минут (скачивается образ и плагины).

2. Откройте http://localhost:8080 → войдите: **admin / admin**.
   (Пользователь создан заранее скриптом `jenkins/init.groovy`,
   мастер настройки отключён.)

3. Изучите `jenkins/Dockerfile`, `jenkins/plugins.txt`, `jenkins/init.groovy` —
   ответьте себе на вопрос: как Jenkins «из коробки» оказался с плагинами
   и пользователем без единого клика?

4. Создайте пайплайн:
   - **New Item** (слева вверху) → имя: `cicd-lab` → тип **Pipeline** → **OK**
   - прокрутите до секции **Pipeline**
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: `https://github.com/<ваш-логин>/<ваш-репо>.git`
     (если репозиторий приватный — сделайте его временно публичным или
     добавьте credentials)
   - Branch Specifier: `*/main`
   - Script Path: `jenkins/Jenkinsfile`
   - **Save**

5. Напишите `jenkins/Jenkinsfile` (декларативный синтаксис). Скелет:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Install') {
               steps {
                   sh 'python3 -m venv venv && . venv/bin/activate && pip install -r app/requirements.txt'
               }
           }
           stage('Test') {
               steps {
                   sh '. venv/bin/activate && pytest app/tests -v --junitxml=report.xml'
               }
               post {
                   always { junit 'report.xml' }
               }
           }
           // TODO: добавьте stage 'Deploy' с условием when { branch 'main' }
       }
       // TODO: добавьте post { success / failure } с echo-сообщениями
   }
   ```
   Заполните оба TODO, закоммитьте, запушьте.

6. В Jenkins нажмите **Build Now**. Дождитесь зелёного результата.
   Откройте сборку → **Test Result** — там ваши 5 тестов.

7. Слева на странице job'а нажмите **Open Blue Ocean** — посмотрите
   альтернативную визуализацию пайплайна.

## Критерий выполнения

- Pipeline job зелёный, в Stage View видны стадии Install → Test → Deploy
- В сборке есть Test Result с 5 тестами (виджет junit)
- В Jenkinsfile есть условный деплой (`when { branch 'main' }`) и блоки post
- Скриншот Blue Ocean с зелёным пайплайном

## Вопросы для самопроверки

1. Где физически выполняются шаги пайплайна? (подсказка: `docker exec jenkins ls`)
2. Чем declarative pipeline отличается от scripted?
3. Назовите два плюса и два минуса self-hosted CI по сравнению с GitHub Actions.

## Завершение

```bash
cd jenkins && docker compose down   # остановить Jenkins после работы
```
