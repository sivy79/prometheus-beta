import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_small_numbers():
    """Test small known numbers"""
    assert find_largest_prime_factor(2) == 2
    assert find_largest_prime_factor(7) == 7
    assert find_largest_prime_factor(13) == 13
    assert find_largest_prime_factor(14) == 7
    assert find_largest_prime_factor(15) == 5

def test_composite_numbers():
    """Test larger composite numbers"""
    assert find_largest_prime_factor(21) == 7
    assert find_largest_prime_factor(84) == 7
    assert find_largest_prime_factor(100) == 5
    assert find_largest_prime_factor(1024) == 2
    assert find_largest_prime_factor(999) == 37

def test_large_number():
    """Test a relatively large number"""
    assert find_largest_prime_factor(13195) == 29

def test_prime_number():
    """Test pure prime numbers"""
    assert find_largest_prime_factor(17) == 17
    assert find_largest_prime_factor(97) == 97

def test_error_handling():
    """Test invalid inputs"""
    with pytest.raises(TypeError):
        find_largest_prime_factor("not an int")
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError):
        find_largest_prime_factor(-10)