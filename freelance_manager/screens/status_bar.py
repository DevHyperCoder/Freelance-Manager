from freelance_manager.constants import freelance_manager_welcome
import curses


def status_bar(mode: str):
    screen = curses.newwin(1, curses.COLS)
    screen.clear()
    screen.addstr(0, 0, freelance_manager_welcome)
    screen.addstr(0, curses.COLS - (len(mode) + 1), mode, curses.A_BOLD)
    screen.refresh()
