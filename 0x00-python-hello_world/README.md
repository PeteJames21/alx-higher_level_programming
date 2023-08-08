# 0x00. Python - Hello, World

## 0-run
Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable $PYFILE

## 1-run_inline
Write a Shell script that runs Python code. The Python code will be saved in the environment variable $PYCODE

## 2-print.py
Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

## 3-print_number.py
Use f-strings to print an integer

## 4-print_float.py
Use f-strings to format a float

## 5-print_string.py
Perform string multiplication and slicing

## 6-concat.py
Concatenate two strings

## 7-edges.py
More string slicing

## 8-concat_edges.py
Perform string slicing and concatenation

## 9-easter_egg.py
Print The Zen of Python

## 10-check_cycle.c
Write a function in C that checks if a singly linked list has a cycle in it.

## 100-write.py
Write a string to stderr

## 101-compile
Compile a .py files into .pyc using the `compileall` module. Use legacy (pre-PEP3147) compiled file locations where the .pyc files are stored in the current directory instead of the __pychache__ directory.

## 102-magic_calculation.py
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
