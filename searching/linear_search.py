def linear_search(arr, target):
    """
    Perform a linear search for the target in the given array.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1   

# Example usage:
arr = [5, 3, 2, 8, 1]
target = 2
result = linear_search(arr, target)
print(f"Target {target} found at index: {result}")  # Output: Target 2 found at index: 2