class Calculator:
    def __init__(self, a: float, b: float, operation: int):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 1:
            return self.a + self.b
        elif self.operation == 2:
            return self.a - self.b
        elif self.operation == 3:
            return self.a * self.b
        elif self.operation == 4:
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Error: Invalid operation. Choose a number between 1 and 4."


if __name__ == "__main__":
    try:
        print("Choose the type of operation:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        
        operation = int(input("Enter the operation number (1/2/3/4): "))
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))

        calc = Calculator(a, b, operation)
        result = calc.calculate()
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numeric values for 'a', 'b', and operation number.")

