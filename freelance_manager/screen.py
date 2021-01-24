import curses
from freelance_manager.constants import freelance_manager_welcome, exit_help
import traceback


def status_bar(screen, mode: str):
    screen.addstr(0, 0, freelance_manager_welcome)
    screen.addstr(curses.LINES - 1, 0, mode, curses.A_BOLD)


def multi_text(screen, text: list[str], offset: int):
    for i, text_line in enumerate(text):
        screen.addstr(offset + i, 0, text_line)

    return len(text)


def init():
    # curses init
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    # wide try catch so term doesnt get messed up
    try:
        mode = "LIST"
        while True:

            if mode == "INSERT":
                screen.clear()

                status_bar(screen, mode)

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

                status_bar(screen, mode)

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
                    mode = "LIST"
                    continue

                mode = "LIST"

            screen.clear()
            status_bar(screen, mode)

            screen.refresh()

            key = screen.getch()

            # Break with q
            if key == ord("q"):
                break

            if key == ord("a"):
                screen.addstr(0, 0, "asdfasdf")
                mode = "INSERT"

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
