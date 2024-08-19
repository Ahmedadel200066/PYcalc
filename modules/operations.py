#!/usr/bin/python3

import math

class Operations:
    """Class containing methods for basic and scientific operations."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def sqrt(a):
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(a)

    @staticmethod
    def sin(a):
        return math.sin(math.radians(a))

    @staticmethod
    def cos(a):
        return math.cos(math.radians(a))

    @staticmethod
    def tan(a):
        return math.tan(math.radians(a))