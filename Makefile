all:
	$(MAKE) -C example all
	example/venv/bin/python -m pylint pytest_integration
