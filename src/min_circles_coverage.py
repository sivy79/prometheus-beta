from typing import List, Tuple, Optional
import math

class Circle:
    def __init__(self, x: float, y: float, radius: float):
        """
        Initialize a circle with center coordinates and radius.
        
        Args:
            x (float): x-coordinate of circle's center
            y (float): y-coordinate of circle's center
            radius (float): radius of the circle
        """
        self.x = x
        self.y = y
        self.radius = radius

def calculate_distance(circle1: Circle, circle2: Circle) -> float:
    """
    Calculate Euclidean distance between two circle centers.
    
    Args:
        circle1 (Circle): First circle
        circle2 (Circle): Second circle
    
    Returns:
        float: Distance between circle centers
    """
    return math.sqrt((circle1.x - circle2.x)**2 + (circle1.y - circle2.y)**2)

def do_circles_overlap(circle1: Circle, circle2: Circle) -> bool:
    """
    Check if two circles overlap or touch.
    
    Args:
        circle1 (Circle): First circle
        circle2 (Circle): Second circle
    
    Returns:
        bool: True if circles overlap or touch, False otherwise
    """
    distance = calculate_distance(circle1, circle2)
    return distance <= circle1.radius + circle2.radius

def find_minimum_covering_circles(input_circles: List[Circle]) -> List[Circle]:
    """
    Find the minimum number of circles to cover all input circles without overlap.
    
    Args:
        input_circles (List[Circle]): List of input circles to be covered
    
    Returns:
        List[Circle]: Minimum set of circles that cover all input circles
    
    Raises:
        ValueError: If input_circles is empty
    """
    if not input_circles:
        raise ValueError("Input circles list cannot be empty")
    
    # If only one circle, return it
    if len(input_circles) == 1:
        return input_circles
    
    # Sort circles by radius in descending order
    sorted_circles = sorted(input_circles, key=lambda c: c.radius, reverse=True)
    
    # Greedy approach to find covering circles
    covering_circles = []
    
    for circle in sorted_circles:
        # Check if this circle is already covered by existing covering circles
        if any(do_circles_overlap(circle, existing) for existing in covering_circles):
            continue
        
        # Add this circle to covering circles
        covering_circles.append(circle)
    
    return covering_circles