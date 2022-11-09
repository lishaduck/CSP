"""Program: traversing_turtles.py - Add code to make turtles move in a circle and change colors.
"""
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.pencolor(turtle_colors[-1])
    t.fillcolor(turtle_colors[-1])
    turtle_colors.pop()
    my_turtles.append(t)

# starts at 0,0
startx = 0
starty = 0
direction = 0

# loiops through all the turtles in the list of turtles
for t in my_turtles:
    t.penup()
    t.setheading(direction)
    t.goto(startx, starty)
    t.right(45)
    t.forward(50)
    t.pendown()
    # new x,y
    startx = t.xcor()
    starty = t.ycor()
    direction = t.heading()
wn = trtl.Screen()
wn.mainloop()
