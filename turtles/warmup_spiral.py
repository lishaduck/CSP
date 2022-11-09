"""
don't pass anything into this
it broke with the addtion of colors
TODO: RGB
"""

import turtle

painter = turtle.Turtle()
painter.speed(0)

r = 1
g = 1
b = 1

for i in range(103):
    painter.circle(150)
    painter.right(7)
    painter.forward(5)
    painter.pencolor((r, g, b))
    r = r + 1
    g = g + 1
    b = b + 1

wn = turtle.Screen()
wn.mainloop()
