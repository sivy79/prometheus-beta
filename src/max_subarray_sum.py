def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a subarray with size k.

    Args:
        arr (list): Input list of integers.
        k (int): Size of the subarray.

    Returns:
        int: Maximum sum of a subarray of size k.
             Returns None if k is larger than the array length.

    Raises:
        ValueError: If k is non-positive.

    Example:
        >>> max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
        39
        >>> max_subarray_sum([2, 3, 4, 1, 5], 3)
        10
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray size (k) must be a positive integer")
    
    # Check if k is larger than array length
    if k > len(arr):
        return None
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum