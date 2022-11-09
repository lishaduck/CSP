"""
don't pass anything into this
it broke with the addtion of colors
TODO: RGB
"""

import turtle

painter = turtle.Turtle()
painter.speed(0)

R = 1
G = 1
B = 1

for i in range(103):
    painter.circle(150)
    painter.right(7)
    painter.forward(5)
    painter.pencolor((R, G, B))
    R = R + 1
    G = G + 1
    B = B + 1

wn = turtle.Screen()
wn.mainloop()
