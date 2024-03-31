"""Mutating Functions!"""


__author__ = "730472183"


def manual_append(input: list[int], mod: int) -> None:
    """Appends mod to end!"""
    input.append(mod)
    return


def double(input: list[int]) -> None:
    """Multiples input by 2!"""
    i: int = 0 
    while i < len(input):
        input[i] = input[i] * 2
        i = i + 1
    return