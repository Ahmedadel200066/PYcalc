#!/usr/bin/python3

from modules.operations import Operations
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestOperations(unittest.TestCase):
    """
    A test class for testing the Operations class.

    Methods:
    - test_add: Test the add method of the Operations class.
    - test_subtract: Test the subtract method of the Operations class.
    - test_multiply: Test the multiply method of the Operations class.
    - test_divide: Test the divide method of the Operations class.
    - test_power: Test the power method of the Operations class.
    - test_sqrt: Test the sqrt method of the Operations class.
    - test_sin: Test the sin method of the Operations class.
    - test_cos: Test the cos method of the Operations class.
    - test_tan: Test the tan method of the Operations class.
    """

    def test_add(self):
        self.assertEqual(Operations.add(1, 2), 3)
        self.assertEqual(Operations.add(-1, 1), 0)
        self.assertEqual(Operations.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Operations.subtract(10, 5), 5)
        self.assertEqual(Operations.subtract(-1, 1), -2)
        self.assertEqual(Operations.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Operations.multiply(3, 7), 21)
        self.assertEqual(Operations.multiply(-1, 1), -1)
        self.assertEqual(Operations.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Operations.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            Operations.divide(1, 0)

    def test_power(self):
        self.assertEqual(Operations.power(2, 3), 8)
        self.assertEqual(Operations.power(2, 0), 1)

    def test_sqrt(self):
        self.assertEqual(Operations.sqrt(9), 3)
        with self.assertRaises(ValueError):
            Operations.sqrt(-1)

    def test_sin(self):
        self.assertAlmostEqual(Operations.sin(30), 0.5, places=5)

    def test_cos(self):
        self.assertAlmostEqual(Operations.cos(60), 0.5, places=5)

    def test_tan(self):
        self.assertAlmostEqual(Operations.tan(45), 1.0, places=5)


if __name__ == '__main__':
    unittest.main()
