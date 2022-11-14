"""Program catch_a_turtle.py - It's a game with a persistant state leaderboard.

Catch a turtle
[Victor and Eli - 11.8-11]
"""


# -----import statements-----
import os
import random as rand
import turtle as trtl
from pathlib import Path

import leaderboard as lb

# -------entrypoint--------
if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        print("Let's play!")
    else:
        print(__doc__)


p = Path(os.path.realpath(__file__)).parent
LEADERBOARD_FILE_NAME = Path.resolve(p / "leaderboard.csv")
print(LEADERBOARD_FILE_NAME)
player_name = input("What shall the leaderboard remember you as, should you win? ")


# --set the screen and turtle--
wn = trtl.Screen()
wn.bgcolor("black")
spot = trtl.Turtle()
spot.speed(10)
score = 0


# -----countdown variables-----
FONT_SETUP = ("Arial", 20, "normal")
timer = 30
COUNTER_INTERVAL = 1000  # 1000 represents 1 second
timer_up = False


# -----countdown writer-----
counter = trtl.Turtle()
counter.hideturtle()
counter.pencolor("white")
counter.penup()
counter.goto(-50, 250)


# -----game functions-----
def countdown() -> None:
    """Create the timer and score."""
    global timer
    global timer_up
    counter.clear()
    if timer > 0:
        counter.write(f"Timer: {timer}  Score: {score}", font=FONT_SETUP)
        timer -= 1
        counter.getscreen().ontimer(countdown, COUNTER_INTERVAL)
    else:
        counter.write(f"Time's Up!      Score: {score}", font=FONT_SETUP)
        timer_up = True
        print(f"Your score was: {score}!")
        manage_leaderboard()
        spot.hideturtle()


def spot_clicked(x: float, y: float):
    """Event handler for the spot.

    :param x: current x of the spot
    :param y: current y of the spot
    """
    if timer > 0:
        global score
        score += 1
        print(score, end="\r")
        change_position(x, y)


def change_position(x: float, y: float) -> None:
    """Move the spot (called when spot_clicked).

    :param x: current x of the spot
    :param y: current y of the spot
    """
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    while new_xpos == x:
        new_xpos = rand.randint(-200, 200)
    while new_ypos == y:
        new_ypos = rand.randint(-200, 200)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()


# Game Code
SPOT_COLOR = "light green"
spot_size = rand.randint(3, 5)
SPOT_SHAPE = "turtle"
spot.shape(SPOT_SHAPE)
spot.shapesize(spot_size)
spot.fillcolor(SPOT_COLOR)
spot.goto(-100, 0)


# manages the leaderboard for top 5 scorers
def manage_leaderboard() -> None:
    """Interface the leaderboard.py module."""
    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(LEADERBOARD_FILE_NAME)
    leader_scores_list = lb.get_scores(LEADERBOARD_FILE_NAME)

    # show the leaderboard with or without the current player
    if len(leader_scores_list) < 5 or score >= leader_scores_list[4]:
        lb.update_leaderboard(
            LEADERBOARD_FILE_NAME,
            leader_names_list,
            leader_scores_list,
            player_name,
            score,
        )
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, counter, score)

    else:
        lb.draw_leaderboard(
            False, leader_names_list, leader_scores_list, counter, score
        )


# ---------events----------
spot.onclick(spot_clicked)
wn.ontimer(countdown, COUNTER_INTERVAL)
wn.mainloop()
