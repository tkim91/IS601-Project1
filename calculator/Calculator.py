from calculator.Multiplication import multiply
from calculator.Division import divide
from calculator.Addition import add
from calculator.Subtraction import subtract
from calculator.Square import square
from calculator.SquareRoot import sqrt


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        """addition"""
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        """subtraction"""
        self.result = subtract(a, b)
        return self.result

    def multiply(self, a, b):
        """multiplication"""
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        """division"""
        self.result = divide(a, b)
        return self.result

    def square(self, a):
        """square"""
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        """square root"""
        self.result = round(sqrt(a), 8)
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
