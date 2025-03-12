from typing import Set, Union
from math import isqrt

def sum_perfect_squares_from_set(number_set: Set[int]) -> int:
    """
    Calculate the sum of all perfect squares that can be directly found 
    in the given set of integers.
    
    Args:
        number_set (Set[int]): A set of non-negative integers
    
    Returns:
        int: Sum of perfect squares found directly in the set
    
    Raises:
        ValueError: If the set contains negative numbers
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3, 4})
        14  # Only 1 + 4 as direct perfect squares
        >>> sum_perfect_squares_from_set({0, 5, 10})
        0   # No perfect squares directly in the set
    """
    # Validate input: ensure no negative numbers
    if any(num < 0 for num in number_set):
        raise ValueError("Input set must contain only non-negative integers")
    
    # Find perfect squares directly in the set
    perfect_squares = {num for num in number_set if is_perfect_square(num)}
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)

def is_perfect_square(n: int) -> bool:
    """
    Check if a number is a perfect square.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if the number is a perfect square, False otherwise
    """
    if n < 0:
        return False
    sqrt = isqrt(n)
    return sqrt * sqrt == n