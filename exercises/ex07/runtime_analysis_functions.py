"""Assesses runtime of functions."""

__author__ = "730472183"

import numpy as np
import timeit
import tracemalloc

from random import randint
MAX_VAL: int = 10 ** 5


def random_descending_list(n: int) -> list[int]:
    """Generate a list of random descending integers."""
    new_list: list[int] = [MAX_VAL]
    for i in range(1, n):
        next_value: int = randint(0, MAX_VAL - 1)
        new_list.append(next_value)
    for i in range(len(new_list)):
        max_index: int = i
        for j in range(i + 1, len(new_list)):
            if new_list[j] > new_list[max_index]:
                max_index = j
        temp = new_list[max_index]
        new_list[max_index] = new_list[i]
        new_list[i] = temp
    return new_list


def evaluate_runtime(fn_name, start_size: int, end_size: int) -> np.array:
    """Evaluate the runtime for different size inputs."""
    from sort_functions import selection_sort, insertion_sort
    NUM_TRIALS: int = 1
    times: list[float] = []
    for inp_size in range(start_size, end_size + 1):
        l: list[int] = random_descending_list(inp_size)
        call_command: str = f"{fn_name}(l)"
        print(f"Trial {inp_size-start_size}/{end_size - start_size}")
        result = timeit.timeit(stmt=call_command, globals=locals(), number=NUM_TRIALS)
        times.append(result / NUM_TRIALS)
    print(f"Runtime of {fn_name} for input of size {end_size}: {round(result / NUM_TRIALS, 2)} seconds")
    return np.array(times)


def evaluate_memory_usage(fn_name, start_size: int, end_size: int):
    """Evaluates memory usage."""
    from sort_functions import selection_sort, insertion_sort
    usage: list[float] = []
    for inp_size in range(start_size, end_size + 1):
        l: list[int] = random_descending_list(inp_size)
        print(f"Trial {inp_size-start_size}/{end_size - start_size}")
        tracemalloc.start()
        locals()[fn_name](l)
        result = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        usage.append(result[1])
    print(f"Memory usage of {fn_name} for input of size {end_size}: {result[1]} blocks of memory.")
    return np.array(usage)