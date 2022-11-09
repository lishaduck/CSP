"""Program: project.py - make a custom pumpkin.
"""


import turtle as trtl


# init
painter = trtl.Turtle()
painter.shape("classic")
painter.speed(0)

# pick color
color = input("What color? (Must be vaild colorstring): ")

# config colors
painter.color(color)
painter.fillcolor(color)
painter.pencolor(color)

# prep
painter.penup()
painter.goto(0, 200)
painter.setheading(180)


# Pumpkin
painter.begin_fill()
painter.pendown()
painter.circle(200, 350)
painter.end_fill()

# Stem
painter.fillcolor("brown")
painter.begin_fill()
painter.right(90)
painter.pendown()
painter.forward(50)
painter.right(90)
painter.forward(20)
painter.right(90)
painter.forward(50)
painter.end_fill()


# Nose
NOSE_SIZE = int(input("Nose size (15-35): "))
painter.goto(0, 20)
painter.pendown()
painter.setheading(270)
painter.color("white")
painter.forward(NOSE_SIZE)
painter.circle(NOSE_SIZE / 2, 180)
painter.penup()


# Teeth
painter.penup()
painter.goto(100, -25)

for _ in range(6):
    painter.setheading(270)
    painter.begin_fill()
    painter.forward(30)
    painter.right(90)
    painter.forward(20)
    painter.right(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(20)
    painter.end_fill()

painter.left(90)
painter.forward(50)
painter.left(90)

for _ in range(6):
    painter.setheading(90)
    painter.begin_fill()
    painter.forward(30)
    painter.right(90)
    painter.forward(20)
    painter.right(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(20)
    painter.end_fill()


# Eyes
EYE_SHAPE = input("Eye shape (must be valid turtleshape): ")
EYE_SIZE = float(input("Eye size (0.5-2): "))
Y_COR = int(input("Eye y-loc (50-100): "))
if EYE_SIZE > 1:
    X_COR = 50
else:
    X_COR = 30
painter.shape(EYE_SHAPE)
painter.turtlesize(EYE_SIZE, EYE_SIZE, EYE_SIZE)

painter.goto(X_COR, Y_COR)
painter.stamp()
painter.goto(-X_COR, Y_COR)
painter.stamp()

# Persist Screen
wn = trtl.Screen()
wn.mainloop()
