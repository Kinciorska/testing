import pytest

import source.shapes as shapes

square_area_values = [
    (5, 25),
    (4, 16),
    (3, 9)
]

square_perimeter_values = [
    (5, 20),
    (4, 16),
    (3, 12)
]


@pytest.mark.parametrize('side_length, expected_area', square_area_values)
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize('side_length, expected_perimeter', square_perimeter_values)
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
