"""Convert inches to centimeters using a GUI."""

import tkinter as tk
import tkinter.messagebox as mb


class ConverterApp(tk.Tk):
    """Convert inches to centimeters using a GUI."""

    inches = 0
    cm = 0

    def __init__(self):
        """Create an instance of this class with a GUI."""
        tk.Tk.__init__(self)

        self.title("Unit Converter")
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, sticky="news")

        vcmd = (self.register(self.validate), "%P")
        ivcmd = (self.register(self.invalidated),)

        self.lbl_inches = tk.Label(self.frame, text="Inches")
        self.lbl_inches.pack(pady=5)
        self.user_data = tk.Entry(
            self.frame,
            validate="focusout",
            validatecommand=vcmd,
            invalidcommand=ivcmd,
        )
        self.user_data.pack(pady=5)

        self.lbl_cm = tk.Label(self.frame, text="Centimeters")
        self.lbl_cm.pack(pady=5)
        self.ent_cm = tk.Label(self.frame, bd=3)
        self.ent_cm.pack(pady=5)

        self.btn_convert = tk.Button(
            self.frame, text="Press to convert", command=self.convert
        )
        self.btn_convert.pack(padx=175, pady=20)

        self.btn_quit = tk.Button(self.frame, text="Exit", command=self.close_window)
        self.btn_quit.pack()

        self.frame.tkraise()

    def convert(self):
        """Convert inches to centimeters."""
        try:
            self.inches = float(self.user_data.get())
            self.cm = self.inches * 2.54
            self.ent_cm.config(text=self.cm)
        except ValueError:
            self.invalidated()

    # thanks to: https://www.pythontutorial.net/tkinter/tkinter-validation/
    def validate(self, value) -> bool:
        """Validate the input."""
        if value.isDigit():
            return True
        return False

    def invalidated(self):
        """Display an error message."""
        mb.showinfo(
            "Value error!",
            "There was invalid input.",
        )

    def close_window(self):
        """Close the window."""
        self.destroy()


if __name__ == "__main__":
    my_win = ConverterApp()

    # start the GUI
    my_win.mainloop()
