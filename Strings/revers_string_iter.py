def revers_string_iter(s):
    """Reverse a given string s using iteration.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

