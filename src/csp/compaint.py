"""
Program: compaint.py - This program creates a custom message using turtle graphics.

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
    reason: str,
    paint_color: str = "purple",
    text_font: str = "Arial",
    text_size: int = 75,
    text_styling: str = "italic",
):
    """Complain.

    :param reason: Reason you want to complain. Makes up sign text.
    :param paint_color: Color of the text.
    :param text_font: Font of the text.
    :param text_size: Size of the text.
    :param text_styling: Styling of the text. Can be either empty, or bold, or underline.
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
        color = input("color: ")
        font = input("font: ")
        size = int(input("Text Size (Int, not Float/Real): "))
        style = input("styling - bold, italic, or none (empty string): ")

        CURRENT_COMPLAINT = input("Message: ")
        compainer(
            CURRENT_COMPLAINT,
            paint_color=color,
            text_font=font,
            text_size=size,
            text_styling=style,
        )
    else:
        CURRENT_COMPLAINT = input("Message: ")
        compainer(CURRENT_COMPLAINT)
