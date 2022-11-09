import turtle as trtl

firework = trtl.Turtle()
firework.speed(0)

for i in range(36):
    for i in range(5):
        firework.left(144)
        firework.forward(200)
    firework.right(10)

firework.hideturtle()

wn = trtl.Screen()
wn.mainloop()
