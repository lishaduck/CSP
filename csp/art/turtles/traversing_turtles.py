"""Program: traversing_turtles.py - Add code to make turtles move in a circle and change colors."""


import turtle as trtl

from csp.utilities import TURTLE_SHAPES

# create an empty list of turtles
my_turtles = []


# use interesting shapes and colors

turtle_colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "gold",
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "gold",
]


s: str
for s in TURTLE_SHAPES:
    t = trtl.Turtle(shape=s)
    t.pencolor(turtle_colors[-1])
    t.fillcolor(turtle_colors[-1])
    turtle_colors.pop()
    my_turtles.append(t)


# starts at 0,0
startx = 0
starty = 0


# direction of the turtle
direction = 0
spin = 50


# loops through all the turtles in the list of turtles
t: trtl.Turtle
for t in my_turtles:
    t.penup()

    # set the direction via heading
    t.setheading(direction)
    t.goto(startx, starty)
    t.right(45)
    t.forward(spin)
    t.pendown()

    # new x,y
    startx = t.xcor()
    starty = t.ycor()

    # set direction so the next turtle will go a different way
    direction = t.heading()
    spin = spin + 7


wn = trtl.Screen()
wn.mainloop()
