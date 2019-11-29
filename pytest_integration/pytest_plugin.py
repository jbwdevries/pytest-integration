"""
Plugin for pytest to organize test by unit, (quick) integration
or slow integration tests.

See https://github.com/jbwdevries/pytest-integration
"""

import pytest

def pytest_load_initial_conftests(early_config, parser, args):
    """
    Adds configuration options for pytest-integration
    """
    del early_config
    del args

    parser.addoption(
        '--with-integration', action='store_const', const=True,
        dest='run_integration')
    parser.addoption(
        '--without-integration', action='store_const', const=False,
        dest='run_integration')
    parser.addoption(
        '--with-slow-integration', action='store_const', const=True,
        dest='run_slow_integration')
    parser.addoption(
        '--without-slow-integration', action='store_const', const=False,
        dest='run_slow_integration')

    parser.addoption('--integration-cover', action='store_true')

def pytest_configure(config):
    """
    Adds markers for pytest-integration
    """
    config.addinivalue_line(
        "markers", "integration_test: mark test to run after unit tests "
        "are complete"
    )

    config.addinivalue_line(
        "markers", "slow_integration_test: mark test to run after unit tests "
        "and (quick) integration tests are complete"
    )

@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):
    """
    Sorts the items; unit test first, then (quick) integration tests, then
    slow integration tests.

    Also applies the `no_cover` marker, unless the user has requested us not to.
    """
    del session

    items.sort(key=_get_items_key)

    if config.getoption('integration_cover'):
        return

    no_cover_found = False
    for line in config.getini('markers'):
        # See _pytest/mark/structures.py
        marker = line.split(":")[0].split("(")[0].strip()
        if marker == 'no_cover':
            no_cover_found = True
            break

    if not no_cover_found:
        # pytest-cov not installed, nothing to do here
        return

    for item in items:
        if (item.get_closest_marker('integration_test')
                or item.get_closest_marker('slow_integration_test')):
            item.add_marker('no_cover')

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """
    Checks whether tests should be skipped based on integration settings
    """

    if item.get_closest_marker('integration_test'):
        if item.config.getoption('run_integration') in (None, True):
            return
        pytest.skip('Integration tests skipped')

    if item.get_closest_marker('slow_integration_test'):
        if item.config.getoption('run_slow_integration') in (None, True):
            return
        pytest.skip('Slow integration tests skipped')

def pytest_runtest_makereport(item, call):
    """
    Turns of running (quick) integration tests or integration tests
    if one of the previous stages failed.
    """

    if not call.excinfo or call.excinfo.value.__class__.__name__ == 'Skipped':
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
