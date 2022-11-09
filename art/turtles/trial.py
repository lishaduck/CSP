"""
Program: trial.py - python input practice.

command-line usage
answer the prompts
"""


# import the datetime module to get the current date/year
import datetime as dt
from typing import Literal

# ask user for their name then welcome them
user_name: str = input("What is your name?")
print("Hello", user_name, "welcome to my program.")

# ask user for their age
age: int = int(input("How old are you?"))

# get the current year using the datetime object that resides in the datetime module
curr_year: int = dt.datetime.now().year

# prepare and display output
birth_year: int = curr_year - age
print("Hmmm... were you born in", birth_year, ".")

YOU: Literal[""] = ""


def figure(who) -> Literal[""]:
    """
    Figure func.

    args:
    who: string - pass in name
    """
    if who == "":
        return ""

    return ""
