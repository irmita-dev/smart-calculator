"""Utility helpers for the smart calculator."""

from typing import Optional, Tuple, Union

Number = Union[int, float]


def parse_expression(expr: str) -> Optional[Tuple[Number, str, Number]]:
    """Parse a simple expression of the form: <number> <operator> <number>.

    Example:
      "10 + 5" -> (10, "+", 5.0)

    Returns:
      Tuple (left, operator, right) or None if parsing fails.
    """
    parts = expr.strip().split()

    if len(parts) != 3:
        return None

    left_str, op, right_str = parts

    try:
      left = float(left_str)
      right = float(right_str)
    except ValueError:
      return None

    if op not in {"+", "-", "*", "/", "^", "%"}:
        return None
    
    return (left, op, right)

def format_number(value: Number) -> str:
    """Format a number for display.

    - integers are shown without .0
    - other numbers are rounded to a reasonable length
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))

    # limit length but keep precision
    return f"{value:.10g}"

def is_exit_command(text: str) -> bool:
    """Return True if the user wants to quit."""
    lowered = text.strip().lower()
    return lowered in {"exit", "quit", "q", "x"}