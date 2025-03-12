import pytest
from src.grid_shortest_path import find_shortest_path

def test_basic_path():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) == 5  # Minimum path length is 4 steps + start
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_blocked_start():
    grid = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_blocked_end():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    path = find_shortest_path(grid)
    assert path is None

def test_path_with_obstacles():
    grid = [
        ['.', '.', '.', '.'],
        ['.', 'O', 'O', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']
    ]
    path = find_shortest_path(grid)
    assert path is not None
    assert len(path) <= 7  # Minimum path around obstacles
    assert path[0] == (0, 0)
    assert path[-1] == (3, 3)

def test_empty_grid():
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_non_rectangular_grid():
    with pytest.raises(ValueError):
        find_shortest_path([
            ['.', '.', '.'],
            ['.', '.'],
            ['.', '.', '.']
        ])

def test_single_cell_grid():
    grid = [['.']
    ]
    path = find_shortest_path(grid)
    assert path == [(0, 0)]

def test_completely_blocked_grid():
    grid = [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O']
    ]
    path = find_shortest_path(grid)
    assert path is None