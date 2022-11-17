# Changelog

## [0.2.3] - 2022-11-17

### Fixed

- Fixed the pytest11 entry point; it was using a copied name from the example
  documentation, rather than properly name it. This would break other plugins
  that made the same mistake.

## [0.2.2] - 2020-04-16

### Fixed

- Integration tests are no longer skipped on tests marked with xfail

## [0.2.1] - 2020-04-13

### Fixed

- pytest_timeout is now fully optional

## [0.2.0] - 2019-12-03

### Added

- integration-timeout command line option
- integration-timeout-method command line option

## [0.1.0] - 2019-12-02

Inital version
