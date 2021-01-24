import curses
from freelance_manager.constants import freelance_manager_welcome, exit_help
import traceback


def init():
    # curses init
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    # wide try catch so term doesnt get messed up
    try:
        key = 0
        while True:

            # Break with q
            if key == ord("q"):
                break

            screen.clear()

            screen.addstr(0, 0, freelance_manager_welcome, curses.A_BOLD)
            screen.addstr(curses.LINES - 1, 0, exit_help)

            screen.refresh()

            key = screen.getch()

    except Exception:
        # Show traceback
        error_msg = traceback.format_exc()
        screen.addstr(0, 0, "ERROR", curses.A_BOLD)
        screen.addstr(1, 0, f'{error_msg}\n\nPress any key to exit')
        screen.getkey()
        exit(-1)

    finally:
        curses.echo()
        curses.nocbreak()
        screen.keypad(False)
        curses.endwin()
