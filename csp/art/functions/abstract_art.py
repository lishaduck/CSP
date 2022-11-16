"""Program: abstract_art.py - Make abstract art with turtles.

"Use random colors, randomly sized circles, and randomly sized squares
to create abstract art that is different each time you run the program."
"""


import random
import turtle as trtl
from time import sleep

from csp.utilities import COLORS

# Credit where credit is due: https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/


# init turtle, and config
painter = trtl.Turtle()
painter.speed(0)
wn = trtl.Screen()


# See /art/turtles/a_row_of_colored_squares.py for original code.
def square(s):
    """Make a square."""
    for i in range(4):
        painter.forward(s)
        painter.left(90)


def generate_fill_color():
    """Generate a color, change pencolor, and begin fill."""
    painter.begin_fill()
    painter.fillcolor(random.choice(COLORS))
    painter.width(random.randint(1, 30))
    painter.pencolor(random.choice(COLORS))


def forward():
    """Move the turtle forward, and set the heading."""
    painter.forward(random.randint(20, 100))
    painter.setheading(random.randint(0, 360))


def draw():
    """Do the drawing."""
    forward()
    generate_fill_color()
    square(random.randint(10, 50))
    painter.end_fill()
    forward()
    generate_fill_color()
    painter.circle(random.randint(5, 30))
    painter.end_fill()

    if painter.xcor() > wn.window_width() / 2:
        painter.goto(0, 0)
        print("Summoned (Too far right x).  ", end="\r")
        sleep(3)

    if painter.xcor() < -(wn.window_width() / 2):
        painter.goto(0, 0)
        print("Summoned (Too far left x).  ", end="\r")
        sleep(3)

    if painter.ycor() > wn.window_height() / 2:
        painter.goto(0, 0)
        print("Summoned (Too far top y).   ", end="\r")
        sleep(3)

    if painter.ycor() < -(wn.window_height() / 2):
        painter.goto(0, 0)
        print("Summoned (Too far bottom y).", end="\r")
        sleep(3)


iterations = input("Iterations (Int, or 'Infinity'): ")
if iterations == "Infinity":
    RUNNING = True
    i = 0
    while RUNNING:
        draw()
        print(str(i) + "                           ", end="\r")
        i = i + 1

elif str.isdigit(iterations):
    for i in range(int(iterations)):
        draw()
        print(str(i) + "                           ", end="\r")
        i = i + 1
else:
    print("That wasn't an option ... so you're going to have a 100 iteration loop.")
    for i in range(100):
        draw()
        print(str(i) + "                           ", end="\r")
        i = i + 1

wn.mainloop()
