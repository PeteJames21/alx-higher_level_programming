# Python - if/else, loops, functions

## 0-positive_or_negative.py
Determine if a number is positive or negative

## 1-last_digit.py
Check the last digit of an integer

## 2-print_alphabet.py
Print the entire ascii lowercase alphabet

## 3-print_alphabt.py
Print the entire ascii lowercase alphabet excluding `q` and `e`

## 4-print_hexa.py
Print the numbers of 0-98 in hexadecimals

## 5-print_comb2.py
Print the numbers 0-99 formatted. zero-pad all numbers < 10.

## 6-print_comb3.py
Print combinations of digits
- The two digits must be different
- 01 and 10 are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits

## 7-islower.py
Check if a character is lowercase usnig the `ord()` builtin.

## 8-uppercase.py
Convert and print the uppercase conversion of a string

## 9-print_last_digit.py
Print and return the last digit of a number

## 10-add.py
Write a function that adds two numbers and returns the sum

## 11-pow.py
Compute powers of numbers

## 12-fizzbuzz.py
Implement the fizzbuzz algorithm

## 100-print_tebahpla.py
Prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase), not followed by a new line.

## 101-remove_char_at.py
Write a function that creates a copy of the string, removing the character at the position `n`

## 102-magic_calculation.py
Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
