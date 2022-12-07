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

        self.window: ttk.Frame = ttk.Frame(self)
        self.window.grid(column=0, row=0, sticky="news")

        self.canvas: tk.Canvas = tk.Canvas(
            self.window, width=400, height=400, bg="black"
        )
        self.canvas.grid(column=1, row=1)

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
            self.window, text="Score: " + str(self.score), justify="center"
        )
        self.score_display.grid(column=1, row=2)

        # Level widget
        self.level = 1
        self.level_display = ttk.Label(
            self.window, text="Level: " + str(self.level), justify="center"
        )
        self.level_display.grid(column=1, row=3)

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

        # Bind the keys to the character
        self.canvas.bind_all("<KeyPress>", self.check_input)  # bind key press
        self.canvas.bind_all("<KeyRelease>", self.end_input)  # bind all keys to circle

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
        self.window.after(1000, self.make_candy())

    def move_candy(self):
        """Move the candies downward."""
        for candy in self.candy_list:
            self.canvas.move(candy, 0, self.candy_speed)
            if self.canvas.coords(candy)[1] > 400:
                xposition = rand.randint(1, 400)
                self.canvas.coords(candy, xposition, 0, xposition + 30, 30)
        self.window.after(50, (self.move_candy()))

    # Step 3: Add code to update the score and end the game

    def update_score_level(self):
        """Update the score, level, and candy_speed."""
        self.score = self.score + 1
        self.score_display.config(text="Score :" + str(self.score))
        if 5 < self.score <= 10:
            self.candy_speed = self.candy_speed + 1
            level = 2
            self.level_display.config(text="Level :" + str(level))
        elif self.score > 10:
            self.candy_speed = self.candy_speed + 1
            level = 3
            self.level_display.config(text="Level :" + str(level))

    # Step 4: Add code to check if candy and character collide

    # Collision function to check distance between objects
    def collision(self, item1, item2, distance):
        xdistance = abs(self.canvas.coords(item1)[0] - self.canvas.coords(item2)[0])
        ydistance = abs(self.canvas.coords(item1)[1] - self.canvas.coords(item2)[1])
        overlap = xdistance < distance and ydistance < distance

    # Check hits function to see if character hits a bad candy
    def check_hits(self):
        for candy in self.bad_candy_list:
            if self.collision(self.character, candy, 30):
                self.game_over = self.canvas.create_text(
                    200, 200, text="Game Over", fill="red"
                )
                self.window.after(2000, self.end_game_over)
        for candy in self.candy_list:
            if self.collision(self.character, candy, 30):
                self.canvas.delete(candy)
                self.candy_list.remove(candy)
                self.update_score_level()

    # Step 5:Add code to control the character with arrow keys

    # Direction variable
    move_direction = 0

    def check_input(self, event):
        """Handle when user presses arrow keys."""
        key = event.keysym
        if key == "Right":
            self.move_direction = "Right"
        elif key == "Left":
            self.move_direction = "Left"

    def end_input(self, event):
        """Stop movement when user does not press arrow keys."""
        self.move_direction = "None"

    def move_character(self):
        """Move character."""
        if (
            self.move_direction == "Right"
            and self.canvas.coords(self.character)[0] < 400
        ):
            # Increase character x position
            self.canvas.move(self.character, 10, 0)
        if (
            self.move_direction == "Left"
            and self.canvas.coords(self.character)[0] < 400
        ):
            # Decrease character x position
            self.canvas.move(self.character, -10, 0)
        self.window.after(16, self.move_character)

    # Step 6: Schedule all the functions and make a working game!

    # Schedule all of the functions
    def end_game_over(self):
        """End the game."""
        self.window.destroy()

    def end_title(self):
        """Show the end screen."""
        self.canvas.delete(self.game_title)
        self.canvas.delete(self.directions)


# Step 1 - Create the GUI

if __name__ == "__main__":
    root = CandyMonsterGUI()
    # last line of code
    root.mainloop()
