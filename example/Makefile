all: test

test: venv/pip.done
#	venv/bin/python -m pytest -v --without-integration --without-slow-integration
#	venv/bin/python -m pytest -v --without-slow-integration
	venv/bin/python -m pytest

venv/pip.done: venv requirements.txt ../setup.py $(wildcard ../pytest_integration/*)
	venv/bin/python -m pip uninstall pytest_integration --yes || true
	venv/bin/python -m pip install -r requirements.txt
	touch $@

venv:
	python3 -m venv venv
