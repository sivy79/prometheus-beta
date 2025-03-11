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
    
    # Calculate total sum and validate partition possibility
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    
    # Create a dynamic programming set
    dp = {0}
    
    for num in nums:
        # Create a copy to avoid modifying during iteration
        current_sums = set(dp)
        
        for current_sum in current_sums:
            new_sum = current_sum + num
            
            # Check if we've found a subset that matches target
            if new_sum == target_sum:
                return True
            
            # Add new subset sum if within target
            if new_sum < target_sum:
                dp.add(new_sum)
    
    return False