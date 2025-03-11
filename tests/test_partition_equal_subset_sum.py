import pytest
from src.partition_equal_subset_sum import can_partition

def test_can_partition_basic_cases():
    # Basic cases where partition is possible
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 5]) == False

def test_can_partition_edge_cases():
    # Empty list
    assert can_partition([]) == False
    
    # Single element lists
    assert can_partition([1]) == False
    assert can_partition([2]) == False
    
    # Lists with zero
    assert can_partition([0, 0]) == True
    assert can_partition([1, 0, 1]) == True

def test_can_partition_larger_cases():
    # More complex scenarios
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([1, 2, 3, 4, 5, 6]) == True
    assert can_partition([1, 3, 4, 8]) == False

def test_can_partition_negative_cases():
    # Impossible to partition cases
    assert can_partition([1, 2, 3]) == False
    assert can_partition([1, 1, 1, 1]) == True
    assert can_partition([3, 3, 3, 4, 5]) == False

def test_can_partition_large_numbers():
    # Cases with larger numbers
    assert can_partition([100, 100, 100, 100, 100, 100, 100, 100, 100]) == True
    assert can_partition([1, 1, 1, 1, 1, 1, 1, 1, 100]) == False