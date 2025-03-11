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
    
    # Immediate false for impossible configurations
    if len(nums) < 2 or max(nums) > target_sum:
        return False
    
    # Sort for better pruning
    nums.sort()
    
    # Recursive solution with pruning
    def can_subset_sum(index, current_sum):
        # Base cases
        if current_sum == 0:
            return True
        if index >= len(nums) or current_sum < 0:
            return False
        
        # Try including or excluding current number
        return (
            can_subset_sum(index + 1, current_sum - nums[index]) or  # Include
            can_subset_sum(index + 1, current_sum)  # Exclude
        )
    
    return can_subset_sum(0, target_sum)