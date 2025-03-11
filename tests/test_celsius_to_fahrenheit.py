import pytest
from src.celsius_to_fahrenheit import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():
    """Test conversion of positive temperatures."""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6

def test_celsius_to_fahrenheit_negative():
    """Test conversion of negative temperatures."""
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-273.15) == -459.67

def test_celsius_to_fahrenheit_float():
    """Test conversion of float temperatures."""
    assert round(celsius_to_fahrenheit(25.5), 1) == 77.9

def test_celsius_to_fahrenheit_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([1, 2, 3])