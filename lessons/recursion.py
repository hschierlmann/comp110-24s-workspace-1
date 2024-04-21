"""Defining f."""

__author__ = "730472183"


def f(n: int, k: int) -> int:
    """Recursion."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)