# Единые команды: локально и в CI вызывается одно и то же.
# Это важный принцип: "если работает локально — сработает и в CI".

.PHONY: install test lint docker-build docker-run act

install:        ## Установить зависимости
	pip install -r app/requirements.txt

test:           ## Прогнать тесты
	pytest app/tests -v

lint:           ## Линтер (ruff)
	ruff check app/

docker-build:   ## Собрать Docker-образ
	docker build -t calc-app app/

docker-run:     ## Запустить приложение в Docker
	docker run --rm -p 5000:5000 calc-app

act:            ## Прогнать GitHub Actions локально
	act push -W .github/workflows/01-basic-ci.yml
