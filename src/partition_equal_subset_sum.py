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
    
    # Dynamic programming solution
    possible_sums = {0}
    for num in nums:
        new_sums = set()
        for s in possible_sums:
            new_sum = s + num
            if new_sum == target_sum:
                return True
            if new_sum < target_sum:
                new_sums.add(new_sum)
        possible_sums.update(new_sums)
    
    return False