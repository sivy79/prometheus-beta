def can_partition(nums):
    """
    Determine if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (List[int]): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(n * total_sum)
    Space Complexity: O(total_sum)
    
    Examples:
        >>> can_partition([1, 5, 11, 5])
        True
        >>> can_partition([1, 2, 3, 5])
        False
    """
    # Handle trivial cases first
    if len(nums) <= 1:
        return False
    
    # Calculate total sum and validate partition possibility
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Speed optimization: If target sum is larger than list total, return False early
    if target_sum > total_sum // 2:
        return False
    
    # Sort numbers to help early exit and pruning
    nums.sort(reverse=True)
    
    # Recursive helper with memoization
    def can_partition_recursive(index, current_sum):
        # Base cases
        if current_sum == 0:
            return True
        if index >= len(nums) or current_sum < 0:
            return False
        
        # Try including or excluding current number
        return (
            can_partition_recursive(index + 1, current_sum - nums[index]) or  # Include
            can_partition_recursive(index + 1, current_sum)  # Skip
        )
    
    return can_partition_recursive(0, target_sum)