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

print("Sorted array is:", sortColors(arr))