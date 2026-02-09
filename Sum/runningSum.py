def runningSum(nums):
    n = len(nums)
    ans = []
    ans.append(nums[0])
    for i in range(1, n):
        sums = ans[i-1] + nums[i]
        ans.append(sums)
    return ans

nums = [1,2,3,4]
print(runningSum(nums))
