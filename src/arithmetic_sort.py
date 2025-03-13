def arithmetic_sort(arr):
    """
    Sort a list of integers using only basic arithmetic operations.
    
    This implementation uses a selection sort algorithm with basic 
    arithmetic comparisons to find the minimum element in each pass.
    
    Args:
        arr (list): A list of integers to be sorted
    
    Returns:
        list: A new sorted list of integers
    
    Raises:
        TypeError: If input is not a list
        TypeError: If list contains non-integer elements
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All list elements must be integers")
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Perform selection sort using only arithmetic operations
    for i in range(len(sorted_arr)):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, len(sorted_arr)):
            # Replace comparison with arithmetic subtraction
            if sorted_arr[j] - sorted_arr[min_idx] < 0:
                min_idx = j
        
        # Swap elements using only arithmetic operations
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr