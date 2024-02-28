import pytest
import source.functions as func


def test_add():
    result = func.add(1, 2)
    assert result == 3


def test_add_strings():
    result = func.add("I like", " burger")
    assert result == "I like burger"


def test_multiply():
    result = func.multiply(3, 4)
    assert result == 12


def test_divide():
    result = func.divide(5, 5)
    assert result == 1


# divide by zero error.
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        func.divide(10, 0)
