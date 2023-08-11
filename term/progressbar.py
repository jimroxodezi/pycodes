

from sys import stdout as STDOUT
import time

FORE_BLACK_BLINKING_BOLD = "\x1b[1;5;38;5;16m"
FINE_BLUE = "\x1b[48;5;12m"
FORE_BLACK_BOLD = "\x1b[1;38;5;16m"
FORE_BLACK_UNDERLINE = "\x1b[4;38;5;16m"



def progress():
    print("loading....")
    for i in range(1,101):
        time.sleep(0.05)
        STDOUT.write("\x1b[1000D" + FINE_BLUE + FORE_BLACK_BOLD + str(i) + "%")
        STDOUT.flush()
    print("\x1b[0m")


def progress_bar():
    print("loading....")
    for i in range(1, 101):
        time.sleep(0.05)
        width = i // 2
        bar = "[" + ("#" * width) + " " * (50 - width) + "]"
        STDOUT.write("\x1b[1000D" + FINE_BLUE + FORE_BLACK_BOLD + bar)
        STDOUT.flush()
    print("\x1b[0m")

import random
def many_progress(count: int):
    print("Loading...")
    progresses: list[int] = [0] * count
    STDOUT.write("\n" * count)


    # i don't understand this code yet
    while any(x < 100 for x in progresses):
        time.sleep(0.01)

        # randomly increment one of the progress values
        unfinished: list[tuple[int,int]] = [(i,v) for (i,v) in enumerate(progresses) if v < 100]
        index_of_random_choice, _ = random.choice(unfinished)
        progresses[index_of_random_choice] += 1

        # move the cursor left
        STDOUT.write("\x1b[1000D")
        # move the cursor up
        STDOUT.write(f"\x1b[{str(count)}A")

        for progress in progresses:
            width = progress // 4
            print(FINE_BLUE + FORE_BLACK_BOLD + "[" + ("#" * width) + (" " * (25 - width)) + "]")
    print("\x1b[0m")



# print(any([1,2,3,4]))
# progress_bar()
progress()
many_progress(4)
progress_bar()