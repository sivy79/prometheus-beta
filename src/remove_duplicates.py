def remove_duplicates(input_string):
    """
    Remove duplicate characters from a given string while preserving the original order.

    Args:
        input_string (str): The input string from which duplicates should be removed.

    Returns:
        str: A string with duplicate characters removed, keeping the first occurrence of each character.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> remove_duplicates("hello")
        'helo'
        >>> remove_duplicates("aabbcc")
        'abc'
        >>> remove_duplicates("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Use an ordered set to preserve character order while removing duplicates
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)