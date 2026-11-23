
import pytest

from calc import add,subtract, divide


def test_add():
    assert add(10, 5) == 15

# update the test subtract code in branch1
def test_subtract():
    assert subtract(10,5)==5

def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
