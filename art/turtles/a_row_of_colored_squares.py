import turtle as trtl

painter = trtl.Turtle()

colors = ["red", "green", "blue", "orange", "purple", "yellow"]

for i in range(6):
    painter.pencolor(colors[i])
    for i in range(4):
        painter.forward(20)
        painter.left(90)
    painter.penup()
    painter.forward(30)
    painter.pendown()

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
