"""A program creates a window on your screen using Tkinter."""


from tkinter import *

username = ""
password = ""


# main window
root = Tk()
root.title("Authorization")
root.wm_geometry("400x200")

# create empty frame
frame_login = Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = Label(frame_login, text="Username:", font="Courier")
lbl_username.pack()
ent_username = Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = Label(frame_login, text="Password:", font="Courier")
lbl_password.pack()
ent_password = Entry(frame_login, bd=3, show="*")
ent_password.pack(pady=5)


def test_my_button():
    global username
    global password
    username = ent_username.get()
    password = ent_password.get()
    frame_auth.tkraise()


def hello_there_foolish_mortal():
    print(
        "Hello there,",
        username + "!",
        "I know your password. Hahaha! Oh yeah, it's",
        password + "! :)",
    )
    user_label.config(
        text=("Hello, silly foolish one, you who is wonder, " + username + ".")
    )
    user_label.pack()


btn_login = Button(frame_login, text="Login", font="Courier", command=test_my_button)
btn_login.pack(pady=5)


frame_auth = Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")


user_label = Label(
    frame_auth,
    font="Courier",
    fg="yellow",
    bg="black",
)


btn_color = Button(
    frame_auth, text="Click Me, Child.", command=hello_there_foolish_mortal
)
btn_color.pack(pady=5)


frame_login.tkraise()
root.mainloop()
