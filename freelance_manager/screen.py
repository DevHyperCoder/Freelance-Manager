import curses
import traceback

from freelance_manager.screens.insert_screen import insert_screen
from freelance_manager.screens.status_bar import status_bar


def init():
    # curses init
    curses.initscr()
    curses.noecho()
    curses.cbreak()

    # wide try catch so term doesnt get messed up
    try:
        mode = "LIST"
        while True:

            if mode == "INSERT":
                insert_screen()
                mode = "LIST"
                continue

            status_bar(mode)
            screen = curses.newwin(curses.LINES - 1, curses.COLS, 1, 0)

            screen.refresh()

            key = screen.getch()

            # Break with q
            if key == ord("q"):
                break

            if key == ord("a"):
                mode = "INSERT"

    except Exception:
        # Show traceback
        error_msg = traceback.format_exc()
        screen = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        screen.addstr(0, 0, "ERROR", curses.A_BOLD)
        screen.addstr(1, 0, f'{error_msg}\n\nPress any key to exit')
        screen.getkey()
        exit(-1)

    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
