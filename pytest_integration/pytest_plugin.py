"""
Plugin for pytest to organize test by unit, (quick) integration
or slow integration tests.

See https://github.com/jbwdevries/pytest-integration
"""

import pytest

try:
    import pytest_cov # pylint: disable=W0611
    HAVE_PYTEST_COV = True
except ImportError:
    HAVE_PYTEST_COV = False

try:
    import pytest_timeout
    HAVE_PYTEST_TIMEOUT = True
except ImportError:
    HAVE_PYTEST_TIMEOUT = False

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

    if HAVE_PYTEST_COV:
        parser.addoption('--integration-cover', action='store_true')

    if HAVE_PYTEST_TIMEOUT:
        parser.addoption('--integration-timeout', type=int, default=0)
        parser.addoption(
            '--integration-timeout-method',
            type=_timeout_method, default='DEFAULT_METHOD')

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

    no_cover_marker = None
    if HAVE_PYTEST_COV and not config.getoption('integration_cover'):
        no_cover_marker = pytest.mark.no_cover

    timeout_marker = None
    if HAVE_PYTEST_TIMEOUT and config.getoption('integration_timeout') > 0:
        timeout_marker = pytest.mark.timeout

    if not no_cover_marker and not timeout_marker:
        # pytest-cov and pytest-timeout not installed, or disabled
        # nothing to do here
        return

    for item in items:
        if item.get_closest_marker('integration_test'):
            if no_cover_marker:
                item.add_marker(no_cover_marker)

            if timeout_marker:
                item.add_marker(timeout_marker(
                    timeout=config.getoption('integration_timeout'),
                    method=config.getoption('integration_timeout_method'),
                ))

        if item.get_closest_marker('slow_integration_test'):
            if no_cover_marker:
                item.add_marker(no_cover_marker)

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
    if item.get_closest_marker("xfail"):
        return

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

def _timeout_method(item):
    if HAVE_PYTEST_TIMEOUT and item == 'DEFAULT_METHOD':
        return pytest_timeout.DEFAULT_METHOD

    if item not in ['thread', 'signal']:
        raise ValueError('Invalid timeout method')

    return item
