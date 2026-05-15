class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows*cols - 1

        while l <= r:

            mid = (l+r)//2

            if matrix[mid//cols][mid%cols] == target:
                return True

            elif matrix[mid//cols][mid%cols] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False
    

# Example usage:

matrix = [[3, 1, 4],
          [2, 7, 5],
          [9, 6, 8]]
target = 6
solution = Solution()
result = solution.searchMatrix(matrix, target)
print(f"Target {target} found in matrix: {result}")  # Output: Target 3 found in matrix: True