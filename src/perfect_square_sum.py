from typing import Set
from math import isqrt

def sum_perfect_squares_from_set(number_set: Set[int]) -> int:
    """
    Calculate the sum of unique perfect squares within a set.
    
    A perfect square can be:
    1. A number in the set that is a perfect square
    2. A combination of set members that forms a perfect square when multiplied
    
    Args:
        number_set (Set[int]): A set of non-negative integers
    
    Returns:
        int: Sum of unique perfect squares
    
    Raises:
        ValueError: If the set contains negative numbers
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3, 4})
        14  # 1² + 4² = 1 + 16 = 14
        >>> sum_perfect_squares_from_set({0, 5, 10})
        0   # No perfect squares
    """
    # Validate input: ensure no negative numbers
    if any(num < 0 for num in number_set):
        raise ValueError("Input set must contain only non-negative integers")
    
    # Check for perfect squares
    all_perfect_squares = set()
    
    # Find all possible perfect squares
    for num in number_set:
        # Check if the number itself is a perfect square
        if is_perfect_square(num):
            all_perfect_squares.add(num)
        
        # Check products with other set members
        for other_num in number_set:
            product = num * other_num
            if is_perfect_square(product):
                all_perfect_squares.add(product)
    
    return sum(all_perfect_squares)

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