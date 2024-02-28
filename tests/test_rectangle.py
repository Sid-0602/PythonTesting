import pytest
import source.shapes as shapes


# Pytest fixtures are reusable functions that provide a way to manage
# states and dependencies in test cases
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)


@pytest.fixture
def other_reactangle():
    return shapes.Rectangle(4, 20)


def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (10 + 20)


def test_not_equal(my_rectangle, other_reactangle):
    assert my_rectangle != other_reactangle
