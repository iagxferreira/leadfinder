.PHONY: help sync run lint format test check clean

help:
	@echo "make sync    - install project + dev dependencies"
	@echo "make run CITY=\"Barbacena, MG, Brasil\" [CATEGORIES=\"padaria,salão de beleza\"] [OUTPUT=leads.csv]"
	@echo "make lint    - run ruff check"
	@echo "make format  - run ruff format"
	@echo "make test    - run pytest"
	@echo "make check   - lint + test"
	@echo "make clean   - remove caches and generated CSV output"

sync:
	uv sync

run:
	@if [ -z "$(CITY)" ]; then echo "usage: make run CITY=\"City, State, Country\""; exit 1; fi
	uv run leadfinder --city "$(CITY)" \
		$(if $(CATEGORIES),--categories "$(CATEGORIES)") \
		$(if $(OUTPUT),--output "$(OUTPUT)")

lint:
	uv run ruff check .

format:
	uv run ruff format .

test:
	uv run pytest

check: lint test

clean:
	rm -rf .ruff_cache .pytest_cache **/__pycache__ leads.csv
