"""Exercise 2 -- One shot Battleship."""

__author__: str = "730472183"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

correct: bool = False

BLUE_BOX: str = ("\U0001F7E6")
RED_BOX: str = ("\U0001F7E5")
WHITE_BOX: str = ("\U00002B1C")
escape_sequence: str = ("\n")

while not correct:
    row_guess = int(input("Guess a row: "))
    while row_guess > grid_size or row_guess < 1:
        row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    column_guess: int = int(input("Guess a column: "))
    while column_guess > grid_size or column_guess < 1:
        column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))   

    row_counter: int = 1

    while row_counter <= grid_size:
        row_string: str = ""
        column_counter: int = 1

        while column_counter <= grid_size:
            if row_counter == secret_row and column_counter == secret_column:
                if row_guess == secret_row and column_guess == secret_column:
                    row_string += RED_BOX
                else:
                    row_string += BLUE_BOX
            elif row_counter == row_guess and column_counter == column_guess:
                row_string += WHITE_BOX
            else:
                row_string += BLUE_BOX
            column_counter += 1

        print(row_string)
        row_counter += 1

    # Giving A Hint to User
    if row_guess == secret_row and column_guess == secret_column:
        print(f"Hit!{escape_sequence}")
        correct = True
    else:
        if row_guess == secret_row and column_guess != secret_column:
            print(f"Close! Correct row, wrong column.{escape_sequence}")
        elif column_guess == secret_column and row_guess != secret_row:
            print(f"Close! Correct column, wrong row.{escape_sequence}")
        else:
            print(f"Miss!{escape_sequence}")

        correct = True  