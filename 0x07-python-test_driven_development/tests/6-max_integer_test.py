#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_empty(self):
        result = max_integer([])
        self.assertIsNone(result, "Expected Null result")

    def test_list_one_element(self):
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_max_element_correct(self):
        result1 = max_integer([1, 2, 3])
        result2 = max_integer([1, 3, 2, 4, 6, 1])
        result3 = max_integer([-12, -3, -9])
        self.assertEqual(result1, 3)
        self.assertEqual(result2, 6)
        self.assertEqual(result3, -3)

    def test_incorrect_arg_type(self):
        with self.assertRaises(TypeError):
            max_integer(9)

    def test_no_arg(self):
        result = max_integer()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
