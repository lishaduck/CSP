"""
"""
import turtle as trtl

painter = trtl.Turtle()
painter.speed(3)
painter.pensize(1)
painter.shape("turtle")
painter.penup()
painter.right(90)
painter.forward(100)
painter.left(90)
painter.pendown()

painter.fillcolor("green")
painter.begin_fill()
painter.circle(200)
painter.end_fill()

painter.penup()
painter.left(90)
painter.forward(125)
painter.left(90)
painter.forward(40)
painter.right(180)
painter.pendown()

painter.fillcolor("white")
painter.begin_fill()
painter.circle(50)
painter.end_fill()

painter.fillcolor("black")
painter.begin_fill()
painter.circle(20)
painter.end_fill()

painter.penup()
painter.forward(80)
painter.pendown()

painter.fillcolor("white")
painter.begin_fill()
painter.circle(50)
painter.end_fill()


painter.fillcolor("black")
painter.begin_fill()
painter.circle(20)
painter.end_fill()

painter.penup()
painter.right(90)
painter.forward(50)
painter.right(90)
painter.forward(80)
painter.right(180)
painter.pendown()


painter.fillcolor("white")
painter.begin_fill()
painter.setheading(270)
painter.circle(50, 180)
painter.end_fill()

wn = trtl.Screen()
wn.mainloop()
