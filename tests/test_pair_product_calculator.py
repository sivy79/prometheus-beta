import pytest
from src.pair_product_calculator import calculate_pair_products

def test_basic_pair_products():
    """Test basic functionality with simple list of integers."""
    result = calculate_pair_products([1, 2, 3])
    # All unique pair combinations: (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)
    assert result == [1, 2, 3, 2, 4, 6, 3, 6, 9]

def test_negative_numbers():
    """Test functionality with negative numbers."""
    result = calculate_pair_products([-1, 0, 1])
    assert result == [1, 0, -1, 0, 0, 0, -1, 0, 1]

def test_single_element_list():
    """Test with a single-element list."""
    result = calculate_pair_products([5])
    assert result == [25]

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        calculate_pair_products([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_pair_products("not a list")

def test_non_integer_input_raises_error():
    """Test that list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pair_products([1, 2, "3"])

def test_large_numbers():
    """Test functionality with larger numbers."""
    result = calculate_pair_products([10, 20])
    assert result == [100, 200, 200, 400]