"""A program creates a window on your screen using Tkinter."""


import os
from pathlib import Path
from tkinter import *  # pylint: disable=unused-wildcard-import, wildcard-import

p = Path(os.path.realpath(__file__)).parent
username: str = ""
password: str = ""


# main window
root: Tk = Tk()
root.title("Authorization")
root.wm_geometry("400x200")

# create empty frame
frame_login: Frame = Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username: Label = Label(frame_login, text="Username:", font="Courier")
lbl_username.pack()
ent_username: Entry = Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password: Label = Label(frame_login, text="Password:", font="Courier")
lbl_password.pack()
ent_password: Entry = Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)


def _test_my_button() -> None:
    """Set the username and password, then raise the frame_auth frame."""
    global username  # pylint: disable=global-statement
    global password  # pylint: disable=global-statement
    username = ent_username.get()
    password = ent_password.get()
    frame_auth.tkraise()


def _hello_there_foolish_mortal() -> None:
    """Print the username and password to the console.

    Then, update and pack the user_label.
    """
    print(
        "Hello there,",
        username + "!",
        "I know your password. Hahaha! Oh yeah, it's",
        password + "! :)",
    )
    user_label.config(
        text=("Hello, silly foolish one, you who got in, " + username + ".")
    )
    user_label.pack()


btn_login: Button = Button(
    frame_login, text="Login", font="Courier", command=_test_my_button
)
btn_login.pack(pady=5)


frame_auth: Frame = Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")


user_label: Label = Label(
    frame_auth,
    font="Courier",
    fg="yellow",
    bg="black",
)


btn_color: Button = Button(
    frame_auth, text="Click Me, Child.", command=_hello_there_foolish_mortal
)
btn_color.pack(pady=5)


# Day 2 work starts here


canvas: Canvas = Canvas(frame_auth, width=400, height=400)
canvas.pack()


STRAWBERRY_LEMONADE_FILE_NAME = Path.resolve(p / "strawberry-lemonade.png")


# create an image using a gif file
img2 = PhotoImage(file=STRAWBERRY_LEMONADE_FILE_NAME)
# use image to create a canvas image
myphoto = canvas.create_image(150, 150, image=img2)


# create a circle
circle = canvas.create_oval(100, 200, 130, 230, fill="red")
# create a rectangle
blue_rectangle = canvas.create_rectangle(50, 50, 70, 80, fill="blue")
# create text
screen_message = canvas.create_text(
    300, 300, text="Welcome!", font=("Helvetica", 30), fill="black"
)


# create an image using a gif file
GREEN_CHAR_FILE_NAME = Path.resolve(p / "greenChar.gif")
img = PhotoImage(file=GREEN_CHAR_FILE_NAME)
# use image to create a canvas image
mychar = canvas.create_image(-100, -100, image=img)


# This function is called when the arrow key is pressed
def move(event: Event) -> object:
    key = event.keysym
    if key == "Right":
        canvas.move(circle, 10, 0)  # change x positive
    elif key == "Left":
        canvas.move(circle, -10, 0)  # change x negative
    if key == "Up":
        canvas.move(blue_rectangle, 0, 10)  # change y positive
    elif key == "Down":
        canvas.move(blue_rectangle, 0, -10)  # change y negative


def move_character(event: Event) -> object:
    canvas.coords(mychar, event.x, event.y)


# bind the function to the mouse click
canvas.bind_all("<Button-1>", move_character)


# bind keyboard input to move_circle
canvas.bind_all("<Key>", move)


# Figure out how to make a triangle (or any POLYGON) on the canvas
triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill="red")

# end Day 2 work


frame_login.tkraise()
root.mainloop()
