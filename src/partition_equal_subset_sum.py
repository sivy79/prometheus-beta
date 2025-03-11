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
    
    # Require at least two elements
    if len(nums) < 2:
        return False
    
    # Immediate false for impossible small sums
    if max(nums) > target_sum:
        return False
    
    # Dynamic programming solution
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target_sum]