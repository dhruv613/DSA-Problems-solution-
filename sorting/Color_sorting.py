#sort an array using counting sort

def sortColors(nums):
    minnum = min(nums)
    maxinum = max(nums)
    # count the frequency of each number in the array
    count = [0]*(maxinum - minnum + 1)

    for num in nums:
        count[num - minnum] += 1 

    sorted_index = 0

    for i in range(len(count)):
        while count[i] > 0:
            nums[sorted_index] = i + minnum
            sorted_index += 1
            count[i] -= 1
    return nums

arr = [2,0,2,1,1,0]

print("Sorted-1 array is:", sortColors(arr))


# Sorting with conditions and while loop 

def sortColors(nums):
    left = 0
    right = len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        else:
            i += 1

    return nums

arr = [2,0,2,1,1,0]
print("Sorted-2 array is:", sortColors(arr))