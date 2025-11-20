"""Unit tests for basic math operations."""

from src.operations import add, subtract, multiply, divide, power, percent
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 2) == 4.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(4, 0.5) == 2

def test_percent():
    assert percent(200, 10) == 20
    assert percent(50, 50) == 25