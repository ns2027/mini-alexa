"""Parse exactly two finite numbers and a basic operator; never execute input."""
import math
import re

NUMBER = r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
EXPRESSION = re.compile(r"\s*(" + NUMBER + r")\s*([+*/-])\s*(" + NUMBER + r")\s*")


def parse_expression(text):
    match = EXPRESSION.fullmatch(text)
    if not match:
        raise ValueError("Use two numbers and +, -, *, or /, for example: 12 + 8.")
    left, operator, right = match.groups()
    return float(left), operator, float(right)


def calculate(left, operator, right):
    if not all(math.isfinite(n) for n in (left, right)):
        raise ValueError("Please use finite numbers of a smaller size.")
    if operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right
    elif operator == '*':
        result = left * right
    elif operator == '/':
        if right == 0:
            raise ValueError("I can't divide by zero. Try a different number.")
        result = left / right
    else:
        raise ValueError("Supported operators: +, -, *, /.")
    if not math.isfinite(result):
        raise ValueError("The result is too large. Try smaller numbers.")
    return result
