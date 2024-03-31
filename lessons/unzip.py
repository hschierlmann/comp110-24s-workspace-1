"""Splitting a dictionary into two lists."""

__author__ = "730472183"


def get_keys(x_dict: dict[str, int]) -> list[str]:
    """Returns a list of keys."""
    key_list: list[str] = []
    for keys in x_dict:
        key_list.append(keys)
    return key_list
    

def get_values(y_dict: dict[str, int]) -> list[int]:
    """Returns a list of values."""
    value_list: list[int] = []
    for keys in y_dict:
        value_list.append(y_dict[keys])
    return value_list
    