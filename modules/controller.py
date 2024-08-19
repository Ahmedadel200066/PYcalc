#!/usr/bin/python3

from errors import ZeroDivisionError

class CalculatorController:
    def __init__(self):
        self.history = []

    def calculate(self, expression):
        try:
            # For simplicity, using eval, but you can map string operations to the Operations methods.
            result = eval(expression)
            return result
        except ZeroDivisionError as e:
            return str(e)
        except ValueError as e:
            return str(e)
        except Exception as e:
            return "Error"

    def add_to_history(self, operation):
        self.history.append(operation)

    def get_history(self):
        return self.history
