"""Program: buggy_image.py - make a spider.
"""


import turtle as trtl


# this section of code makes the spider's body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)


# initializes variables
LEGS = 6
LEG_LENGTH = 70
DIRECTION = 380 / LEGS
spider.pensize(5)


# this loop makes the legs, set the direction, and moves forward
count = 0
while count < LEGS:
    spider.goto(0, 0)
    spider.setheading(DIRECTION * count)
    spider.forward(LEG_LENGTH)
    count = count + 1


# shows the finished product and hides the turtle
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
