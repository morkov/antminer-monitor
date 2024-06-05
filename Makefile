
PYTHON_VERSION ?= 3.11
POETRY_VERSION ?= 1.8.0
POETRY_CACHE_DIR ?= .cache
POETRY_VENV ?= .venv


clean:
	rm -fr *.egg-info build dist */version.json
	find . -iname '*.pyc' -delete


purge: clean
	rm -fr $(POETRY_ENV)


develop: clean purge
	python$(PYTHON_VERSION) -m venv $(POETRY_VENV) \
		&& $(POETRY_VENV)/bin/pip install -U pip setuptools \
		&& $(POETRY_VENV)/bin/pip install poetry==${POETRY_VERSION}

	$(POETRY_VENV)/bin/poetry check
	$(POETRY_VENV)/bin/poetry install --no-interaction --no-cache
