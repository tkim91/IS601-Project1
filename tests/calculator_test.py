"""Testing the Calculator"""
from calculator.Calculator import Calculator


def test_calculator_is_instance():
    """Testing the Calculator"""
    calc = Calculator()
    assert isinstance(calc, Calculator)


def test_calculator_get_result_method():
    """Testing the Calculator"""
    calc = Calculator()
    assert calc.get_result() == 0


def test_calculator_result_property():
    """Testing the Calculator"""
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    """Testing the add"""
    calc = Calculator()
    assert calc.add(1, 1) == 2


def test_calculator_subtract_method():
    """Testing the subtraction"""
    calc = Calculator()
    assert calc.subtract(2, 3) == -1


def test_calculator_multiply_method():
    """Testing the multiply"""
    calc = Calculator()
    assert calc.multiply(10, 2) == 20


def test_calculator_divide_method():
    """Testing the divide"""
    calc = Calculator()
    assert calc.divide(10, 2) == 5


def test_calculator_square_method():
    """Testing the square"""
    calc = Calculator()
    assert calc.square(4) == 16


def test_calculator_square_root_method():
    """Testing the square root"""
    calc = Calculator()
    assert calc.squareroot(144) == 12
