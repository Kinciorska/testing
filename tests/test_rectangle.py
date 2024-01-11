import pytest


def test_area(defined_rectangle):
    assert defined_rectangle.area() == 10 * 5


def test_perimeter(defined_rectangle):
    assert defined_rectangle.perimeter() == (2 * 10) + (2 * 5)
