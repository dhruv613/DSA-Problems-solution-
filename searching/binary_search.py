def Binary_search(nums, target):
    """
    Perform a binary search for the target in the given sorted array.
    Parameters:
    nums (list): The sorted list to search through.
    target: The value to search for.
    Returns:
    int: The index of the target if found, otherwise -1.
    """
    l = 0
    r = len(nums) - 1    

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1


# Example usage:    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5  
result = Binary_search(nums, target)
print(f"Target {target} found at index: {result}")  # Output: Target 5 found at index: 4