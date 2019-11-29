pytest-integration
------------------

Plugin for [pytest](https://pypi.org/project/pytest/) to mark tests as
integration or slow integration.

Integration tests are run after normal tests (unit tests) and
slow integration tests are run after (quick) integration tests.

If a unit test fails, quick and slow integration tests are not run.

If a quick integration tests fails, slow integration tests are not run.
