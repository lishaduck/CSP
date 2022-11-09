"""Program: circle_of_circles.py - Make a circle out of smaller circles.
"""


import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)


colors = ["red", "green", "blue", "orange", "purple", "yellow"]


for i in range(36):
    painter.penup()
    painter.forward(200)
    for i in range(6):
        painter.pendown()
        painter.circle(5)
        painter.penup()
        painter.back(20)
    painter.goto(0, 0)
    painter.right(10)
    painter.pendown()

painter.hideturtle()


wn = trtl.Screen()
wn.mainloop()
