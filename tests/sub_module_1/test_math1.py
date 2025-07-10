import pytest

from sub_module_1.math1 import (
    custom_power, custom_add
)

def test_custom_power():
    assert custom_power(0) == 0
    assert custom_power(1) == 1
    assert custom_power(2) == 4
    assert custom_power(4) == 16

def test_custom_add():
    assert custom_add(0, 1) == 1
    assert custom_add(0, 0) == 0
    assert custom_add(100, 10) == 110
    assert custom_add(0.1, 0.2) == pytest.approx(0.3)