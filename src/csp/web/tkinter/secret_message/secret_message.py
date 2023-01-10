"""Encrypt and Decrypt! Uses an object-oriented tkinter design.

Elisha Dukes [12.12]- Mrs. Carson
"""


import os
import tkinter as tk
from pathlib import Path
from tkinter import (  # Use object oriented design to build the dialog.
    Tk,
    messagebox,
    simpledialog,
    ttk,
)
from tkinter.ttk import Frame, Style

from PIL import Image, ImageTk

from csp.utilities import artistic_text


class SecretMessageGUI(Tk):
    """The secret message GUI."""

    def __init__(self):
        """Initialize the window."""
        super().__init__()

        self.title("Lock & Key")
        self.wm_geometry("200x300")
        style = Style()
        style.theme_use("aqua")


# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/
class MainFrame(Frame):
    """The main frame of the secret message GUI."""

    def __init__(self, container):
        """Initialize the frame."""
        super().__init__(container)
        self.display()
        self.config(cursor="question_arrow")
        # The swap_letters function has a really useful feature: if you run it on an encrypted message, it will decrypt it. So you can use this function to encrypt or decrypt messages depending on what the user wants to do. Update the while loop you created in Step 6.

        artistic_text("Lock & Key", font="random-small", speed=0.05)

    def message(self):
        """Do the tricky stuff."""
        self.loading.grid(column=1, row=3, **self.options)
        self.loading.start(20)
        # Call the get_task function and store its result in a variable called task.
        task = str(self.get_task())
        # If task equals 'encrypt', call the get_message() function and store it in a variable called message. Then create a message box that displays the message.
        if task in ("encrypt", "e"):
            message: str = str(self.get_message())
            # Under the if statement, after you call the get_message function, call the swap_letters function. Pass in the parameter message and store its return value in a variable encrypted.
            encrypted: str = self.swap_letters(message)
            # creating a message box
            # Update the message box code to show
            # “Ciphertext of the secret message is: ”, encrypted
            messagebox.showinfo("Ciphertext of the secret message is: ", encrypted)
        # Else if task equals 'decrypt', call the get_message() function and store it in a variable called message. Then create a message box that displays the message.
        elif task in ("decrypt", "d"):
            message: str = str(self.get_message())
            # Under the elif statement, after you call the get_message function, call the swap_letters function. Pass in the parameter message and store its return value in a variable decrypted.
            decrypted: str = self.swap_letters(message)
            if decrypted[-1] == "x":
                decrypted.rstrip("x")
            # creating a message box
            # Update the message box code to show
            # “Plaintext of the secret message is: ”, decrypted
            messagebox.showinfo("Plaintext of the secret message is: ", decrypted)
        else:
            messagebox.showwarning(
                title="Uh-oh",
                message=f'Oops! It looks like something went wrong.\nYou inputted "{task}"',
            )

        self.loading.grid_remove()
        self.loading.stop()

    def display(self):
        """Display the canvas."""
        # from https://www.pythontutorial.net/tkinter/tkinter-object-oriented-application/
        # field options
        self.options = {"padx": 5, "pady": 5}

        self.canvas = tk.Canvas(width=200, height=200, bg="sienna2")
        self.canvas.grid(column=1, row=1, **self.options)

        self.p = Path(os.path.realpath(__file__)).parent
        self.logo_file_name: Path = Path.resolve(self.p / "logo.gif")

        # with assistance from https://www.pythontutorial.net/tkinter/tkinter-thread-progressbar/
        pil_img = Image.open(self.logo_file_name)

        # resize the picture
        resized_img = pil_img.resize((200, 200), Image.Resampling.LANCZOS)

        self.logo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(resized_img)
        # use image to create a canvas image
        self.img_logo = self.canvas.create_image((100, 102.5), image=self.logo_image)

        self.btn_crypt = ttk.Button(text="Run!", command=self.message)
        self.btn_crypt.grid(column=1, row=2, **self.options)

        self.loading = ttk.Progressbar(
            orient="horizontal", length=50, mode="indeterminate"
        )

    # Test your program. Choose “encrypt” in the task window. When the message window pops up, enter the sort of message a spy might want to keep secret.
    # If you select the encrypted text and copy it, you can choose the “decrypt” option next time round the loop. In the message window, paste the encrypted message and click OK. You'll then see the original message again.
    # Your cipher program should now be working. To make sure, try decrypting the text shown here.

    # modify: You can add these extra features to your program.
    # To make it harder still for people to break your encryption, reverse the message after encrypting it with swap_letters. To do this, you'll need to create two different functions - one to encrypt and one to decrypt.
    # Another way to encrypt messages is to insert random letters between each pair of letters. So the word 'secret' might become 'stegciraelta' or 'shevcarieste'. You'll need two different functions, one to encrypt and one to decrypt.

    def get_task(self):
        """Ask if it should encrypt or decrypt."""
        # “Task” is the title of the dialog box
        task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt?")
        # return passes the value of task back into the main program
        return task

    def get_message(self):
        """Ask for the message."""
        # “Message” is the title of the dialog box
        message = simpledialog.askstring("Message", "Enter the secret message: ")
        # return passes the value of message back into the main program
        return message

    def is_even(self, number):
        """Tell the program whether or not there's an even number of characters in your message.

        The function will use the modulo operator (%) to check if it can divide the number by 2 without leaving a remainder. If it can (True), then the number is even. Return the True or False result back to the program. Add this function to the top of the code directly under the import statement.
        """
        remainder = number % 2
        is_remainder: bool = remainder != 0

        return not is_remainder

    def get_even_letters(self, message: str):
        """Produce a list containing all the even-numbered letters.

        The function uses a for loop with a range that goes from 0 to len(message), so that it checks all the letters in the string. Add this function under the is_even function.
        """
        even_letters = []  # Create an empty list even_letters.
        # Start a for loop with a range from 0 to the length of the message.
        for i, letter in enumerate(message):
            # In the loop, call the is_even function in an if statement
            # If is_even returns True, append the letter to the even_letters list.
            if self.is_even(i):
                even_letters.append(letter)
        return even_letters  # Return the even_letters list back to the program.

    def get_odd_letters(self, message):
        """Produce a list of all the odd-numbered letters in your message."""
        odd_letters = []  # Create an empty list odd_letters.
        # Start a for loop with a range from 0 to the length of the message.
        for i, letter in enumerate(message):
            # In the loop, call the is_even function in an if statement
            # If is_even returns False, append the letter to the odd_letters list.
            if not self.is_even(i):
                odd_letters.append(letter)
        return odd_letters  # Return the odd_letters list back to the program.

    def swap_letters(self, message: str):
        """Now that you've got even letters in one list and odd in another, you can use them to encrypt your message. The next function swap_letters will take letters alternately from these lists and put them into a new list. But rather than assembling them in the original order, starting with an even letter, it'll start the message with an odd one. Type this function under the get_odd_letters function from step 10."""
        # Create an empty list letter_list.
        letter_list = []
        # If the length of the message is not even, append the letter 'x' to the end of the message.
        if not self.is_even(len(message)):
            message += "x"
        # Create a variable even_letters and assign it the value returned from the get_even_letters function.
        even_letters = self.get_even_letters(message)

        # Create a variable odd_letters and assign it the value returned from the get_odd_letters function.
        odd_letters = self.get_odd_letters(message)
        # Start a for loop with a range from 0 to the length of the list divided by 2. Because you are dividing, don't forget to convert (len(message)2) to an integer.
        for i in range(0, int(len(message) / 2)):
            # In the loop, append an odd letter to letter_list and then append an even letter.
            letter_list.append(odd_letters[i])
            letter_list.append(even_letters[i])
        # Outside the loop, create a new_message that joins the list of letters into a string
        new_message = "".join(letter_list)

        # Return new_message.
        return new_message


# Now that you've created your interface functions, add this infinite while loop to call them in the correct order.
if __name__ == "__main__":
    root: tk.Tk = SecretMessageGUI()
    frame: ttk.Frame = MainFrame(root)
    root.mainloop()
