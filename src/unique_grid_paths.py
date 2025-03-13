import typing
from typing import List, Tuple, Set

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find a continuous path of prime number sequence in the grid.
    
    Args:
        grid (List[List[int]]): 2D grid of integers
    
    Returns:
        List[Tuple[int, int]]: Path of coordinates forming a prime number sequence
    
    Raises:
        ValueError: If grid is empty or None
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Special case for single cell grid
    rows, cols = len(grid), len(grid[0])
    if rows == 1 and cols == 1 and is_prime(grid[0][0]):
        return [(0, 0)]
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def dfs(row: int, col: int, current_path: List[Tuple[int, int]], 
            current_sequence: List[int]) -> List[Tuple[int, int]]:
        """
        Depth-first search to find prime number sequence.
        
        Args:
            row (int): Current row
            col (int): Current column
            current_path (List[Tuple[int, int]]): Current path of coordinates
            current_sequence (List[int]): Current sequence of numbers
        
        Returns:
            List[Tuple[int, int]]: Path of prime number sequence if found
        """
        # Check if current cell is valid and not visited
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            (row, col) in visited):
            return []
        
        # Current number
        current_num = grid[row][col]
        
        # Check if current sequence is valid prime sequence
        if len(current_sequence) > 0 and not is_prime(int(''.join(map(str, current_sequence + [current_num])))):
            return []
        
        # Mark as visited
        visited.add((row, col))
        current_path.append((row, col))
        current_sequence.append(current_num)
        
        # If we have a valid prime sequence of at least 2 digits
        if len(current_sequence) >= 2 and is_prime(int(''.join(map(str, current_sequence)))):
            return current_path.copy()
        
        # Explore in all 4 directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Create copies to avoid modifying original lists
            path_copy = current_path.copy()
            sequence_copy = current_sequence.copy()
            
            result = dfs(new_row, new_col, path_copy, sequence_copy)
            if result:
                return result
        
        # Backtrack
        visited.remove((row, col))
        return []
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            visited.clear()
            path = dfs(r, c, [], [])
            if path:
                return path
    
    return []  # No prime number sequence found