from typing import List

class Solution:
    def lower_bound(self, nums, target, l, h):
        if h is None:
            h = len(nums)
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        return l # This index is the lower bound

    def upper_bound(self, nums, target, l, h):
        if h is None:
            h = len(nums)
        while l < h:
            mid = (l + h) // 2
            if nums[mid] > target:
                h = mid  # Look in the left half
            else:
                l = mid + 1  # Look in the right half
                
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target, 0, len(nums))
        ub = self.upper_bound(nums, target, 0, len(nums))
        if lb == ub:
            return [-1, -1]
        return [lb, ub - 1]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
print(solution.searchRange(nums, target))  # Output: [3, 4]