"""Program: leaderboard.py - The leaderboard module to be used in Activity 1.2.2."""


import csv
import turtle as trtl
from pathlib import Path

import art

# set the levels of scoring
MUD_SCORE = 5
BRONZE_SCORE = 20
SILVER_SCORE = 25
GOLD_SCORE = 40
PLATINUM_SCORE = 100


def get_names(file_name: Path) -> list[str]:
    """Return names in the leaderboard file.

    :param file_name: A file name, in the format of a path.
    :return: A list of integers representing the scores.
    """
    with file_name.open("rt", encoding="utf-8", newline="") as leaderboard_file:

        # use a for loop to iterate through the content of the file, one line at a time
        # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
        names: list[str] = []
        # print("Fetching names.")
        name_reader = csv.reader(leaderboard_file, dialect="excel")
        for line in name_reader:
            leader_name = line[0]
            # add the player name to the names list
            names.append(leader_name)
            # print(names)
    #  return the names list in place of the empty list
    return names


def get_scores(file_name: Path) -> list[int]:
    """Return scores from the leaderboard file.

    :param file_name: A file name, in the format of a path.
    :return: A list of integers representing the scores.
    """
    with file_name.open(
        "rt", encoding="utf-8"
    ) as leaderboard_file:  # be sure you have created this

        scores: list[int] = []
        # print("Fetching scores.")
        score_reader = csv.reader(leaderboard_file, dialect="excel")
        for line in score_reader:
            leader_score = int(line[1])
            # add the player score to the scores list
            scores.append(leader_score)
        # print(scores)
    # return the scores in place of the empty list
    return scores


def update_leaderboard(
    file_name: Path,
    leader_names: list[str],
    leader_scores: list[int],
    player_name: str,
    player_score: int,
) -> None:
    """Update leaderboard by inserting the current player and score to the list at the correct position."""
    index = 1
    # loop through all the scores in the existing leaderboard list
    for i in range(5):
        # check if this is the position to insert new score at
        if player_score > leader_scores[i]:
            leader_names.pop()
            leader_names.insert(index, player_name)
            leader_scores.pop()
            leader_scores.insert(index, player_score)
        else:
            index = index + 1

    # store the latest leaderboard back in the file
    with file_name.open(
        "wt",  # this mode opens the file and erases its contents for a fresh start
        encoding="utf-8",
        newline="",
    ) as leaderboard_file:

        leaderboard_writer = csv.writer(leaderboard_file, dialect="excel")
        # loop through all the leaderboard elements and write them to the the file
        for i, name in enumerate(leader_names):
            leaderboard_writer.writerow([name, str(leader_scores[i])])


def draw_leaderboard(
    high_scorer: bool,
    leader_names: list[str],
    leader_scores: list[int],
    turtle_object: trtl.Turtle,
    player_score: int,
) -> None:
    """Draw leaderboard and display a message to player."""
    # clear the screen and move turtle object to (-200, 100)
    # to start drawing the leaderboard
    font_setup = ("Comic Sans", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-200, 200)
    turtle_object.hideturtle()
    turtle_object.down()

    # draw the leaderboard title
    turtle_object.write(
        art.text2art("Time's up!", font="random-medium"),
        font=("Courier New", 20, "normal"),
    )

    # loop through the lists and use the same index to display the corresponding name
    # and score, separated by a tab space '\t'
    for index, name in enumerate(leader_names):
        turtle_object.write(
            str(index + 1) + "\t" + str(name) + "\t" + str(leader_scores[index]),
            font=font_setup,
        )
        turtle_object.penup()
        turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
        turtle_object.down()

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # display message about player making/not making leaderboard
    if high_scorer:
        if player_score > leader_scores[4]:
            turtle_object.write(
                "Congratulations!\nYou made the leaderboard!", font=font_setup
            )
        elif player_score <= leader_scores[4]:
            turtle_object.write("So close...", font=font_setup)
    else:
        turtle_object.write(
            "Sorry!\nYou didn't make the leaderboard.\nMaybe next time!",
            font=font_setup,
        )

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # Display a gold/silver/bronze message if player earned a gold/silver/bronze medal; display nothing if no medal
    if MUD_SCORE <= player_score < BRONZE_SCORE:
        turtle_object.write(
            "You earned a dried piece of mud! It doesn't even resemble a medal... It's just a circle of mud. Oh, and you got a ruble, don't spend it all in one place.",
            font=font_setup,
        )
    elif BRONZE_SCORE <= player_score < SILVER_SCORE:
        turtle_object.write("You earned a bronze medal!", font=font_setup)
    elif SILVER_SCORE <= player_score < GOLD_SCORE:
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif GOLD_SCORE <= player_score < PLATINUM_SCORE:
        turtle_object.write("You earned a gold medal!", font=font_setup)
    elif PLATINUM_SCORE <= player_score:
        turtle_object.write("Poggers?", font=font_setup)
    else:
        turtle_object.write(
            "Here's an Iranian Rial. You might as well spend it all in one place. Better Luck Next Time..."
        )

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()
    turtle_object.write(f"You caught the turtle {player_score} times.", font=font_setup)
