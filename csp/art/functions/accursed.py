from curses import wrapper


def main(stdscr):
    # Clear screen
    stdscr.clear()
    i = 2
    stdscr.addstr(i, 1, f"10 divided by {i} is {10 / i}")

    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
