.PHONY: open restart restart-build

WEB_PORT=5000
APP_ENV=dev

# Подгрузка настроек докера, чтобы изменять файлы конфигов через sed (nginx, supervisor, etc..)
ifneq (",$(wildcard ./.env.docker.${APP_ENV}.local)")
    include .env.docker.${APP_ENV}.local
endif

INTERACTIVE := $(shell [ -t 0 ] && echo 1)
ifdef INTERACTIVE # is a terminal
	EXEC_TTY :=
else # cron job
	EXEC_TTY := -T
endif

ifneq (",$(wildcard /usr/bin/docker-compose-v1)")
	DOCKER_COMPOSE_BIN := /usr/bin/docker-compose-v1
else ifneq (",$(wildcard /usr/local/bin/docker-compose-v1)")
	DOCKER_COMPOSE_BIN := /usr/local/bin/docker-compose-v1
else ifneq (",$(wildcard /usr/bin/docker-compose)")
	DOCKER_COMPOSE_BIN := /usr/bin/docker-compose
else
    DOCKER_COMPOSE_BIN := $(shell which docker-compose)
endif

ifeq ($(OS),Windows_NT)
    DOCKER_COMPOSE_BIN := winpty docker-compose
endif

args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`
env = ${APP_ENV}
pwd = $(shell eval pwd -P)

ifneq (",$(wildcard ./docker-compose.local.yml)")
    docker-compose = ${DOCKER_COMPOSE_BIN} --file=./.docker/docker-compose.yml --file=./.docker/docker-compose.${env}.yml --file=./docker-compose.local.yml --env-file=./.env.docker.${env}.local -p "${pwd}_${env}"
else
    docker-compose = ${DOCKER_COMPOSE_BIN} --file=./.docker/docker-compose.yml --file=./.docker/docker-compose.${env}.yml --env-file=./.env.docker.${env}.local -p "${pwd}_${env}"
endif

# https://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux
# Reset
Color_Off = \033[0m
# Regular Colors
Black = \033[0;30m
Red = \033[0;31m
Green = \033[0;32m
Yellow = \033[0;33m
Blue = \033[0;34m
Purple = \033[0;35m
Cyan = \033[0;36m
White = \033[0;37m

help:
	@echo -e "[${env}]: ENV = ${Yellow}${env}${Color_Off} get from ${DEFAULT_ENV_FILE}"
	@if [ ! -f .env.local ]; then \
  		echo -e "[${env}]: No configuration found."; \
  		echo -e "[${env}]: Run '${Yellow}make init-configs${Color_Off}' for default ENV"; \
  		echo -e "[${env}]: or '${Yellow}make env=dev init-configs${Color_Off}' for development ENV."; \
  		echo -e "[${env}]: When edit generated config files!"; \
	else \
		echo -e "[${env}]: For deploying application run '${Yellow}make deploy${Color_Off}'"; \
		echo -e "[${env}]: Open in browser '${Yellow}make open${Color_Off}' or click ${Yellow}http://localhost:${WEB_PORT}${Color_Off}"; \
	fi

restart: down up
restart-build: down build up

open:
	@if [ "$(shell uname -s)" = "Linux" ]; then \
		xdg-open http://localhost:${WEB_PORT}; \
	else \
		start http://localhost:${WEB_PORT}; \
	fi

build:
	@echo "[${env}]: build containers..."
	@${docker-compose} build
	@echo "[${env}]: containers builded!"

up:
	@echo "[${env}]: start containers..."
	@${docker-compose} up -d
	@echo "[${env}]: containers started!"
	@if [ ${env} = 'dev' ]; then \
		echo -e "Open in browser '${Yellow}make open${Color_Off}' or click ${Yellow}http://localhost:${WEB_PORT}${Color_Off}"; \
	fi

down:
	@echo "[${env}]: stopping containers..."
	@${docker-compose} down --remove-orphans
	@echo "[${env}]: containers stopped!"

ps:
	@${docker-compose} ps

### DataBase
# https://stackoverflow.com/questions/63934856/why-is-pg-restore-segfaulting-in-docker
db-bash:
	@${docker-compose} exec ${EXEC_TTY} db bash;

# https://stackoverflow.com/questions/54090238/stop-executing-makefile
# make: *** No rule to make target `my'.  Stop.
%:
	@true
