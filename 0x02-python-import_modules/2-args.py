#!/usr/bin/python3

import sys

if __name__ == "__main__":
    sys.argv.pop(0)  # Remove name of program.
    nargs = len(sys.argv)
    if nargs == 0:
        print("0 arguments.")
        exit()
    elif nargs == 1:
        print("1 argument:")
    elif nargs > 1:
        print(f"{nargs} arguments:")

    for i, arg in enumerate(sys.argv, start=1):
        print(f"{i}: {arg}")
