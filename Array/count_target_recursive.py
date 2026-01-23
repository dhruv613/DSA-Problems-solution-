def count_target_recursive(arr, target):
    """
    Counts the occurrences of target in a nested array using recursion.

    Parameters:
    arr (list): The nested array to search.
    target: The value to count.

    Returns:
    int: The count of occurrences of target in arr.
    """
    if len(arr) == 0:
        return 0
    else:
        first, rest = arr[0], arr[1:]
        count = 0
        if isinstance(first, list):
            count += count_target_recursive(first, target)
        elif first == target:
            count += 1
        count += count_target_recursive(rest, target)
    return count    

