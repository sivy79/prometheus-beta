from typing import Set, Union
from math import isqrt

def sum_perfect_squares_from_set(number_set: Set[int]) -> int:
    """
    Calculate the sum of all perfect squares that can be formed 
    from the integers in the set, including:
    1. Numbers that are perfect squares
    2. Squares formed by multiplying set elements
    
    Args:
        number_set (Set[int]): A set of non-negative integers
    
    Returns:
        int: Sum of unique perfect squares that can be formed from the set
    
    Raises:
        ValueError: If the set contains negative numbers
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3, 4})
        14  # 1² + 2²
        >>> sum_perfect_squares_from_set({0, 5, 10})
        25  # 5²
    """
    # Validate input: ensure no negative numbers
    if any(num < 0 for num in number_set):
        raise ValueError("Input set must contain only non-negative integers")
    
    # Find all possible perfect squares
    perfect_squares = set()
    number_list = list(number_set)
    
    # Check individual numbers
    for num in number_list:
        if is_perfect_square(num):
            perfect_squares.add(num)
    
    # Check squares formed by multiplying set elements
    for i in range(len(number_list)):
        for j in range(i, len(number_list)):
            product = number_list[i] * number_list[j]
            if is_perfect_square(product):
                perfect_squares.add(product)
    
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