#!/usr/bin/python3

class CalculatorController:
    """
    A class that represents a calculator controller.

    Attributes:
        history (list): A list to store the history of operations.

    Methods:
        calculate(expression): Calculates the result of the given expression.
        add_to_history(operation): Adds the given operation to the history.
        get_history(): Returns the history of operations.
    """

    """
        Calculates the result of the given expression.

        Args:
            expression (str): The mathematical expression to be evaluated.

        Returns:
            float or str: The result of the calculation or an error message.

        Raises:
            ZeroDivisionError: If the expression involves division by zero.
            ValueError: If the expression is invalid.
            Exception: If an unexpected error occurs.
        """

    """
        Adds the given operation to the history.

        Args:
            operation (str): The operation to be added to the history.
        """

    """
        Returns the history of operations.

        Returns:
            list: The list of operations in the history.
        """

    def __init__(self):
        self.history = []

    def calculate(self, expression):
        try:
            # For simplicity, using eval, but you can map string operations to methods.
            result = expression
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
