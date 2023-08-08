#!/usr/bin/python3

# Print the ASCII alphabet in reverse in alternating lower and uppercase.
for i in range(ord('z'), ord('a') - 1, - 1):
    if (i % 2) == 0:
        print("{}".format(chr(i)), end="")  # Print lowercase
    else:
        print("{}".format(chr(i - 32)), end="")  # Print uppercase
