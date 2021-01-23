import curses
from freelance_manager.constants import freelance_manager_welcome, exit_help


def init():
    # curses init
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    # wide try catch so term doesnt get messed up
    try:
        screen.clear()

        screen.addstr(0, 0, freelance_manager_welcome, curses.A_BOLD)
        screen.addstr(curses.LINES - 1, 0, exit_help)

        screen.refresh()

        screen.getkey()

    except Exception as e:
        print(e)
        exit(-1)

    finally:
        curses.echo()
        curses.nocbreak()
        screen.keypad(False)
        curses.endwin()
