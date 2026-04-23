def findmedian(nums1, nums2):
    m = sorted(nums1 + nums2)
    n = len(m)

    if n % 2 == 0:
        return (m[n//2 - 1] + m[n//2]) / 2

    else:
        return m[n//2]



nums1 = [1, 2]
nums2 = [3, 4]
print(findmedian(nums1, nums2))