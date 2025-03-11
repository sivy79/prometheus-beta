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
    
    # Dynamic programming: used a set for more memory-efficient tracking
    possible_sums = {0}
    
    for num in nums:
        # Create a new set to avoid modifying the set during iteration
        current_sums = possible_sums.copy()
        for current_sum in current_sums:
            new_sum = current_sum + num
            if new_sum == target_sum:
                return True
            if new_sum < target_sum:
                possible_sums.add(new_sum)
    
    return False