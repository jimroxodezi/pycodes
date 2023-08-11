

import tty
import sys
import termios
# import os


STDIN = sys.stdin
STDOUT = sys.stdout

def command_line():

    # tty.setcbreak(STDIN, when=termios.TCSADRAIN)
    old_settings = termios.tcgetattr(STDIN)
    tty.setraw(STDIN, when=termios.TCSANOW)
    STDIN.flush()


    # take keyboard input
    while True:
        c = STDIN.read(1)
        
        # ctrl+c == 3; break the program
        if ord(c) == 3:
            print("exiting")
            STDIN.flush()
            break

        print(ord(c))
        STDOUT.write("\x1b[1000D")

    # restore the original setting of STDIN.
    termios.tcsetattr(STDIN, termios.TCSADRAIN, old_settings)

command_line()