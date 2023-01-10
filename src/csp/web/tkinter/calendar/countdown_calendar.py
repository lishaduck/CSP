"""A countdown calendar using csv reading and tkinter."""


import csv
import os
import tkinter as tk
from datetime import date
from datetime import datetime as dt
from pathlib import Path

from csp.utilities import typing_print

p = Path(os.path.realpath(__file__)).parent


class CountdownCalendar(tk.Tk):
    """A countdown calendar."""

    events_file_name = Path.resolve(p / "events.csv")
    events = ""

    def __init__(self):
        """Create an instance of this class."""
        tk.Tk.__init__(self)
        self.title("Countdown Calendar")
        self.wm_geometry("800x800")
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, sticky="news")
        self.frame.pack()

        self.canvas = tk.Canvas(self.frame, width=800, height=800, bg="light sky blue")
        self.canvas.pack()

        self.canvas.create_text(
            400,
            50,
            text="My Countdown Calendar!",
            fill="sienna2",
            font="Arial 28 bold",
        )

        events = self.get_events(self.events_file_name)
        today = date.today()

        vertical_space = 100

        for event in events:
            event_name = event[0]  # get the name of the event
            days_until = self.days_between_dates(event[1], today)
            display = f"It is {days_until} days until {event_name}"

            self.canvas.create_text(
                100,
                vertical_space,
                anchor="w",
                fill="sienna2",
                font="Arial 28 bold",
                text=display,
            )

            vertical_space = vertical_space + 30

        self.frame.tkraise()

    def get_events(self, file_name: Path) -> list[list[object]]:
        """Get events from a file."""
        events: list[list[object]] = []
        typing_print("Fetching events...", end="\r")
        with file_name.open("rt", encoding="utf-8", newline="") as leaderboard_file:
            name_reader = csv.reader(leaderboard_file, dialect="excel")
            for line in name_reader:

                event_date = dt.strptime(line[1], "%m/%d/%Y").date()
                current_event: list[object] = [line[0], event_date]
                events.append(current_event)

                # print(event_date)
        #  return the names list in place of the empty list
        typing_print("Events fetched!   ")
        return events

    def days_between_dates(self, date1, date2: date) -> str:
        """Find the number of days between two dates.

        :param date1: First date
        :type date1: date
        :param date2: Second date
        :return: str
        """
        time_between = str(date1 - date2)
        number_of_days = time_between.split(" ")
        return number_of_days[0]


if __name__ == "__main__":
    app = CountdownCalendar()
    app.mainloop()
