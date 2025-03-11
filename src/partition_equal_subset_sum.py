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
    # Empty list or single-element list cannot be partitioned
    if len(nums) <= 1:
        return False
    
    # Check if the total sum is odd (cannot be divided into two equal subsets)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Dynamic programming using a set
    possible_sums = {0}
    
    for num in nums:
        current_sums = set(current_sum + num for current_sum in possible_sums)
        
        # Check if target sum is achievable
        if target_sum in current_sums:
            return True
        
        # Update possible sums
        possible_sums.update(current_sums)
        
        # Pruning: If set gets too large, stop
        if len(possible_sums) > 2 * len(nums):
            break
    
    return False