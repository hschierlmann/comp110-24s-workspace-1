"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730472183"

user_input: str = input("pick a secret boat location between 1 and 4: ")
user_number: int = int(user_input)

if user_number < 1:
    print(f"Error! {user_number} too low!")
    exit()
if user_number > 4:
    print(f"Error! {user_number} too high!")
    exit()

user2_input: str = input("Guess a number between 1 and 4: ")
user2_number: int = int(user2_input)

if user2_number < 1:
    print(f"Error! {user2_number} too low!")
    exit()
if user2_number > 4:
    print(f"Error! {user2_number} too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
BLUE_BOX2: str = "\U0001F7E6"
RED_BOX2: str = "\U0001F7E5"
WHITE_BOX2: str = "\U00002B1C"
BLUE_BOX3: str = "\U0001F7E6"
RED_BOX3: str = "\U0001F7E5"
WHITE_BOX3: str = "\U00002B1C"
BLUE_BOX4: str = "\U0001F7E6"
RED_BOX4: str = "\U0001F7E5"
WHITE_BOX4: str = "\U00002B1C"

if user2_number == user_number == 1:
    print(RED_BOX + BLUE_BOX2 + BLUE_BOX3 + BLUE_BOX4)
else:
    print(WHITE_BOX + BLUE_BOX2 + BLUE_BOX3 + BLUE_BOX4)

if user2_number == user_number == 2:
    print(BLUE_BOX + RED_BOX2 + BLUE_BOX3 + BLUE_BOX4)
else:
    print(BLUE_BOX + WHITE_BOX2 + BLUE_BOX3 + BLUE_BOX4)

if user2_number == user_number == 3:
    print(BLUE_BOX + BLUE_BOX2 + RED_BOX3 + BLUE_BOX4)
else:
    print(BLUE_BOX + BLUE_BOX2 + WHITE_BOX3 + BLUE_BOX4)

if user2_number == user_number == 4:
    print(BLUE_BOX + BLUE_BOX2 + BLUE_BOX3 + RED_BOX4)
else:
    print(BLUE_BOX + BLUE_BOX2 + BLUE_BOX3 + WHITE_BOX4)

if user2_number == user_number:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")