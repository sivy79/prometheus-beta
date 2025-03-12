import pytest
import math
from src.min_circles_coverage import (
    Circle, 
    calculate_distance, 
    do_circles_overlap, 
    find_minimum_covering_circles
)

def test_circle_initialization():
    circle = Circle(1.0, 2.0, 3.0)
    assert circle.x == 1.0
    assert circle.y == 2.0
    assert circle.radius == 3.0

def test_calculate_distance():
    circle1 = Circle(0, 0, 1)
    circle2 = Circle(3, 4, 1)
    
    expected_distance = 5
    actual_distance = calculate_distance(circle1, circle2)
    
    assert math.isclose(actual_distance, expected_distance)

def test_circles_overlap():
    # Overlapping circles
    circle1 = Circle(0, 0, 2)
    circle2 = Circle(1, 1, 2)
    assert do_circles_overlap(circle1, circle2) is True
    
    # Non-overlapping circles
    circle3 = Circle(0, 0, 1)
    circle4 = Circle(5, 5, 1)
    assert do_circles_overlap(circle3, circle4) is False

def test_minimum_covering_circles_single_circle():
    circle = Circle(1, 1, 2)
    result = find_minimum_covering_circles([circle])
    assert len(result) == 1
    assert result[0] == circle

def test_minimum_covering_circles_multiple_circles():
    # Test multiple circles where some will be covered
    circles = [
        Circle(0, 0, 3),    # Large circle
        Circle(2, 2, 1),    # Small circle inside the first
        Circle(5, 5, 2),    # Another circle
        Circle(10, 10, 1)   # Far circle
    ]
    
    result = find_minimum_covering_circles(circles)
    assert len(result) <= len(circles)
    assert len(result) >= 2

def test_minimum_covering_circles_empty_input():
    with pytest.raises(ValueError, match="Input circles list cannot be empty"):
        find_minimum_covering_circles([])

def test_minimum_covering_circles_no_complete_coverage():
    # Circles that might not have complete coverage
    circles = [
        Circle(0, 0, 1),
        Circle(10, 10, 1),
        Circle(20, 20, 1)
    ]
    
    result = find_minimum_covering_circles(circles)
    assert len(result) == len(circles)  # All circles needed