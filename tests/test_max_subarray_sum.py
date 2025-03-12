import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_case():
    """Test with a standard input array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39

def test_single_element_window():
    """Test with window size of 1"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 1
    assert max_subarray_sum(arr, k) == 23

def test_full_array_window():
    """Test when window size equals array length"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = len(arr)
    assert max_subarray_sum(arr, k) == sum(arr)

def test_window_larger_than_array():
    """Test when window size is larger than array length"""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) is None

def test_empty_array():
    """Test with an empty array"""
    arr = []
    k = 3
    assert max_subarray_sum(arr, k) is None

def test_negative_window_size():
    """Test with a negative window size"""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        max_subarray_sum(arr, -1)

def test_zero_window_size():
    """Test with a zero window size"""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        max_subarray_sum(arr, 0)

def test_negative_numbers():
    """Test with an array containing negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3