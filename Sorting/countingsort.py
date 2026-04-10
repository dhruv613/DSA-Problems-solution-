def CountingSort(nums):
    if not nums:
        return nums
    n = len(nums)
    mx = max(nums)
    freq = [0]*(mx+1)

    for i in nums:
        freq[i]+=1

    nums = []
    for i in range(0, mx+1):
        while freq[i]>0:
            nums.append(i)
            freq[i]-=1

    return nums

if __name__ == "__main__":
    nums = [4, 2, 2, 8, 3, 3, 1]
    print(CountingSort(nums))