import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_basic():
    """Test basic sorting of integers"""
    assert bubble_sort([5, 2, 9, 1, 7]) == [1, 2, 5, 7, 9]

def test_bubble_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_bubble_sort_empty_list():
    """Test sorting an empty list"""
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element"""
    assert bubble_sort([42]) == [42]

def test_bubble_sort_float_numbers():
    """Test sorting a list of floating-point numbers"""
    assert bubble_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_bubble_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert bubble_sort([-5, -2, -9, -1, -7]) == [-9, -7, -5, -2, -1]

def test_bubble_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    assert bubble_sort([5, -2, 9, -1, 7]) == [-2, -1, 5, 7, 9]

def test_bubble_sort_non_list_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        bubble_sort("not a list")

def test_bubble_sort_uncomparable_elements():
    """Test that a TypeError is raised for uncomparable elements"""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        bubble_sort([1, 2, "a"])