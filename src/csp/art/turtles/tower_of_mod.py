"""
Program: tower_of_mod.py - Make a tower.

# Modify this code in VS Code to alternate the colors of the floors every three floors
"""

import turtle as trtl

painter = trtl.Turtle()
painter.speed(2)
painter.pensize(5)
painter.shape("turtle")

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    rem1 = floor % 6
    if rem1 == 0:
        painter.color("blue")
    elif rem1 == 2:
        painter.color("purple")
    elif rem1 == 4:
        painter.color("grey")
    y = y + 5  # location of next floor
    # draw the floor
    painter.pendown()
    painter.forward(50)

    rem2 = floor % 21
    if rem2 == 20:
        painter.penup()
        painter.goto((x + 150), (-150))
        y = -150
        x = x + 150

wn = trtl.Screen()
wn.mainloop()
