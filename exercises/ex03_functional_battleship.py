"""EX03 - functional battleship!"""

__author__ = "730472183"

import random

BLUE_BOX: str = ("\U0001F7E6")
RED_BOX: str = ("\U0001F7E5")
WHITE_BOX: str = ("\U00002B1C")
escape_sequence: str = ("\n")


def input_guess(grid_size: int, guess_type: str) -> int:
    """Input guess function!"""
    assert guess_type == "row" or guess_type == "column"
    
    while True:
        user_guess = int(input(f"Guess a {guess_type}: "))
        user_guess = int(user_guess)
        if 1 <= user_guess <= grid_size:
            return user_guess
        else:
            print(f"The grid is only {grid_size} by {grid_size}. Try again: ")


EMPTY_BOX = "🟦"
HIT_BOX = "🟥"
MISS_BOX = "⬜"


def print_grid(grid_size: int, row_guess: int, column_guess: int, is_correct: bool) -> None:
    """Grid function!"""
    row_counter = 1
    while row_counter <= grid_size:
        column_counter = 1
        row_string = ""

        while column_counter <= grid_size:
            if row_counter == row_guess and column_counter == column_guess:
                if is_correct:
                    row_string += HIT_BOX
                else:
                    row_string += MISS_BOX
            else:
                row_string += EMPTY_BOX

            column_counter += 1

        print(row_string)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Correct guess function!"""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False
    

def main(grid_size_main: int, secret_row_main: int, secret_column_main: int) -> None:
    """Main function!"""
    turn = 1
    
    while turn <= 5:
        print(f"=== Turn {turn}/5 ===")

        user_row_guess = input_guess(grid_size_main, "row")
        user_column_guess = input_guess(grid_size_main, "column")

        is_correct = correct_guess(secret_row_main, secret_column_main, user_row_guess, user_column_guess)
        print_grid(grid_size_main, user_row_guess, user_column_guess, is_correct)
        if is_correct:
            print(f"Hit! You won in {turn}/5 turns!")
            break
        else:
            print("Miss!")
            turn += 1
    else:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))