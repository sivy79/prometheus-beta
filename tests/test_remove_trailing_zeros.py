import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros_basic():
    """Test basic cases of removing trailing zeros."""
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(123000) == 123
    assert remove_trailing_zeros(45600) == 456

def test_remove_trailing_zeros_zero():
    """Test handling of zero input."""
    assert remove_trailing_zeros(0) == 0

def test_remove_trailing_zeros_no_zeros():
    """Test numbers without trailing zeros."""
    assert remove_trailing_zeros(123) == 123
    assert remove_trailing_zeros(1) == 1

def test_remove_trailing_zeros_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        remove_trailing_zeros(-10200)

def test_remove_trailing_zeros_large_number():
    """Test handling of large numbers with trailing zeros."""
    assert remove_trailing_zeros(1000000) == 1
    assert remove_trailing_zeros(10000000000) == 1