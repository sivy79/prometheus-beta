import os
from typing import Union, Optional

def find_oldest_file(directory: str) -> Optional[str]:
    """
    Find the oldest file in a given directory.

    Args:
        directory (str): Path to the directory to search for the oldest file.

    Returns:
        Optional[str]: Full path to the oldest file, or None if no files exist.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Specified path is not a directory: {directory}")

    # Get list of files in the directory
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except PermissionError:
        # Handle permission issues when listing directory contents
        return None

    # If no files exist, return None
    if not files:
        return None

    # Find the oldest file based on creation time
    try:
        oldest_file = min(files, key=os.path.getctime)
        return oldest_file
    except Exception:
        # Fallback in case of any unexpected errors
        return None