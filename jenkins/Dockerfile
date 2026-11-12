FROM jenkins/jenkins:lts

USER root
# Python внутри Jenkins — пайплайн запускает тесты прямо на контроллере
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*
USER jenkins

# Плагины, нужные для демо, ставим заранее — не придётся ждать на лекции
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Демо-пользователь admin/admin при первом запуске
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/admin.groovy

# Пропускаем мастер первоначальной настройки (плагины уже установлены)
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
