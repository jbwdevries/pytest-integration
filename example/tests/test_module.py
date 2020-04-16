import pytest

from package import module as sut

@pytest.mark.slow_integration_test
def test_slow_integration_testable_method_two():
    assert 2 == sut.slow_integration_testable_method_two()

@pytest.mark.slow_integration_test
def test_slow_integration_testable_method_ten():
    assert 10 == sut.slow_integration_testable_method_ten()

@pytest.mark.slow_integration_test
def test_slow_integration_testable_method_tenthousand():
    assert 10000 == sut.slow_integration_testable_method_tenthousand()

@pytest.mark.integration_test
def test_integration_testable_method_one():
    assert 1 == sut.integration_testable_method_one()

@pytest.mark.integration_test
def test_integration_testable_method_nine():
    assert 9 == sut.integration_testable_method_nine()

@pytest.mark.integration_test
def test_integration_testable_method_thousand():
    assert 1000 == sut.integration_testable_method_thousand()

def test_unit_testable_method_zero():
    assert 0 == sut.unit_testable_method_zero()

def test_unit_testable_method_eight():
    assert 8 == sut.unit_testable_method_eight()

def test_unit_testable_method_hundred():
    assert 100 == sut.unit_testable_method_hundred()

@pytest.mark.xfail
def test_unit_xfail():
    assert False
