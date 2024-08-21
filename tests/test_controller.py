#!/usr/bin/python3

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from modules.controller import CalculatorController

class TestCalculatorController(unittest.TestCase):

    def setUp(self):
        self.controller = CalculatorController()

    def test_calculate_addition(self):
        result = self.controller.calculate("2+3")
        self.assertEqual(result, 5)

    def test_calculate_division(self):
        result = self.controller.calculate("10/2")
        self.assertEqual(result, 5)

    def test_calculate_division_by_zero(self):
        result = self.controller.calculate("10/0")
        self.assertEqual(result, "Cannot divide by zero.")

    def test_add_to_history(self):
        self.controller.add_to_history("2+3=5")
        self.assertIn("2+3=5", self.controller.get_history())

    def test_get_history(self):
        self.controller.add_to_history("2+3=5")
        self.controller.add_to_history("10/2=5")
        history = self.controller.get_history()
        self.assertEqual(len(history), 2)

if __name__ == '__main__':
    unittest.main()
