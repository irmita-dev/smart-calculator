"""Calculator core logic."""

from typing import Union
from .operations import add, subtract, multiply, divide, power, percent
from .utils import parse_expression, format_number

Number = Union[int, float]


class Calculator:
    """Smart calculator that evaluates simple expressions."""

    def evaluate(self, expression: str) -> str:
        expression = expression.strip()

        if not expression:
            return "No input."

        parsed = parse_expression(expression)
        if parsed is None:
            return "Invalid expression. Use: <number> <op> <number>"

        left, op, right = parsed

        try:
            result = self._apply_operation(left, op, right)
        except ZeroDivisionError:
            return "Error: cannot divide by zero."

        return format_number(result)

    def _apply_operation(self, left: Number, op: str, right: Number) -> Number:
        if op == "+":
            return add(left, right)
        if op == "-":
            return subtract(left, right)
        if op == "*":
            return multiply(left, right)
        if op == "/":
            return divide(left, right)
        if op == "^":
            return power(left, right)
        if op == "%":
            return percent(left, right)

        raise ValueError(f"Unsupported operator: {op}")