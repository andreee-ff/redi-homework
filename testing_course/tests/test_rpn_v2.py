import pytest
from testing_course.src.rpn_v2 import RPNCalculator

def test_complex_example():
    """
    Example: Test a complex example that combines multiple operations.
    """
    rpn = RPNCalculator()

    rpn.evaluate("1")
    assert rpn.stack == [1]
    rpn.evaluate("2")
    assert rpn.stack == [1, 2]
    rpn.evaluate("+")
    assert rpn.stack == [3]
    rpn.evaluate("5")
    assert rpn.stack == [3, 5]
    rpn.evaluate("*")
    assert rpn.stack == [15]

def test_addition_with_fixture(rpn_calc):
    """
    TODO: Create a fixture named `rpn_calc` that initializes an RPNCalculator instance.
    """
    rpn_calc.evaluate("4")
    rpn_calc.evaluate("5")
    rpn_calc.evaluate("+")
    assert rpn_calc.stack == [9]


def test_zero_division_error():
    """
    Example: Test that division by zero raises ZeroDivisionError.
    """
    rpn = RPNCalculator()
    rpn.evaluate("1")
    rpn.evaluate("0")
    with pytest.raises(ZeroDivisionError):
        rpn.evaluate("/")
    assert rpn.stack == []


def test_invalid_operator_value_error():
    """
    TODO: Complete this test so that it checks that an invalid operator (e.g., '^') triggers a ValueError.
    """
    rpn = RPNCalculator()
    rpn.evaluate("1")
    rpn.evaluate("2")
    # Students: Complete the test below

# TODO: Write a test for the case where there are not enough operands in the stack when an operator is used (Bonus Point)
