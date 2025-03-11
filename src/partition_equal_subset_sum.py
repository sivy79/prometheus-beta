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
    
    # Create a dynamic programming table
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    # Iterate through each number in the input list
    for num in nums:
        # We go backwards to avoid using the same number multiple times
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target_sum]