"""Program: guessing_game.py - guess what is is.
"""


import random


def guess_num():
    """This is the number game.

    No Args
    """
    num = random.randint(0, 100)
    # print(num)
    guess = int(input("Choose number from 0 through 100: "))

    while guess != num:
        if guess < num:
            guess = int(input("Too low :( Try again: "))
        elif guess > num:
            guess = int(input("Too high :( Try again: "))
    print("You got it!")


def quiz_game():
    """This is the quiz game.

    No Args
    """
    score = 0
    questions = [
        "What is the capital of Peru?",
        "What is the longest river?",
        "Do goldfish have a three second memory?",
        "Did George Washington had wood teeth?",
        "Are there over 7,500 varieties of apple?",
    ]
    answers = ["lima", "amazon", "no", "no", "yes"]

    _: int
    for _ in range(len(questions)):
        num = random.randint(0, len(questions) - 1)
        question = questions.pop(num)
        correct_answer = answers.pop(num)
        print(question)
        answer = input("What is your answer? ")
        if answer == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect.")
            print("The correct answer was ...", correct_answer)
    print(score)


if __name__ == "__main__":
    playing = True
    while playing is True:
        print("Pick game: \n 1 for guess that number \n 2 for the quiz game")
        game = int(input("Selection: "))
        if game == 1:
            guess_num()
        elif game == 2:
            quiz_game()
        still_playing = input("Want to play again? Or change your game? Answer y/n: ")
        playing = bool(still_playing in ("y", "Y", "yes", "Yes"))
    print("Goodbye!")
