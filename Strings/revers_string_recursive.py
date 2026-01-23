def revers_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + revers_string_recursive(s[:-1])
    """Reverse a given string s using recursion.    
    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """