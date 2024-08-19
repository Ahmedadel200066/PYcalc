#!/usr/bin/python3

import unittest
from modules.errors import InvalidOperationError, ZeroDivisionError, NegativeSqrtError

class TestErrors(unittest.TestCase):

    def test_invalid_operation_error(self):
        with self.assertRaises(InvalidOperationError):
            raise InvalidOperationError("Invalid")

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            raise ZeroDivisionError()

    def test_negative_sqrt_error(self):
        with self.assertRaises(NegativeSqrtError):
            raise NegativeSqrtError()

if __name__ == '__main__':
    unittest.main()
