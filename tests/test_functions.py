import pytest
import time

import source.functions as functions


def test_add():
    result = functions.add(1, 2)
    assert result == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        functions.divide(1 / 0)


@pytest.mark.slow
def test_slow_add_test():
    time.sleep(2)
    result = functions.add(1, 2)
    assert result == 3


@pytest.mark.skip(reason="This feature is broken")
def test_skip_test():
    pass


@pytest.mark.xfail(reason="We know we cannot divide by 0")
def test_divide_by_zero_is_broken():
    functions.divide(1 / 0)
