import pytest
from src.lowercase_converter import convert_to_lowercase

def test_convert_to_lowercase_basic():
    """Test basic lowercase conversion."""
    assert convert_to_lowercase("Hello") == "hello"
    assert convert_to_lowercase("WORLD") == "world"
    assert convert_to_lowercase("MiXeD CaSe") == "mixed case"

def test_convert_to_lowercase_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase("") == ""

def test_convert_to_lowercase_already_lowercase():
    """Test conversion of an already lowercase string."""
    assert convert_to_lowercase("lowercase") == "lowercase"

def test_convert_to_lowercase_with_special_characters():
    """Test conversion with special characters and numbers."""
    assert convert_to_lowercase("Hello, World! 123") == "hello, world! 123"

def test_convert_to_lowercase_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase(["list"])