"""Program: project.py - make a custom pumpkin.
"""
import turtle as trtl

# init
painter = trtl.Turtle()
painter.shape("turtle")
painter.speed(0)

# pick color
color = input("What color? ")

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

# Teeth
painter.penup()
painter.goto(100, -25)

for _ in range(6):
    painter.setheading(270)
    painter.begin_fill()
    painter.color("white")
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
    painter.color("white")
    painter.forward(30)
    painter.right(90)
    painter.forward(20)
    painter.right(90)
    painter.forward(30)
    painter.left(90)
    painter.forward(20)
    painter.end_fill()

# Persist Screen
wn = trtl.Screen()
wn.mainloop()
