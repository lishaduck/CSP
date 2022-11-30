"""A program creates a window on your screen using Tkinter."""


from tkinter import *  # pylint: disable=unused-wildcard-import, wildcard-import

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


frame_login.tkraise()
root.mainloop()
