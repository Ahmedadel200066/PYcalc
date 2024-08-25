#!/usr/bin/python3
from modules.errors import InvalidOperationError, ZeroDivisionError, NegativeSqrtError
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestErrors(unittest.TestCase):
    """
    A test case class for testing error conditions.

    Methods:
    - test_invalid_operation_error: Test for raising an InvalidOperationError.
    - test_zero_division_error: Test for raising a ZeroDivisionError.
    - test_negative_sqrt_error: Test for raising a NegativeSqrtError.
    """

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
