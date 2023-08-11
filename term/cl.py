import sys


STDOUT = sys.stdout
RED = "\x1B[0;31m"
RESET = "\x1B[0m"
RED_BACKGROUND = "\x1b[41m"
BLINKING_RED = "\x1B[1;31;5m"
RESET_BLINKING_RED = "\x1b[25m"
GREEN_BACKGROUND = "\x1b[42m"
BRIGHT_RED = "\x1b[1;31m"


print("\x1b[A\r\x1b[K\x1b[1;32mopened " + "\x1b[1;4;34m%s\x1b[0;1;32m in your browser." + RESET)

print(RED + "This should be red" + RESET)
STDOUT.write(RED + "This should be another red\n" + RESET)
STDOUT.write(GREEN_BACKGROUND + BRIGHT_RED + "This is bright red on green background" + RESET)
STDOUT.write(BRIGHT_RED + "\nThis is a bright red colour\n" + RESET)
print(BLINKING_RED + "This text is blinking red" + RESET_BLINKING_RED + " This is another text not blinking" + RESET)