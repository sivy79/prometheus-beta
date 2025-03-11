import pytest
from src.bit_reversal import reverse_bits

def test_reverse_bits_basic():
    """Test basic bit reversal scenarios."""
    # Example from problem statement
    assert reverse_bits(43261596) == 964176192
    
    # All zeros
    assert reverse_bits(0) == 0
    
    # All ones
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF

def test_reverse_bits_edge_cases():
    """Test edge cases for bit reversal."""
    # Single bit at different positions
    assert reverse_bits(1) == 2147483648  # 1 -> 2^31
    assert reverse_bits(2147483648) == 1  # 2^31 -> 1

def test_reverse_bits_invalid_input():
    """Test error handling for invalid inputs."""
    # Negative number
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(-1)
    
    # Number out of 32-bit unsigned integer range
    with pytest.raises(ValueError, match="Input must be a 32-bit unsigned integer"):
        reverse_bits(2**33)

def test_reverse_bits_symmetry():
    """Test that reversing bits twice returns the original number."""
    test_numbers = [0, 1, 42, 255, 65535, 4294967295]
    for num in test_numbers:
        assert reverse_bits(reverse_bits(num)) == num