import pytest

from package import other_module as sut

IN_PUT = "01234567890"
OUT_PUT = "09876543210"

def test_short_method():
    assert OUT_PUT == sut.short_method(IN_PUT)

@pytest.mark.integration_test
def test_medium_method():
    assert OUT_PUT == sut.medium_method(IN_PUT)

@pytest.mark.slow_integration_test
def test_long_method():
    assert OUT_PUT == sut.long_method(IN_PUT)
