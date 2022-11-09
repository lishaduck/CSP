import turtle as trtl


def compainer(reason):

    paint = trtl.Turtle()

    paint.color("purple")
    style = ("Arial", 75, "italic")
    paint.write(reason, font=style, align="center")
    paint.hideturtle()

    wn = trtl.Screen()
    wn.mainloop()


current_compaint = """ "Please Let me Leave!" - Hayden """

compainer(current_compaint)
