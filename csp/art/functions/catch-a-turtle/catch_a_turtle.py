"""Program catch_a_turtle.py - Catch a turtle!

It's a game!
[Victor and Eli - 11.8-11]
"""


# -----import statements-----
import random as rand
import turtle as trtl

import leaderboard as lb

# --set the screen and turtle--
wn = trtl.Screen()
wn.bgcolor("black")
leaderboard_file_name = "leaderboard.txt"
player_name = input("What shall the leaderboard remember you as, should you win? ")
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
    """Function: countdown() - timer."""
    global timer
    global timer_up
    counter.clear()
    if timer <= 0:
        counter.write(f"Time's Up!    Score: {score}", font=font_setup)
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


def start_game():
    pass


# Game Code
spot_color = "light green"
spot_size = rand.randint(3, 5)
spot_shape = "turtle"
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.goto(-100, 0)


# manages the leaderboard for top 5 scorers
def manage_leaderboard():

    global score
    global spot

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    # show the leaderboard with or without the current player
    if len(leader_scores_list) < 5 or score >= leader_scores_list[4]:
        lb.update_leaderboard(
            leaderboard_file_name,
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

# -------entrypoint--------
if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        start_game()
    else:
        print(__doc__)
        start_game()
