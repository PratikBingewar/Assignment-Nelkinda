import pytest
from factorial import calculate_factorial

def test_factorial_with_positive_number():
    assert calculate_factorial(5) == 120

def test_factorial_with_zero():
    assert calculate_factorial(0) == 1

def test_factorial_with_negative_number():
    with pytest.raises(ValueError):
        calculate_factorial(-5)
