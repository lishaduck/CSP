"""Program: buggy_image.py - make a spider.
"""


import turtle as trtl


# this section of code makes the spider's body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)


# initializes variables
LEGS = 4
LEGS_PER_SIDE = 4
LEG_LENGTH = 70
DIRECTION = 360 / 10
spider.pensize(5)


# this loop makes the legs, set the direction, and moves forward
for i in range(2):
    count = 0
    while count < LEGS:
        spider.goto(0, 20)
        if i == 1:
            spider.setheading(DIRECTION * count + 45)
        else:
            spider.setheading(DIRECTION * count - 135)
        spider.forward(LEG_LENGTH)
        count = count + 1


spider.penup()
spider.goto(20, 20)
spider.setheading(180)

for i in range(2):
    spider.fillcolor("White")
    spider.begin_fill()
    spider.circle(10)
    spider.end_fill()
    spider.begin_fill()
    spider.right(135)
    spider.forward(8)


# shows the finished product and hides the turtle
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
