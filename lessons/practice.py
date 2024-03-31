"""Demonstrate Basic List Syntax"""

# Initialize an empty list
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal

# Add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

def display(list: list[str]) -> str:
    print(display)

def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1,word2]
    return my_list


print(create("you","all"))


def plus_or_minus_n(inpdict: dict[str, int], n: int) -> None:
    for keys in inpdict:
        if inpdict[keys] % 2 == 0:
            inpdict[keys] += n
        elif inpdict[keys] % 2 == 1:
            inpdict[keys] -= n


def value_exists(xdict: dict[str, int], testnum: int) -> bool:
    condition = False
    for key in xdict:
        if xdict[key] == testnum:
            condition = True
    return condition
            

        

test_dict: dict[str,int] = {"a": 2, "b": 4, "c": 7, "d": 1}
test_val: int = 4
value_exists(test_dict, test_val)