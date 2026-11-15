from main import *
import pytest

def test_add():
    assert add(2, 3) == 5

def test_diff():
    assert diff(5, 3) == 2

def test_mul():
    assert mul(2, 5) == 10

def test_div_zero():
    with pytest.raises(ValueError):
        div(5, 0)

def test_div():
    assert div(6, 2) == 3