.PHONY: format lint dev

# >-----< SETUP >-----< #

PYTHON = .venv/bin/python
PIP = .venv/bin/pip

# >-----< FUNCTIONS >-----< #

clean:
	$(PYTHON) scripts/clean.py

format:
	$(PYTHON) -m black source/
	$(PYTHON) -m isort source/

lint:
	$(PYTHON) -m flake8 source/

build:
	poetry build --output=out/ --format=wheel

dev:
	$(PYTHON) source/main.py -- --dev
