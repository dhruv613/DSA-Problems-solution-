def sum_arr(arr):
    """Returns the sum of all elements in an array using recursion.

    Args:
        arr (list): A list of numbers.  
    Returns:
        float: The sum of all elements in the array.
    """
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_arr(arr[1:])
        