"""Program: ladybug_code.py - Make a ladybug.
"""


import turtle as trtl


# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)


# initializes variables
LEGS = 6
LEGS_PER_SIDE = 3
LEG_LENGTH = 60
DIRECTION = 360 / 8
ladybug.penup()
ladybug.pensize(5)
ladybug.color("black")
ladybug.goto(0, -55)
ladybug.pendown()

count = 0
# this loop makes the legs, set the direction, and moves forward
while count < LEGS:
    for i in range(LEGS_PER_SIDE):
        ladybug.goto(0, -45)
        if count <= 2:
            ladybug.setheading(DIRECTION * count + 145)
        else:
            ladybug.setheading(DIRECTION * count + 165)
        ladybug.forward(LEG_LENGTH)
        count = count + 1

ladybug.setheading(0)


# and body
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)


# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)


# draw two sets of dots
while num_dots <= 2:
    ladybug.penup()
    ladybug.goto(xpos, ypos)
    ladybug.pendown()
    ladybug.circle(3)
    ladybug.penup()
    ladybug.goto(xpos + 30, ypos + 20)
    ladybug.pendown()
    ladybug.circle(2)

    # position next dots
    ypos = ypos + 25
    xpos = xpos + 5
    num_dots = num_dots + 1

ladybug.hideturtle()


wn = trtl.Screen()
wn.mainloop()
