import pytest

import calculator


def test_add():
    assert calculator.add(2, 3) == 6


def test_sub():
    assert calculator.sub(10, 4) == 6


def test_mul():
    assert calculator.mul(3, 7) == 21


def test_div():
    assert calculator.div(10, 2) == 5


def test_div_by_zero():
    with pytest.raises(ValueError):
        calculator.div(1, 0)
