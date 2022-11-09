"""Program catch_a_turtle.py - Catch a turtle!

It's a game!
[Victor and Eli - 11.8-11]
"""


# -----import statements-----
import random as rand
import turtle as trtl

# --set the screen and turtle--

wn = trtl.Screen()
spot = trtl.Turtle()

# -----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False
score = 0


# -----countdown writer-----
counter = trtl.Turtle()

# -----game functions-----
def countdown():
    """Function: countdown() -"""
    global timer
    global timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


def spot_clicked(x: float, y: float):
    # print("The spot was clicked!")
    change_position()


def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()


def start_game():
    pass


# Game Code
spot_color = "pink"
spot_size = 5
spot_shape = "circle"
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)


# Timer code
counter.hideturtle()
counter.write(f"Time: {timer}")

# ---------events---------
wn.ontimer(countdown, counter_interval)
spot.onclick(spot_clicked)
wn.mainloop()

if __name__ == "__main__":
    import sys

    if sys.argv[1:]:
        start_game()
    else:
        print(__doc__)
        start_game()
