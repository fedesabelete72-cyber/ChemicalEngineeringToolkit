class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero."

        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result

    def show_history(self):
        if not self.history:
            print("\nNo calculations yet.")
            return

        print("\n===== Calculation History =====")
        for item in self.history:
            print(item)