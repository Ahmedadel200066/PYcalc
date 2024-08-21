#!/usr/bin/python3

class CalculatorController:
    def __init__(self):
        self.history = []

    def calculate(self, expression):
        try:
            # For simplicity, using eval, but you can map string operations to methods.
            result = eval(expression)
            return result
        except ZeroDivisionError as e:
            return "Cannot divide by zero."
        except ValueError as e:
            return str(e)
        except Exception as e:
            return "Cannot divide by zero."

    def add_to_history(self, operation):
        self.history.append(operation)

    def get_history(self):
        return self.history