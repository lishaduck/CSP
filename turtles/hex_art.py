"""
Elisha Dukes [9.14]
"""
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)


colors = ["yellow", "blue", "orange", "green", "red", "red"]


for i in range(36):
    for i in range(6):
        painter.forward(100)
        painter.left(60)
        painter.color(colors[i])
    painter.right(10)
painter.penup()
painter.color("white")
for i in range(36):
    painter.penup()
    painter.forward(220)
    painter.pendown()
    painter.circle(5)
    painter.penup()
    painter.backward(220)
    painter.pendown()
    painter.right(10)


painter.hideturtle()

wn = trtl.Screen()
wn.bgcolor("black")
wn.mainloop()
