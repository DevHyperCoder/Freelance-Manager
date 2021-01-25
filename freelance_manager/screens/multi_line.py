def multi_text(screen, text: list[str], offset: int):
    for i, text_line in enumerate(text):
        screen.addstr(offset + i, 0, text_line)

    return len(text)
