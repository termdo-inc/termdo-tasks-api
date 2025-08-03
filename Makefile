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

run:
	$(PYTHON) -m termdo_tasks_api.main --dev
