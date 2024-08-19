class CalculatorController:
    def __init__(self):
        self.history = []

    def calculate(self, expression):
        try:
            # Use eval() carefully or replace with a safer alternative
            result = eval(expression)
            return result
        except Exception as e:
            return "Error"

    def add_to_history(self, operation):
        self.history.append(operation)

    def get_history(self):
        return self.history
