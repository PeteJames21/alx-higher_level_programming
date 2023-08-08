#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
number_abs = -1 * number if number < 0 else number
ld = number_abs % 10
print(f"Last digit of {number} is {ld}", end=" ")

if ld > 5:
    print("and is greater than 5")
else:
    print("and is less than 6", end=" ")
    if ld == 0:
        print("and is 0")
    else:
        print("and not 0")
