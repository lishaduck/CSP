"""Program catch_a_turtle.py - Its a game with a persistant state leaderboard.

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
LEADERBOARD_FILE_NAME = Path.resolve(p / "leaderboard.txt")
print(LEADERBOARD_FILE_NAME)
player_name = input("What shall the leaderboard remember you as, should you win? ")


# --set the screen and turtle--
wn = trtl.Screen()
wn.bgcolor("black")
spot = trtl.Turtle()
spot.speed(10)
score = 0


# -----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5  # TODO: switch back to 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False


# -----countdown writer-----
counter = trtl.Turtle()
counter.hideturtle()
counter.pencolor("white")
counter.penup()
counter.goto(-50, 250)


# -----game functions-----
def countdown():
    """Create the timer and score."""
    global timer
    global timer_up
    counter.clear()
    if timer <= 0:
        counter.write(f"Time's Up!      Score: {score}", font=font_setup)
        timer_up = True
        manage_leaderboard()
        spot.hideturtle()
    else:
        counter.write(f"Timer: {timer}  Score: {score}", font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


def spot_clicked(x: float, y: float):
    if timer > 0:
        update_score()
        change_position()


def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()


def update_score():
    global score
    score = score + 1
    print(score)


# Game Code
SPOT_COLOR = "light green"
spot_size = rand.randint(3, 5)
SPOT_SHAPE = "turtle"
spot.shape(SPOT_SHAPE)
spot.shapesize(spot_size)
spot.fillcolor(SPOT_COLOR)
spot.goto(-100, 0)


# manages the leaderboard for top 5 scorers
def manage_leaderboard():

    global score
    global spot

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
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)


# ---------events----------
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()
