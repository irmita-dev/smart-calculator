"""Basic math operations for the smart calculator."""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return the difference of two numbers."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b

def divide(a: Number, b: Number) -> Number:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a: Number, b: Number) -> Number:
    """Return a raised to the power of b."""
    return a ** b

def percent(a: Number, b: Number) -> Number:
    """Return b percent of a (e.g. percent(200, 10) ->20)."""
    return (a * b) / 100