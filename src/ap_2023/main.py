"""The main module for the program."""

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """The base class for the app."""

    def __init__(self):
        """The initializing method."""
        super().__init__()

        button = ttk.Button()
        button.pack()


def start_app():
    """Start the app."""
    if __name__ == "__main__":
        App()


start_app()
