build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

makemigrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

flake8:
	docker compose -f local.yml exec api flake8 .