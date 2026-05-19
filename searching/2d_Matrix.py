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


#There Was an another solution with linear scan , but O(m*n) it scan the array with any type 


"""
for row in matrix:
    if target in row:
        return True
    return False 

"""

# Is the array is an sorted But use Binary search Then ... 

"""   
flat = sorted(x for row in matrix for x in row)
l = 0
r = len(flat)

while l <= r:
    mid = (l+r)//2

    if flat[mid] == target:
        return True
    elif flat[mid] > target:
        r = mid-1

    else:
        l = mid+1

return False

"""