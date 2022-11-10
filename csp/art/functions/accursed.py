import curses


def wrapped():
    pass


curses.wrapper(wrapped())
