#!/usr/bin/python3

import sys
import calculator_1 as calc

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)  # Remove the name of the script

    # Validate the arguments
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # Perform calculations based on the arguments. The first and third
    # arguments are assumed to be values that are convertible to integers.
    a = int(args[0])
    op = args[1]
    b = int(args[2])

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.sub(a, b)
    elif op == "*":
        result = calc.mul(a, b)
    else:
        result = calc.div(a, b)

    print(f"{a} {op} {b} = {result}")
