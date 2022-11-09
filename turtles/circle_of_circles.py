import turtle as trtl

painter = trtl.Turtle()

colors = ["red", "green", "blue", "orange", "purple", "yellow"]

painter.speed(0)

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
