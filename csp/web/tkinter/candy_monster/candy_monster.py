"""The Candy Monster Game.

Victor, Eli
"""


import os
import random as rand
import tkinter as tk
from pathlib import Path
from tkinter import ttk


class CandyMonsterGUI(tk.Tk):
    """The Candy Monster Game."""

    p = Path(os.path.realpath(__file__)).parent

    def __init__(self):
        """Create an instance of this class."""
        super().__init__()
        # create window and canvas
        self.title("Nolan - The Game")
        self.config(cursor="target")
        self.wm_geometry("500x500")

        self.root: ttk.Frame = ttk.Frame(self)
        self.root.grid(column=0, row=0, sticky="news")
        self.canvas: tk.Canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.grid(column=0, row=0, sticky="news")

        # create game title and instructions text objects
        self.game_title = self.canvas.create_text(
            200,
            200,
            text="Nolan - The Game:\nThe Candy Monster",
            font=("Arial", 30, "bold"),
            fill="white",
            justify="center",
        )

        self.directions = self.canvas.create_text(
            200,
            275,  # 300 is too far down
            text="Collect Candy but Avoid the Red Ones!",
            font=("Arial", 15, "bold"),  # 30 was too large
            fill="white",
            justify="center",
        )

        # create score display as label widget
        self.score = 0
        self.score_display = ttk.Label(
            self.root, text="Score: " + str(self.score), justify="center"
        )
        self.score_display.grid(column=0, row=1, sticky="news")

        # Level widget
        self.level = 1
        self.level_display = ttk.Label(
            self.root, text="Level: " + str(self.level), justify="center"
        )
        self.level_display.grid(column=0, row=2, sticky="news")

        # create image using green frog
        self.GREEN_CHAR_FILE_NAME = Path.resolve(self.p / "greenChar.gif")
        self.player_image = tk.PhotoImage(file=self.GREEN_CHAR_FILE_NAME)
        # use image to create a canvas image
        self.character = self.canvas.create_image((200, 360), image=self.player_image)

        # Step 2: Add Code to Make Candy and Drop It

        # variable declarations for managing candy
        self.candy_list = []
        self.bad_candy_list = []
        self.candy_speed = 2
        self.candy_color_list = [
            "red",
            "yellow",
            "blue",
            "green",
            "purple",
            "pink",
            "white",
        ]

    # FUNCTION SECTION

    def make_candy(self):
        """Make the candies."""
        xposition = rand.randint(1, 400)
        candy_color = rand.choice(self.candy_color_list)
        candy = self.canvas.create_oval(
            xposition, 0, xposition + 30, 30, fill=candy_color
        )
        self.candy_list.append(candy)
        if candy_color == "red":
            self.bad_candy_list.append(candy)
        self.root.after(1000, self.make_candy())

    def move_candy(self):
        """Move the candies downward."""
        for candy in self.candy_list:
            self.canvas.move(candy, 0, self.candy_speed)
            if self.canvas.coords(candy)[1] > 400:
                xposition = rand.randint(1, 400)
                self.canvas.coords(candy, xposition, 0, xposition + 30, 30)
        self.root.after(50, (self.move_candy()))

    # Step 3: Add code to update the score and end the game

    def update_score_level(self):
        """Update the score, level, and candy_speed."""
        self.score = self.score + 1
        self.score_display.config(text="Score :" + str(self.score))
        if self.score > 5 and self.score <= 10:
            self.candy_speed = self.candy_speed + 1
            level = 2
            self.level_display.config(text="Level :" + str(level))
        elif self.score > 10:
            self.candy_speed = self.candy_speed + 1
            level = 3
            self.level_display.config(text="Level :" + str(level))

    def end_game_over(self):
        """End the game."""
        self.root.destroy()

    def end_title(self):
        """Show the end screen."""
        self.canvas.delete(self.game_title)
        self.canvas.delete(self.directions)

    # Step 4: Add code to check if candy and character collide

    # Collision function to check distance between objects

    # Check hits function to see if character hits a bad candy

    # Step 5:Add code to control the character with arrow keys

    # Direction variable

    # Function to handle when user presses arrow keys

    # Function to stop movement when user does not press arrow keys

    # Function to move character

    # Bind the keys to the character

    # Step 6: Schedule all the functions and make a working game!

    # Schedule all of the functions


# Step 1 - Create the GUI

if __name__ == "__main__":
    window = CandyMonsterGUI()
    # last line of code
    window.mainloop()
