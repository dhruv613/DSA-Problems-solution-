class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1 

        while l <= h:
            mid = (l + h) // 2    

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return l

# Example usage:
nums = [1, 3, 5, 6] 
target = 2
solution = Solution()
print(solution.searchInsert(nums, target))  # Output: 2