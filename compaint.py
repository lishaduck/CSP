"""
compaint.py

Command line usage:
$ python3 complaint
args:
   <[Message]>
returns - trtl.Screen (turtle graphic using a mainloop)
"""
import turtle as trtl


def compainer(reason):
    """
    reason: string - Reason you wan to complain. Makes up sign text.
    """

    paint = trtl.Turtle()

    paint.color("purple")
    style = ("Arial", 75, "italic")
    paint.write(reason, font=style, align="center")
    paint.hideturtle()

    wn_ = trtl.Screen()
    wn_.mainloop()


if __name__ == "__main__":
    CURRENT_COMPLAINT = input("[Message]")
    compainer(CURRENT_COMPLAINT)
