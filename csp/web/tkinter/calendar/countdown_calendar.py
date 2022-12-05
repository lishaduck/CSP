""""""
import csv
import os
import tkinter as tk
from datetime import datetime as dt
from pathlib import Path

p = Path(os.path.realpath(__file__)).parent


class CountdownCalendar(tk.Tk):
    """A countdown calendar."""

    def __init__(self):
        """Create an instance of this class."""
        tk.Tk.__init__(self)
        self.title("Countdown Calendar")
        self.wm_geometry("800x800")
        self.frame = tk.Frame(self, bg="light sky blue")
        self.frame.grid(row=0, column=0, sticky="news")

        self.canvas = tk.Canvas(self.frame, width=800, height=800)
        self.canvas.pack()

        self.canvas.create_text(
            400,
            50,
            text="My Countdown Calendar!",
            font=("Helvetica", 30),
            fill="black",
        )

        EVENTS_FILE_NAME = Path.resolve(p / "events.csv")
        print(self.get_events(EVENTS_FILE_NAME))

        self.frame.tkraise()

    def get_events(self, file_name: Path):
        """Get events from a file."""
        with file_name.open("rt", encoding="utf-8", newline="") as leaderboard_file:

            events: list[str] = []
            print("Fetching events.")
            name_reader = csv.reader(leaderboard_file, dialect="excel")
            for line in name_reader:

                event_date = dt.strptime(line[1], "%m/%d/%y").date()

                print(event_date)
        #  return the names list in place of the empty list
        return events

    def days_between_dates(self, date1, date2):
        time_between = str(date1 - date2)
        number_of_days = time_between.split("")
        return number_of_days[0]


if __name__ == "__main__":
    app = CountdownCalendar()
    app.mainloop()
