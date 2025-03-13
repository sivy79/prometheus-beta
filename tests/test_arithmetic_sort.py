import pytest
from src.arithmetic_sort import arithmetic_sort

def test_arithmetic_sort_basic():
    """Test sorting of basic integer list"""
    arr = [5, 2, 9, 1, 7]
    assert arithmetic_sort(arr) == [1, 2, 5, 7, 9]

def test_arithmetic_sort_already_sorted():
    """Test sorting of an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert arithmetic_sort(arr) == [1, 2, 3, 4, 5]

def test_arithmetic_sort_reverse_sorted():
    """Test sorting of a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert arithmetic_sort(arr) == [1, 2, 3, 4, 5]

def test_arithmetic_sort_with_duplicates():
    """Test sorting of a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert arithmetic_sort(arr) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_arithmetic_sort_empty_list():
    """Test sorting of an empty list"""
    arr = []
    assert arithmetic_sort(arr) == []

def test_arithmetic_sort_single_element():
    """Test sorting of a single-element list"""
    arr = [42]
    assert arithmetic_sort(arr) == [42]

def test_arithmetic_sort_negative_numbers():
    """Test sorting of list with negative numbers"""
    arr = [-5, 3, -2, 0, 7, -1]
    assert arithmetic_sort(arr) == [-5, -2, -1, 0, 3, 7]

def test_arithmetic_sort_raises_type_error_non_list():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        arithmetic_sort("not a list")

def test_arithmetic_sort_raises_type_error_non_integers():
    """Test that list with non-integer elements raises TypeError"""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        arithmetic_sort([1, 2, "3", 4])