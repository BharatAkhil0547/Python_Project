
import pytest

from calc import add,subtract,multiply, divide


def test_add():
    assert add(10, 5) == 15

# update the test subtract code in branch1
def test_subtract():
    assert subtract(10,5)==5

# update the test multiply code in  branch2
def test_multiply():
    assert multiply(10,5)==50

def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
