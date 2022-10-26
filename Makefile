SHELL := /bin/bash
APPLICATION_NAME="Tipper"
APPLICATION_VERSION=1.0

.PHONY: init-db
db-migrate:
	docker-compose -f docker-compose-dev.yml run --rm app /bin/bash -c "alembic upgrade head"

.PHONY: up
up:
	docker-compose -f docker-compose-dev.yml up --build

.PHONY: build-test
build-test:

.PHONY: test
test:
	docker-compose -f docker-compose-test.yml build
	docker-compose -f docker-compose-test.yml run --rm app /bin/bash -c "pytest /tipper/"
