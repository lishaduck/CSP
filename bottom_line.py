"""For health.
"""

living = True
right_amount = 3.2


def death_by_overdose():
    print("You died!")
    is_living = False
    return is_living


def death_by_lacking():
    print("You died!")
    is_living = False
    return is_living


def live():
    print("Good for you!")
    is_living = True
    return is_living


while living:
    amount = float(input("How much water do you have daily? (Liters): "))

    if amount > 10:
        living = death_by_overdose()

    if amount < 10:
        living = death_by_lacking()

    if amount == 10:
        living = live()
