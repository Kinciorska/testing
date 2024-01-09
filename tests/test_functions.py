import pytest

import source.functions as functions


def test_add():
    result = functions.add(1, 2)
    assert result == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        functions.divide(1 / 0)
