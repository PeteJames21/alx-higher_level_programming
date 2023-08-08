#!/usr/bin/python3

def uppercase(s):
    for char in s:
        i = ord(char)
        if i >= ord("a") and i <= ord("z"):
            i -= 32  # Convert to uppercase
        print("{}".format(chr(i)), end="")
    print()
