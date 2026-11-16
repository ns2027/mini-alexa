"""Educational rules and one fixed-weight neuron; no training occurs."""
from datetime import datetime
import math

WEIGHTS = (0.6, -0.4)
BIAS = -0.2


def recommend_activity(hour=None):
    """A hand-written decision tree assigns an activity class to an hour."""
    if hour is None:
        hour = datetime.now().hour
    if not 0 <= hour <= 23:
        raise ValueError("Hour must be between 0 and 23.")
    if hour < 5:
        return "Rest and get some sleep."
    elif hour < 12:
        return "Have breakfast and plan your study tasks."
    elif hour < 17:
        return "Have lunch and work on your project."
    elif hour < 21:
        return "Take a walk or exercise, then review your day."
    return "Have dinner and prepare for sleep."


def perceptron(inputs):
    """Forward pass: weighted sum plus bias, then step activation (> 0)."""
    if len(inputs) != len(WEIGHTS) or not all(math.isfinite(x) for x in inputs):
        raise ValueError("Enter exactly two finite numbers.")
    total = sum(x * w for x, w in zip(inputs, WEIGHTS)) + BIAS
    if not math.isfinite(total):
        raise ValueError("Numbers are too large. Try smaller values.")
    return total, int(total > 0)


def perceptron_demo():
    print("Mini Alexa: One artificial neuron with fixed weights; no training or deep network.")
    raw = input("Enter two numbers separated by a space (or cancel): ").strip().lower()
    if raw in {"cancel", "back"}:
        return "Demo cancelled."
    if raw in {"exit", "quit", "bye"}:
        raise EOFError
    try:
        values = [float(x) for x in raw.split()]
        total, output = perceptron(values)
    except ValueError as error:
        return f"Invalid input: {error}"
    return (f"Inputs: {values}; weights: {WEIGHTS}; bias: {BIAS}\n"
            f"Weighted sum: ({values[0]:g} * {WEIGHTS[0]}) + "
            f"({values[1]:g} * {WEIGHTS[1]}) + ({BIAS}) = {total:g}\n"
            f"Step activation: 1 if sum > 0, otherwise 0. Output: {output}")
