"""List Utilities - Ex 04!"""

__author__ = "730472183"


def all(numbers: list[int], target: int) -> bool:
    """All function definition!"""
    if not numbers:
        return False
    for item in numbers:
        if item != target:
            return False
    return True
        

def max(numbs: list[int]) -> int:
    """Returns the max number!"""
    if len(numbs) == 0:
        raise ValueError("max() arg is an empty List")

    max_num = numbs[0]
    for items in numbs:
        if items > max_num:
            max_num = items

    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determining if two lists are equal."""
    if len(list1) != len(list2):
        return False
    
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appending list 1."""
    for item in list2:
        list1.append(item)
