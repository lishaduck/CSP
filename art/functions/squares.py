import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

# define once how to make a square
def square():
    for i in range(4):
        painter.forward(100)
        painter.right(90)


def new_square(size):
    for i in range(size):
        painter.forward(size)
        painter.right(90)


# call the function when it's needed
square()
painter.forward(120)
new_square(50)

wn = trtl.Screen()
wn.mainloop()
