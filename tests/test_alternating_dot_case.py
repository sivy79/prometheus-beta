import pytest
from src.alternating_dot_case import to_alternating_dot_case

def test_basic_string_conversion():
    """Test basic string conversion to alternating dot case."""
    assert to_alternating_dot_case("hello world") == 'h.E.l.L.o. .w.O.r.L.d'

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_dot_case("") == ''

def test_single_character():
    """Test conversion of a single character."""
    assert to_alternating_dot_case("a") == 'a'
    assert to_alternating_dot_case("Z") == 'z'

def test_mixed_case_input():
    """Test conversion of a mixed case input string."""
    assert to_alternating_dot_case("MiXeD CaSe") == 'm.I.x.E.d. .c.A.s.E'

def test_string_with_numbers_and_symbols():
    """Test conversion of a string with numbers and symbols."""
    assert to_alternating_dot_case("Hello123 World!") == 'h.E.l.L.o.1.2.3. .w.O.r.L.d.!'

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_dot_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_dot_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_dot_case(["hello"])