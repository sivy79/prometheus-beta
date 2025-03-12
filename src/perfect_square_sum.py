from typing import Set, Union
from math import isqrt

def sum_perfect_squares_from_set(number_set: Set[int]) -> int:
    """
    Calculate the sum of all unique perfect squares that can be formed from 
    integers in the given set.
    
    Args:
        number_set (Set[int]): A set of non-negative integers
    
    Returns:
        int: Sum of unique perfect squares formed from the set
    
    Raises:
        ValueError: If the set contains negative numbers
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3, 4})
        14  # 1² + 2² + 4² = 1 + 4 + 16 = 14
        >>> sum_perfect_squares_from_set({0, 5, 10})
        25  # 0² + 5² = 0 + 25 = 25
    """
    # Validate input: ensure no negative numbers
    if any(num < 0 for num in number_set):
        raise ValueError("Input set must contain only non-negative integers")
    
    # Find all possible perfect squares
    perfect_squares = set()
    for num in number_set:
        # Check if the number itself is a perfect square
        sqrt = isqrt(num)
        if sqrt * sqrt == num:
            perfect_squares.add(num)
        
        # Check squares that can be formed by multiplying set numbers
        for other_num in number_set:
            square = num * other_num
            sqrt = isqrt(square)
            if sqrt * sqrt == square:
                perfect_squares.add(square)
    
    # Return the sum of unique perfect squares
    return sum(perfect_squares)