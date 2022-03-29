class Calculator:
    result = 0

    def add(self, value_1):
        """addition"""
        self.result = self.result + value_1
        return self.result

    def subtract(self, value_1):
        """subtraction"""
        self.result = self.result - value_1
        return self.result

    def multiply(self, value_1):
        """multiplication"""
        self.result = self.result * value_1
        return self.result

    def divide(self, value_1):
        """division"""
        self.result = self.result / value_1
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
