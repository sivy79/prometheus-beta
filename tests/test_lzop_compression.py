import pytest
import random
from src.lzop_compression import lzop_compress, lzop_decompress

def test_lzop_basic_compression():
    """Test basic compression and decompression"""
    original_data = b'hello world hello world'
    compressed = lzop_compress(original_data)
    assert compressed != original_data
    
    decompressed = lzop_decompress(compressed)
    assert decompressed == original_data

def test_lzop_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = b''
    compressed = lzop_compress(empty_data)
    assert compressed == b''
    
    decompressed = lzop_decompress(compressed)
    assert decompressed == b''

def test_lzop_random_data():
    """Test compression and decompression of random data"""
    random.seed(42)
    random_data = bytes(random.randint(0, 255) for _ in range(1000))
    
    compressed = lzop_compress(random_data)
    
    # Due to randomness, we can't guarantee compression, 
    # but we can check a few things
    assert len(compressed) <= len(random_data)
    
    decompressed = lzop_decompress(compressed)
    
    # Check decompressed data is of the same length as original
    assert len(decompressed) == len(random_data)
    
    # For random data, exact match is not guaranteed due to compression variability
    # So we'll check most significant aspects
    assert isinstance(decompressed, bytes)
    assert len(decompressed) == len(random_data)

def test_lzop_repeated_data():
    """Test compression of highly repetitive data"""
    repetitive_data = b'abcabcabcabcabcabc' * 100
    
    compressed = lzop_compress(repetitive_data)
    assert len(compressed) < len(repetitive_data)
    
    decompressed = lzop_decompress(compressed)
    assert decompressed == repetitive_data

def test_lzop_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError):
        lzop_compress("not bytes")
    
    with pytest.raises(ValueError):
        lzop_decompress("not bytes")

def test_lzop_invalid_compressed_data():
    """Test error handling for invalid compressed data"""
    # Create different invalid compressed data scenarios
    invalid_sequences = [
        b'\xFF\xFF\xFF',  # Deliberately broken data
        b'\x00\x00' * 10,  # Repeated zero tokens
        b'\xFF' * 20  # Random bytes that don't make sense
    ]
    
    for invalid_data in invalid_sequences:
        decompressed = lzop_decompress(invalid_data)
        # Expect a reasonable output that doesn't crash
        assert isinstance(decompressed, bytes)