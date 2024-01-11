import pytest

import source.shapes as shapes


@pytest.fixture
def defined_rectangle():
    return shapes.Rectangle(10, 5)


@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(5, 2)
