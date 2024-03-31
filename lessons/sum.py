"""Summing the elements of a list using different loops."""

__author__ = "730472183"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of elements using a while loop."""
    result = 0.0
    index = 0

    while index < len(vals):
        result += vals[index]
        index += 1

    return result


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of elements using a for loop."""
    result = 0.0

    for value in vals:
        result += value

    return result


def f_range_sum(vals: list[float]) -> float:
    """Calculate the sum of elements using a for loop with range."""
    result = 0.0

    for i in range(len(vals)):
        result += vals[i]

    return result
