"""Program catch_a_turtle.py - Catch a turtle!

It's a game!
[Victor and Eli - 11.8-11]
"""


# -----import statements-----
import random as rand
import turtle as trtl

# --set the screen and turtle--
wn = trtl.Screen()
wn.bgcolor("black")
spot = trtl.Turtle()
spot.speed(10)
score = 0


# -----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
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
    """Function: countdown() - timer.

    No args.
    """
    global timer
    global timer_up
    counter.clear()
    if timer <= 0:
        counter.write(f"Time's Up!    Score: {score}", font=font_setup)
        timer_up = True
        spot.hideturtle()
    else:
        counter.write(f"Timer: {timer}  Score: {score}", font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


def spot_clicked(x: float, y: float):
    if timer > 0:
        global score
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


# ---------events----------
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        start_game()
    else:
        print(__doc__)
        start_game()
