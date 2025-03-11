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

def test_can_partition_complex_scenarios():
    # More complex scenarios
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([1, 2, 3, 4, 5]) == False

def test_can_partition_sum_calculation():
    # Cases with precise sum requirement
    assert can_partition([100, 100, 100, 100, 100, 100]) == True
    assert can_partition([100, 100, 100, 50, 50]) == True
    assert can_partition([2, 2, 2, 2]) == True
    
    # Non-partitionable sets
    assert can_partition([1, 2, 3]) == False
    assert can_partition([1, 2, 4]) == False