from typing import List, Tuple, Optional

def find_shortest_path(grid: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
        grid (List[List[str]]): A 2D grid where:
            '.' represents an empty cell
            'O' represents a blocking cell
            '#' is unused in input
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path coordinates or None if no path exists
    
    Raises:
        ValueError: If grid is empty or not rectangular
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Ensure grid is rectangular
    if any(len(row) != len(grid[0]) for row in grid):
        raise ValueError("Grid must be rectangular")
    
    rows, cols = len(grid), len(grid[0])
    
    # Validate start and end points are traversable
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        return None
    
    # Breadth-First Search for shortest path
    queue = [[(0, 0)]]
    visited = set([(0, 0)])
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        path = queue.pop(0)
        row, col = path[-1]
        
        # Reached bottom-right corner
        if row == rows - 1 and col == cols - 1:
            return path
        
        # Explore neighboring cells
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] != 'O' and 
                (new_row, new_col) not in visited):
                
                new_path = path + [(new_row, new_col)]
                queue.append(new_path)
                visited.add((new_row, new_col))
    
    # No path found
    return None