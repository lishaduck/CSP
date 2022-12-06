import tkinter as tk


class CandyMonsterGUI(tk.Tk):
    """The Candy Monster Game."""

    def __init__(self):
        """Create an instance of this class."""
        tk.Tk.__init__(self)
        # create window and canvas
        self.title = "Nolan The Game"
        self.wm_geometry("500x500")

        self.window = tk.Frame(self)
        self.window.pack()
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="black")
        self.canvas.pack()

        # create game title and instructions text objects
        self.title = self.canvas.create_text(
            200, 200, text="Candy Monster", font=("Arial", 30), fill="white"
        )

        # create score display as label widget

        # Level widget

        # create image using green frog
