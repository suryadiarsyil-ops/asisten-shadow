.PHONY: help install test lint format clean run dev build docs

help:
	@echo "Asisten Shadow - Makefile Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code with black"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make run        - Run the application"
	@echo "  make dev        - Setup development environment"
	@echo "  make build      - Build package"
	@echo "  make docs       - Generate documentation"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install pytest pytest-cov black flake8 pylint mypy

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

lint:
	flake8 src/ tests/
	pylint src/ tests/

format:
	black src/ tests/

format-check:
	black --check src/ tests/

type-check:
	mypy src/

security-check:
	safety check
	bandit -r src/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run:
	python src/main.py

dev:
	make install-dev
	make test
	make lint

build:
	python -m build

build-check:
	twine check dist/*

docs:
	cd docs && make html

all: clean install-dev test lint build

ci: install-dev test-cov lint format-check security-check

# Docker commands (optional)
docker-build:
	docker build -t asisten-shadow:latest .

docker-run:
	docker run -it asisten-shadow:latest

# Release commands
release-test:
	twine upload --repository testpypi dist/*

release:
	twine upload dist/*

# Git hooks
pre-commit:
	make format
	make lint
	make test
