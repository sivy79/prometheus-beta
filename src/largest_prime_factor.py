def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.

    Args:
        n (int): A large positive integer to factorize.

    Returns:
        int: The largest prime factor of n.

    Raises:
        ValueError: If input is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be greater than or equal to 2")

    # Initialize the largest prime factor
    largest_prime_factor = 1

    # First, handle divisibility by 2
    while n % 2 == 0:
        largest_prime_factor = 2
        n = n // 2

    # Then check odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_prime_factor = factor
            n = n // factor
        factor += 2

    # If n is still greater than 2, it means n itself is prime
    if n > 2:
        largest_prime_factor = n

    return largest_prime_factor