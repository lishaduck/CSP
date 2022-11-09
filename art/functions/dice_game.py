"""Program: dice_game.py - Dice Game.

Elisha Dukes - Mrs. Carson
"""
# https://docs.google.com/document/d/1gsrZj1p-Fvj0YEs63Kgxv3U2-nb4cfKiteWztdGWquk/edit


# Import Statments
import random

# import re
import sys
import time
from typing import Any

import art  # import the art package

# Function Definitions


def typing_print(text: str, runtime: float = 0.05) -> None:
    """Credit does not go to Nolan, as he stole it off the internet...

    But it works!
    Oh, and I modified it to add typing and a few other oddities.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(runtime)
    print("")


def roll_dice(n: int) -> list[int]:
    """Roll a set of dice."""
    dice = []

    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


def roll_again(choices: str, dice_list: list[int]) -> list[int]:
    """Reroll based on a string of re-roll/hold choices."""
    typing_print("Rolling again...\a")
    time.sleep(3)
    for i, choice in enumerate(choices):
        if choice == "r":
            dice_list.pop(i)
            dice_list.insert(i, random.randint(1, 6))
    return dice_list


def computer_strategy(dice_list: list[Any]) -> str:
    """Computer strategy - picks re-roll for computer.

    Stratgy #2
    """
    typing_print("Computer is thinking...")
    time.sleep(3)
    choices: str = ""
    for i, n in enumerate(dice_list):
        if n < 5:
            choices = choices + "r"
        else:
            choices = choices + "-"
    return choices


def find_winner(comp_dice_list: list[int], user_dice_list: list[int]):
    user_total = sum(user_dice_list)
    computer_total = sum(comp_dice_list)
    typing_print(f"The computer total is: {computer_total}")
    typing_print(f"The user total is: {user_total}")
    if user_total > computer_total:
        finish = art.text2art("You win!", font="random-large")  # define art
        typing_print(finish, 0.005)  # draw the art
    elif user_total < computer_total:
        finish = art.text2art("Sorry.", font="random-medium")  # define art

        typing_print(finish, 0.005)  # draw the art
    elif user_total == computer_total:
        finish = art.text2art("Sorry.", font="random-small")  # define art
        typing_print(finish, 0.005)  # draw the art


# def is_choice(choices):
#     search = re.compile(
#         r"[^(-|r|R)$]"
#     ).search  # TODO: fix this regex to determine if 'r' or '-' is found
#     return not bool(
#         search(choices)
#     )  # TODO: Verfiy this checks if the string matches the regex and return a BOOL.


# # Ignore this
# # TODO: Remove
# bad = is_choice("17")
# good = is_choice("--r-rr")
# print("REGEX TEST:")
# print(f"expect False: {bad}")
# print(f"expect True: {good}")

# MAIN PROGRAM
# Step 1 - start the game
# Add art
title = art.text2art("Dice Game!", font="random-xlarge")  # define art
# print(title)  # print the art
typing_print(title, 0.005)  # draw the art
number_dice = input("Enter number of dice:\n")
while not str.isdigit(number_dice):
    number_dice = input("That was not a number, unworthy one:\n")

number_dice = int(number_dice)

input("Ready to start? Hit enter to continue.")

# Step 2 - roll the dice
user_rolls = roll_dice(number_dice)
typing_print("Your turn!")
typing_print(f"User's first roll: {user_rolls}\nThe user's total is: {sum(user_rolls)}")
typing_print("Computer's turn:")
computer_rolls = roll_dice(number_dice)
typing_print(
    f"Computer's first roll: {computer_rolls}\nThe computer's total is: {sum(computer_rolls)}"
)

# Step 3 - get user choices
user_choices = input("'-' to hold, or 'r' to re-roll.")

while (len(user_choices) != number_dice) and (True):
    typing_print(
        f"You must enter {number_dice} choices, and they must only be 'r' or '-'."
    )
    user_choices = input("Input your choice again, foolish mortal.")

# Step 4 - roll again based on user choices
user_rolls = roll_again(user_choices, user_rolls)
typing_print(f"Player's new roll is: {user_rolls}")
# Step 5 - computer decision, computer rolls agian
computer_choices = computer_strategy(computer_rolls)
typing_print(f"The computer's choices are: {computer_choices}")
computer_rolls = roll_again(computer_choices, computer_rolls)
typing_print(f"The computer's new rolls are: {computer_rolls}")

# Step 6 - decide winner
find_winner(computer_rolls, user_rolls)
