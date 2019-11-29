all: test-default

test-default: venv/pip.done
	venv/bin/python -m pytest --cov=package

test-with-cover: venv/pip.done
	venv/bin/python -m pytest --cov=package --integration-cover

test-no-integration: venv/pip.done
	venv/bin/python -m pytest --cov=package --without-integration

test-no-slow-integration: venv/pip.done
	venv/bin/python -m pytest --cov=package --without-slow-integration

test-no-any-integration: venv/pip.done
	venv/bin/python -m pytest --cov=package --without-integration --without-slow-integration

venv/pip.done: venv requirements.txt ../setup.py $(wildcard ../pytest_integration/*)
	venv/bin/python -m pip uninstall pytest_integration --yes || true
	venv/bin/python -m pip install -r requirements.txt
	touch $@

venv:
	python3 -m venv venv
