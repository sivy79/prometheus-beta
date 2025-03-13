import pytest
from src.unique_grid_paths import find_prime_path, is_prime

def test_is_prime():
    """Test primality checking function"""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(4) == False
    assert is_prime(15) == False

def test_find_prime_path_basic():
    """Test basic prime path scenarios"""
    grid1 = [
        [1, 7, 3],
        [2, 9, 5],
        [6, 4, 8]
    ]
    path = find_prime_path(grid1)
    assert path is not None
    assert len(path) > 0

def test_find_prime_path_complex():
    """Test complex grid with multiple possibilities"""
    grid2 = [
        [2, 3, 5],
        [7, 11, 13],
        [17, 19, 23]
    ]
    path = find_prime_path(grid2)
    assert path is not None
    assert len(path) > 0

def test_find_prime_path_no_prime_sequence():
    """Test grid with no prime sequence"""
    grid3 = [
        [4, 6, 8],
        [9, 12, 15],
        [16, 18, 20]
    ]
    path = find_prime_path(grid3)
    assert path == []

def test_find_prime_path_edge_cases():
    """Test edge cases"""
    # Empty grid
    with pytest.raises(ValueError):
        find_prime_path([])
    
    # Single cell grid
    grid_single = [[2]]
    path = find_prime_path(grid_single)
    assert path == [(0, 0)]

def test_find_prime_path_multi_direction():
    """Test finding prime path in multiple directions"""
    grid4 = [
        [1, 1, 3],
        [3, 7, 1],
        [2, 3, 3]
    ]
    path = find_prime_path(grid4)
    assert path is not None
    assert len(path) > 0

def test_prime_sequence_validation():
    """Validate that the path forms a prime sequence"""
    grid5 = [
        [2, 3, 5],
        [1, 1, 3],
        [1, 7, 9]
    ]
    path = find_prime_path(grid5)
    assert path is not None
    
    # Convert path to numbers and verify prime sequence
    if path:
        sequence = [grid5[r][c] for r, c in path]
        sequence_number = int(''.join(map(str, sequence)))
        assert is_prime(sequence_number), f"Sequence {sequence_number} is not prime"