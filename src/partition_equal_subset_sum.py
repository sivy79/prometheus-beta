def can_partition(nums):
    """
    Determine if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (List[int]): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(n * total_sum)
    Space Complexity: O(n * total_sum)
    
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
    
    # Memoization dictionary to cache sub-problem results
    memo = {}
    
    def backtrack(index, current_sum):
        # Base cases
        if current_sum == 0:
            return True
        if index >= len(nums) or current_sum < 0:
            return False
        
        # Check memoized results
        key = (index, current_sum)
        if key in memo:
            return memo[key]
        
        # Try including or excluding current number
        result = (
            backtrack(index + 1, current_sum - nums[index]) or  # Include current number
            backtrack(index + 1, current_sum)  # Exclude current number
        )
        
        # Memoize and return result
        memo[key] = result
        return result
    
    return backtrack(0, target_sum)