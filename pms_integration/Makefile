.PHONY: run test lint migrate makemigrations superuser shell

# Setup
install:
	pip install -r requirements.txt

# Run the dev server
run:
	python manage.py runserver

# Apply migrations
migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

# Run unit tests
test:
	python manage.py test

# Run linter
lint:
	flake8 .

# Clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
