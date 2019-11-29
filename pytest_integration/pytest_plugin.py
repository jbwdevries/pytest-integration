import pytest

def pytest_load_initial_conftests(early_config, parser, args):
    parser.addoption('--with-integration', action='store_const', const=True, dest='run_integration')
    parser.addoption('--without-integration', action='store_const', const=False, dest='run_integration')
    parser.addoption('--with-slow-integration', action='store_const', const=True, dest='run_slow_integration')
    parser.addoption('--without-slow-integration', action='store_const', const=False, dest='run_slow_integration')

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "integration_test: mark test to run after unit tests "
        "are complete"
    )

    config.addinivalue_line(
        "markers", "slow_integration_test: mark test to run after unit tests "
        "and quick integration tests are complete"
    )

def pytest_addoption(parser, pluginmanager):
    print('Hello from pytest_integration')

@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):
    items.sort(key=_get_items_key)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    if item.get_closest_marker('integration_test'):
        if item.config.getoption('run_integration') in (None, True):
            return
        pytest.skip('Integration tests skipped')

    if item.get_closest_marker('slow_integration_test'):
        if item.config.getoption('run_slow_integration') in (None, True):
            return
        pytest.skip('Slow integration tests skipped')

def pytest_runtest_makereport(item, call):
    if not call.excinfo:
        return

    if item.get_closest_marker('slow_integration_test'):
        return

    item.config.option.run_slow_integration = False

    if item.get_closest_marker('integration_test'):
        return

    item.config.option.run_integration = False

def _get_items_key(item):
    if item.get_closest_marker('slow_integration_test'):
        return 2

    if item.get_closest_marker('integration_test'):
        return 1

    return 0
