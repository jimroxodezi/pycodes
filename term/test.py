
# colours
FINE_BLUE = "\x1b[48;5;12m"
FORE_BLACK = "\x1b[38;5;16m"
FORE_BLACK_BOLD = "\x1b[1;38;5;16m"
FORE_BLACK_UNDERLINE = "\x1b[4;38;5;16m"
FORE_BLACK_UNDERLINE_BOLD = "\x1b[1;4;38;5;16m"
FORE_BLACK_BLINKING_BOLD = "\x1b[1;5;38;5;16m"

# controls
UP = "\x1b[A"
DOWN = "\x1b[B"
RIGHT = "\x1b[C"
LEFT = "\x1b[D"

# width of terminal is 1000?
print(FINE_BLUE + FORE_BLACK_BLINKING_BOLD + "\x1b[1000D" + "This text is in a beautiful blue colour\x1b[0m")
# this text will overwrite the one above
# print(FINE_BLUE + FORE_BLACK_BLINKING_BOLD + "\x1b[1A" + "This text--blue colour\x1b[0m")
