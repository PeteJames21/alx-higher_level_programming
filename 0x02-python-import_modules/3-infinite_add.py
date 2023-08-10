#!/usr/bin/python3

import sys

if __name__ == "__main__":
    sum = 0
    sys.argv.pop(0)  # Remove the name of the program
    for arg in sys.argv:
        sum += int(arg)

    print(sum)
