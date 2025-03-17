import pytest
import random
from src.random_integer_generator import generate_random_integer

def test_random_integer_basic_range():
    """Test generating random integer in a basic range."""
    result = generate_random_integer(1, 10)
    assert 1 <= result <= 10, "Result should be within the specified range"

def test_random_integer_same_min_max():
    """Test generating random integer when min and max are the same."""
    result = generate_random_integer(5, 5)
    assert result == 5, "Should return the same number when min and max are equal"

def test_random_integer_negative_range():
    """Test generating random integer in a negative range."""
    result = generate_random_integer(-10, -1)
    assert -10 <= result <= -1, "Result should be within the specified negative range"

def test_random_integer_mixed_range():
    """Test generating random integer in a mixed positive and negative range."""
    result = generate_random_integer(-5, 5)
    assert -5 <= result <= 5, "Result should be within the specified mixed range"

def test_random_integer_invalid_type():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer(1.5, 10)
    
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        generate_random_integer("1", 10)

def test_random_integer_invalid_range():
    """Test that ValueError is raised when min_value > max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        generate_random_integer(10, 1)

def test_random_integer_distribution():
    """Test that the function provides a reasonably uniform distribution."""
    # Set a specific seed for reproducibility
    random.seed(42)
    
    # Generate a large number of random integers
    min_val, max_val = 1, 10
    samples = [generate_random_integer(min_val, max_val) for _ in range(10000)]
    
    # Check that each number appears with roughly equal frequency
    value_counts = {x: samples.count(x) for x in range(min_val, max_val + 1)}
    
    # Calculate expected count (uniform distribution)
    expected_count = len(samples) / (max_val - min_val + 1)
    
    # Allow some variance for randomness (standard deviation-based check)
    for count in value_counts.values():
        assert abs(count - expected_count) < 3 * (expected_count ** 0.5), \
            "Distribution of random integers seems significantly skewed"