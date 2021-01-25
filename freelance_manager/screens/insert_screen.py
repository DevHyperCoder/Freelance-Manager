import curses

from freelance_manager.screens.multi_line import multi_text
from freelance_manager.screens.status_bar import status_bar


def insert_screen():
    status_bar("INSERT")
    screen = curses.newwin(curses.LINES - 1, curses.COLS, 1, 0)
    screen.refresh()

    curses.echo()

    screen.addstr(1, 0, "Client: ")
    client = screen.getstr()
    screen.addstr(2, 0, "Language: ")
    language = screen.getstr()
    screen.addstr(3, 0, "Price: ")
    price = screen.getstr()
    screen.addstr(4, 0, "Time: ")
    time = screen.getstr()

    screen.clear()

    multi_text_offset = multi_text(screen, [
        "Review Entry:",
        client,
        language,
        price,
        time,
        "",
        "Confirm"
    ], 1)

    if screen.getch() != ord("y"):
        screen.addstr(
            1 + multi_text_offset, 0,
            "Cancel")
