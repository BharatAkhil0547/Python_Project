
import pytest

from calc import add, subtract, multiply, divide


def test_add():
    assert add(10, 5) == 15


def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
