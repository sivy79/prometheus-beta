import pytest
from src.perfect_square_sum import sum_perfect_squares_from_set

def test_basic_perfect_square_sum():
    """Test basic scenario with some perfect squares"""
    assert sum_perfect_squares_from_set({1, 2, 3, 4}) == 14

def test_empty_set():
    """Test with an empty set"""
    assert sum_perfect_squares_from_set(set()) == 0

def test_no_perfect_squares():
    """Test with a set containing no perfect squares"""
    assert sum_perfect_squares_from_set({7, 11, 13}) == 0

def test_zero_included():
    """Test with zero in the set"""
    assert sum_perfect_squares_from_set({0, 3, 4}) == 16

def test_multiple_square_formation():
    """Test complex square formation from multiple numbers"""
    assert sum_perfect_squares_from_set({2, 3, 6}) == 49  # 2² + 3² + 6²

def test_negative_numbers_raise_error():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Input set must contain only non-negative integers"):
        sum_perfect_squares_from_set({-1, 2, 3})

def test_duplicates_not_affecting_sum():
    """Test that duplicates do not affect the sum"""
    assert sum_perfect_squares_from_set({1, 1, 2, 2, 3, 3}) == 14

def test_large_numbers():
    """Test with larger numbers"""
    assert sum_perfect_squares_from_set({10, 20, 30}) == 1100  # 10² + 20² + 30²