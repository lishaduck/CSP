"""Program: guessing_game - guess what is is.
"""


import random


num = random.randint(0, 100)
print(num)
guess = int(input("Choose number from 0 through 100: "))


while guess != num:
    if guess < num:
        guess = int(input("Too low :( Try again: "))
    elif guess > num:
        guess = int(input("Too high :( Try again: "))
print("You got it!")
