"""Ice cream lesson."""

def odd_and_even(x: list[int]) -> list[int]:
    """Odd."""
    new_list: list[int] = []
    i: int = 0
    
    while i < len(x):
        for elem in x:
            if elem % 2 == 1 and i % 2 == 0:
                new_list.append(elem)
                i += 1
            else:
                i += 1

    return new_list

odd_and_even([7, 8, 10, 10, 5, 12, 3, 2, 11, 8])