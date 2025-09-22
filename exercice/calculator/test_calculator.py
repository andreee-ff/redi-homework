import pytest

from exercice.calculator.calculator import Calculator

calculator_fixture_scope = "module"  # TODO (5 Points) add the correct scope here


@pytest.fixture(scope=calculator_fixture_scope)
def calculator():
    return Calculator()


def test_add(calculator):
    """Example: Test subtraction operation."""
    assert calculator.add(2, 3) == 5


def test_subtract(calculator):
    """Example: Test subtraction operation."""
    assert calculator.subtract(5, 3) == 2


def test_multiply(calculator):
    """Test multiplication operation."""
    # TODO (5 Points) : Complete this test
    assert calculator.multiply(5, 3) == 15


def test_divide(calculator):
    """Test division operation."""
    # TODO (5 Points) : Complete this test
    assert calculator.divide(12, 4) == 3


def test_divide_by_zero(calculator):
    #Test division by zero operation.
    # TODO (10 Points) : Complete this test (Hint: use pytest.raises)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(7, 0)


def test_evaluate_add(calculator):
    """Test addition operation."""
    assert calculator.evaluate(2, 3, "add") == 5


def test_evaluate_subtract(calculator):
    """Test subtraction operation."""
    assert calculator.evaluate(5, 3, "subtract") == 2


def test_evaluate_multiply(calculator):
    """Test multiplication operation."""
    assert calculator.evaluate(4, 3, "multiply") == 12


def test_evaluate_divide(calculator):
    """Test division operation."""
    assert calculator.evaluate(10, 2, "divide") == 5

def test_evaluate_invalid_operation(calculator):
    with pytest.raises(ValueError, match='Invalid operation.'):
        calculator.evaluate(2, 5, "banana")

@pytest.mark.parametrize("a, b, op, expected", 
[  
    (4, 3, "add", 7),
    (5, 2, "subtract", 3),
    (6, 3, "multiply", 18),
    (14, 7, "divide", 2)
])

def test_evaluate(calculator, a, b, op, expected):
    """
    TODO (20 Points) : Add the @pytest.mark.parametrize decorator to test multiple operations in one go,
    allowing to replace the individual tests above. (test_evaluate_add, test_evaluate_subtract...)
    """
    assert calculator.evaluate(a, b, op) == expected


