import pytest
from src.custom_stack import CustomStack

def test_stack_initialization():
    """Test stack initialization with default and custom capacity."""
    stack = CustomStack()
    assert len(stack) == 0
    assert stack.is_empty() == True

    custom_stack = CustomStack(capacity=5)
    assert len(custom_stack) == 0
    assert custom_stack.is_empty() == True

def test_invalid_stack_initialization():
    """Test that stack creation fails with invalid capacity."""
    with pytest.raises(ValueError):
        CustomStack(capacity=0)
    with pytest.raises(ValueError):
        CustomStack(capacity=-1)

def test_push_and_pop():
    """Test push and pop operations."""
    stack = CustomStack()
    
    # Push different types of data
    stack.push(10)
    stack.push("hello")
    stack.push([1, 2, 3])
    
    assert len(stack) == 3
    assert stack.is_empty() == False
    
    # Verify pop order (last in, first out)
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 10
    
    assert len(stack) == 0
    assert stack.is_empty() == True

def test_peek():
    """Test peek operation."""
    stack = CustomStack()
    
    stack.push(42)
    assert stack.peek() == 42
    assert len(stack) == 1  # Peek should not remove the item
    
    stack.push("test")
    assert stack.peek() == "test"
    assert len(stack) == 2

def test_stack_overflow():
    """Test that stack prevents pushing beyond capacity."""
    stack = CustomStack(capacity=2)
    
    stack.push(1)
    stack.push(2)
    
    with pytest.raises(OverflowError):
        stack.push(3)

def test_empty_stack_operations():
    """Test operations on an empty stack."""
    stack = CustomStack()
    
    with pytest.raises(IndexError):
        stack.pop()
    
    with pytest.raises(IndexError):
        stack.peek()