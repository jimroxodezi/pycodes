# import tty

# print(tty.__all__)

# UNDERLINE = "\x1b[4m"
# print("\x1b[0;31m" + "nothing")
# # print("\033[31m"+"nothing")
# print(UNDERLINE + "NOTHING")
# print("\x1b[4m\x1b[1;31mHello \x1b[0m" + " " + "\x1b[2;37;41mWorld\x1b[0m")


import sys

FORE_BLACK = "\x1b[38;5;16m"
FORE_BLACK_BOLD = "\x1b[38;5;16m"
REMOVE_COLOUR = "\x1b[0m"

for i in range(0,16):
    # print(f"=====================================row {i}=======================================")
    for j in range(0,16):
        code = str(i*16+j)
        sys.stdout.write("\x1b[38;5;" + code + "m" + code.rjust(4))
        sys.stdout.write("|")
    # print(f"\n=====================================row {i}=======================================\n")
    print(REMOVE_COLOUR)

print()
print("========================================background==========================================")
print()

for i in range(0,16):
    for j in range(0,16):
        code = str(i*16+j)
        sys.stdout.write("\x1b[48;5;" + code + "m" + FORE_BLACK + code.rjust(4))
        # print(REMOVE_COLOUR)
    print(REMOVE_COLOUR)
