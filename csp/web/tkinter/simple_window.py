"""A program creates a window on your screen using Tkinter."""


import tkinter as tk

password = ""


def test_my_button():
    global password
    frame_auth.tkraise()
    password = ent_username.get()


# main window
root = tk.Tk()
root.title("Authorization")
root.wm_geometry("400x200")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text="Username:", font="Courier")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_username = tk.Label(frame_login, text="Password:", font="Courier")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3, show="*")
ent_username.pack(pady=5)

btn_login = tk.Button(frame_login, text="Login", font="Courier", command=test_my_button)
btn_login.pack(pady=5)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

user_label = tk.Label(frame_auth, text=password, font="Courier")
user_label.pack()


# TODO: Configure the label in frame_auth to display the password

frame_login.tkraise()
root.mainloop()
