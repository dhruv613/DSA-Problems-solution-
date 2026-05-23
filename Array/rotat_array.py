class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time: O(n), Space: O(1)
        """
        n = len(nums)
        if n <= 1:
            return  # No rotation needed for arrays of size 0 or 1
        
        k = k % n  # Handle cases where k is greater than n
        if k == 0:
            return  # No rotation needed if k is a multiple of n
        
        # Helper function to reverse a portion of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse entire array, then first k, then remaining elements
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)
print(nums)  # Output should be [5, 6, 7, 1, 2, 3, 4]