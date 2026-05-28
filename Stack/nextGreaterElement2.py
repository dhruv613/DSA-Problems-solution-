from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        res = [-1] * n
        st = []  # monotonic decreasing stack (stores values)

        for i in range(2 * n - 1, -1, -1):
            idx = i % n
            while st and st[-1] <= nums[idx]:
                st.pop()
            if st:
                res[idx] = st[-1]
            st.append(nums[idx])

        return res

# Example usage:
nums = [1, 2, 1]
sol = Solution()
print(sol.nextGreaterElements(nums))  # Output: [2, -1, 2]
