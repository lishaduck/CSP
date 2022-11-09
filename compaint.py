"""
compaint.py

Command line usage:
$ python3 complaint
args:
   <IS_CUSTOMIZED>
    <font>
    <size>
    <style>
   <Message>
returns - trtl.Screen (turtle graphic using a mainloop)
"""
import turtle as trtl


def compainer(
    reason, paint_color="purple", text_font="Arial", text_size=75, text_styling="italic"
):
    """
    Args:

    reason: string - Reason you want to complain. Makes up sign text.
    paint_color: string
    text_font: string
    text_size: int
    text_styling: string
    """

    paint = trtl.Turtle()

    paint.color(paint_color)
    text_style = (text_font, text_size, text_styling)
    paint.write(reason, font=text_style, align="center")
    paint.hideturtle()

    wn_ = trtl.Screen()
    wn_.mainloop()


if __name__ == "__main__":
    IS_CUSTOMIZED = input("Customize format options - Y/n: ")
    if IS_CUSTOMIZED in ("Y", "y"):
        font = input("font: ")
        size = int(input("Text Size (Int, not Float/Real): "))
        style = input("styling - bold, italic, or none (empty string): ")

        CURRENT_COMPLAINT = input("Message: ")
        compainer(CURRENT_COMPLAINT, text_font=font, text_size=size, text_styling=style)
    else:
        CURRENT_COMPLAINT = input("Message: ")
        compainer(CURRENT_COMPLAINT)
