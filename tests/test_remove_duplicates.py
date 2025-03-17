import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic string duplicate removal."""
    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("aabbcc") == "abc"
    assert remove_duplicates("") == ""

def test_remove_duplicates_preserves_order():
    """Ensure the original order of characters is maintained."""
    assert remove_duplicates("cabbage") == "cabge"
    assert remove_duplicates("Mississippi") == "Misp"

def test_remove_duplicates_mixed_case():
    """Test duplicate removal with mixed case characters."""
    assert remove_duplicates("HelloWorld") == "HeloWrd"

def test_remove_duplicates_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        remove_duplicates(123)
    with pytest.raises(TypeError):
        remove_duplicates(None)
    with pytest.raises(TypeError):
        remove_duplicates(['a', 'b', 'c'])

def test_remove_duplicates_special_characters():
    """Test duplicate removal with special characters."""
    assert remove_duplicates("a!b!c") == "a!bc"
    assert remove_duplicates("!!@@##") == "!@#"