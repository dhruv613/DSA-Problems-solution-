def twoSums(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
                
nums = [1,2,4,5,6,7]
target = 9
print(twoSums(nums, target))