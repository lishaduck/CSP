"""The Candy Monster Game.

Victor, Eli
"""


import random as rand
import tkinter as tk


class CandyMonsterGUI(tk.Tk):
    """The Candy Monster Game."""

    # TODO: move to proper location
    score_display: tk.Label
    level_display: tk.Label

    directions: int

    def __init__(self):
        """Create an instance of this class."""
        tk.Tk.__init__(self)
        # create window and canvas
        self.title = self.title = "Nolan The Game"
        self.wm_geometry("500x500")

        self.window = tk.Frame(self)
        self.window.pack()
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="black")
        self.canvas.pack()

        # create game title and instructions text objects
        self.title = self.canvas.create_text(
            200,
            200,
            text="Nolan - The Game:\nCandy Monster",
            font=("Arial", 30, "bold"),
            fill="white",
        )

        # create score display as label widget

        # Level widget

        # create image using green frog

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
        self.score = 0

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

    def switch_level(self):
        """Update the score, level, and candy_speed."""

    def update_score_level(self):
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
        self.window.destroy()

    def end_title(self):
        """Show the end screen"""
        self.canvas.delete(self.title)
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

    # last line of code


# Step 1 - Create the GUI

if __name__ == "__main__":
    window = CandyMonsterGUI()
    window.mainloop()
