def sum_arr_iter(arr):
    """Returns the sum of all elements in an array using iteration.

    Args:
        arr (list): A list of numbers.
    Returns:
        float: The sum of all elements in the array.
    """
    total = 0
    for num in arr:
        total += num
    return total

print(sum_arr_iter([1, 2, 3, 4]))  # Example usage, should return 10