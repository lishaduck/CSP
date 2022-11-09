"""Program: shield.py - make a shield shape.
"""

import turtle as trtl

painter = trtl.Turtle()
painter.shape("turtle")
painter.speed(0)

painter.penup()
painter.goto(-200, 200)

painter.pendown()
painter.forward(400)
painter.right(90)
painter.forward(400)
painter.penup()
painter.goto(-200, -200)
painter.pendown()
painter.circle(200, 180)
painter.penup()
painter.goto(-200, -200)
painter.pendown()
painter.setheading(90)
painter.forward(400)


wn = trtl.Screen()
wn.mainloop()
