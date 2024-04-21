"""Functions that implement sorting algorithms."""

__author__ = "730472183"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = key
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for i in range(len(x)):
        min_index = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_index]:
                min_index = j
        x[i], x[min_index] = x[min_index], x[i]
    return None