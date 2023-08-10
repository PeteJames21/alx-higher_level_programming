#!/usr/bin/python3

import hidden_4

# Note: hidden_4 was compiled for Python 3.8.x. Other versions of Python
# will therefore not work with this script.

if __name__ == "__main__":
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)
