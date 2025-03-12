import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bellman_ford import bellman_ford

def test_basic_shortest_path():
    """Test a basic graph with known shortest paths"""
    graph = [
        (0, 1, 4),   # edge from vertex 0 to vertex 1 with weight 4
        (0, 2, 3),   # edge from vertex 0 to vertex 2 with weight 3
        (1, 2, 1),   # edge from vertex 1 to vertex 2 with weight 1
        (1, 3, 2),   # edge from vertex 1 to vertex 3 with weight 2
        (2, 3, 5)    # edge from vertex 2 to vertex 3 with weight 5
    ]
    num_vertices = 4
    start = 0
    
    distances = bellman_ford(graph, start, num_vertices)
    
    assert distances is not None
    assert distances == {0: 0, 1: 4, 2: 3, 3: 6}

def test_negative_weights():
    """Test graph with negative edge weights"""
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (3, 2, 5)
    ]
    num_vertices = 4
    start = 0
    
    distances = bellman_ford(graph, start, num_vertices)
    
    assert distances is not None
    assert distances == {0: 0, 1: -1, 2: 2, 3: 1}

def test_negative_cycle_detection():
    """Test graph with a negative cycle"""
    graph = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, -2)
    ]
    num_vertices = 3
    start = 0
    
    distances = bellman_ford(graph, start, num_vertices)
    
    assert distances is None

def test_single_vertex():
    """Test graph with a single vertex"""
    graph = []
    num_vertices = 1
    start = 0
    
    distances = bellman_ford(graph, start, num_vertices)
    
    assert distances == {0: 0}

def test_invalid_start_vertex():
    """Test with an invalid start vertex"""
    graph = [(0, 1, 4), (1, 2, 3)]
    num_vertices = 3
    
    with pytest.raises(ValueError, match="Start vertex 3 is out of valid range"):
        bellman_ford(graph, 3, num_vertices)

def test_empty_graph_with_multiple_vertices():
    """Test that empty graph works for multiple vertices"""
    graph = []
    num_vertices = 5
    start = 3
    
    distances = bellman_ford(graph, start, num_vertices)
    
    assert distances == {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: 0, 4: float('inf')}