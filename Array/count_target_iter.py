def ccount_target_iter(arr, target):
    count = 0
    for item in arr:
        if item == target:
            count += 1
        elif isinstance(item, list):
            count += ccount_target_iter(item, target)   
    return count
    """
    Counts the occurrences of target in a nested array using iteration.
    Parameters: 
    arr (list): The nested array to search.
    target: The value to count.
    Returns:
    int: The count of occurrences of target in arr.
    """
    