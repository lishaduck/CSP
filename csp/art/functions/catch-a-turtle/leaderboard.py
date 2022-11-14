"""Program: leaderboard.py - The leaderboard module to be used in Activity 1.2.2."""


import csv
import turtle as trtl
from pathlib import Path

Rank = trtl.Turtle()
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
    with file_name.open("r", encoding="utf-8", newline="") as leaderboard_file:

        # use a for loop to iterate through the content of the file, one line at a time
        # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
        names: list[str] = []
        print("Getting names")
        name_reader = csv.reader(leaderboard_file, dialect="excel")
        for line in name_reader:
            leader_name = ""
            index = 0

            # use a while loop to read the leader name from the line (format is "leader_name,leader_score")
            # TODO: fix IndexError
            # File "/Users/dukese01/CSP/csp/art/functions/catch-a-turtle/leaderboard.py", line 35, in get_names
            #   while line[index] != ",":
            # IndexError: list index out of range
            while line[index] != ",":
                leader_name = leader_name + line[index]
                index = index + 1
            print(leader_name)
            # add the player name to the names list
            names.append(leader_name)
        leaderboard_file.close()
    print(names)
    #  return the names list in place of the empty list
    return names


def get_scores(file_name: Path) -> list[int]:
    """Return scores from the leaderboard file.

    :param file_name: A file name, in the format of a path.
    :return: A list of integers representing the scores.
    """
    with file_name.open(
        "r", encoding="utf-8"
    ) as leaderboard_file:  # be sure you have created this

        scores: list[int] = []
        print("Getting scores.")
        score_reader = csv.reader(leaderboard_file, dialect="excel")
        for line in score_reader:
            leader_score = ""
            index = 0

            # use a while loop to index beyond the comma, skipping the player's name
            while line[index] != ",":
                index = index + 1
            # use a while loop to get the score
            while line[index] != "\n":
                leader_score = leader_score + line[index]
                index = index + 1
            leader_score = leader_score.replace(
                ",", ""
            )  # Source: https://www.delftstack.com/howto/python/remove-commas-from-string-in-python/

            # add the player score to the scores list
            leader = int(leader_score)
            scores.append(leader)
        print(scores)
        leaderboard_file.close()
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

    # TODO 12: store the latest leaderboard back in the file
    with file_name.open(
        "w",  # this mode opens the file and erases its contents for a fresh start
        encoding="utf-8",
        newline="",
    ) as leaderboard_file:

        leaderboard_writer = csv.writer(leaderboard_file, dialect="excel")
        # TODO 13 loop through all the leaderboard elements and write them to the the file
        for i in leaderboard_file:
            leaderboard_writer.writerow(
                leader_names[index] + "," + str(leader_scores[index])
            )
        leaderboard_file.close()


def draw_leaderboard(
    high_scorer: bool,
    leader_names: list[str],
    leader_scores: list[int],
    turtle_object: trtl.Turtle,
    player_score: int,
) -> None:  # noqa: D300, D301
    """Draw leaderboard and display a message to player.

    @LeParco1's version:
    # def leaderboard():
    #     \"\"\"Leaderboard\"\"\"
    #     leaderboard = trtl.Turtle()
    #     leaderboard.hideturtle()
    #     leaderboard.write(f"Player Name:     Score:\n{name}     {score}")
    """
    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()

    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    for index, name in enumerate(leader_names):
        turtle_object.write(
            str(index + 1) + "\t" + name + "\t" + str(name),
            font=font_setup,
        )
        turtle_object.penup()
        turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
        turtle_object.down()

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # TODO 14: display message about player making/not making leaderboard
    if high_scorer:
        if player_score > leader_scores[5]:
            turtle_object.write(
                "Congratulations!\nYou made the leaderboard!", font=font_setup
            )
        elif player_score <= leader_scores[5]:
            turtle_object.write("So close...")
    else:
        turtle_object.write(
            "Sorry!\nYou didn't make the leaderboard.\nMaybe next time!",
            font=font_setup,
        )

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor()) - 50)
    turtle_object.pendown()

    # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
    turtle_object.write(f"You caught the turtle {player_score} times.")
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
        turtle_object.write("Poggers", font=font_setup)
    else:
        turtle_object.write(
            "Here's an Iranian Rial. You might as well spend it all in one place. Better Luck Next Time..."
        )
