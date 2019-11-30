pytest-integration
==================

Overview
--------
Plugin for [pytest](https://pypi.org/project/pytest/) to mark tests as
integration or slow integration.

Integration tests are run after normal tests (unit tests) and
slow integration tests are run after (quick) integration tests.

If a unit test fails, (quick) integration and slow integration tests are not run.

If a (quick) integration tests fails, slow integration tests are not run.

If you have also installed [pytest-cov](https://pypi.org/project/pytest-cov/),
then code coverage is disabled for all integration tests, since unit tests
are supposed to cover all the code.

Added pytest markers
--------------------------
- `@pytest.mark.integration_test` Marks this test as a (quick) integration test
- `@pytest.mark.slow_integration_test` Marks this test as a slow integration test

Added pytest command line options
--------------------------
- `--with-integration` Run (quick) integration tests (default)
- `--with-slow-integration` Run slow integration tests (default)
- `--integration-cover` Let integration tests contribute to coverage

`with` options also have a `without` variant.

Example
-------
See the example directory. Examples of how to run are in the Makefile.
