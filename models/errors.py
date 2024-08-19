class CalculatorError(Exception):
    """Base class for other exceptions"""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted"""
    def __init__(self, operation):
        self.message = f"Invalid operation: {operation}"
        super().__init__(self.message)

class ZeroDivisionError(CalculatorError):
    """Raised when division by zero is attempted"""
    def __init__(self):
        self.message = "Cannot divide by zero."
        super().__init__(self.message)

class NegativeSqrtError(CalculatorError):
    """Raised when attempting to take the square root of a negative number"""
    def __init__(self):
        self.message = "Cannot calculate the square root of a negative number."
        super().__init__(self.message)