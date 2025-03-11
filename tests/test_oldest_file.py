import os
import pytest
import tempfile
import time

from src.oldest_file import find_oldest_file

def test_find_oldest_file():
    # Create a temporary directory with multiple files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with different creation times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')

        # Create file1 first
        with open(file1_path, 'w') as f:
            f.write('First file')
        time.sleep(0.1)  # Add a small delay to ensure different creation times

        # Create file2 next
        with open(file2_path, 'w') as f:
            f.write('Second file')
        time.sleep(0.1)

        # Create file3 last
        with open(file3_path, 'w') as f:
            f.write('Third file')

        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        assert oldest_file == file1_path, f"Expected {file1_path}, got {oldest_file}"

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Attempt to find oldest file in empty directory
        result = find_oldest_file(temp_dir)
        assert result is None, "Expected None for empty directory"

def test_nonexistent_directory():
    # Test with a nonexistent directory
    with pytest.raises(FileNotFoundError):
        find_oldest_file('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file to use as an invalid input
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            find_oldest_file(temp_file.name)

def test_directory_with_subdirectories():
    # Create a temporary directory with files and subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files 
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')

        # Create subdirectory
        subdir_path = os.path.join(temp_dir, 'subdir')
        os.makedirs(subdir_path)

        # Create files with different times
        with open(file1_path, 'w') as f:
            f.write('First file')
        time.sleep(0.1)
        
        with open(file2_path, 'w') as f:
            f.write('Second file')
        
        # Find oldest file should ignore subdirectories
        oldest_file = find_oldest_file(temp_dir)
        assert oldest_file == file1_path, f"Expected {file1_path}, got {oldest_file}"