"""Math utility functions."""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# TODO: Implement a function to calculate factorial
# Function name: factorial
# Should return the factorial of a non-negative integer
# Should raise ValueError for negative numbers


# TODO: Implement a function to check if a number is prime
# Function name: is_prime
# Should return True if the number is prime, False otherwise
# Should handle edge cases (numbers less than 2 are not prime)
