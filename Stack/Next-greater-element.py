class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        arr = {}
        for i in range(len(nums2)-1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            # if the stack is not empty, then the top element is the next greater element for nums2[i]
            if st:
                arr[nums2[i]] = st[-1]
            # if the stack is empty, then there is no greater element for nums2[i]
            else:
                arr[nums2[i]] = -1
            # push the current element to the stack
            st.append(nums2[i])
        
        # for each element in nums1, get the next greater element from the arr dictionary
        return [arr[num] for num in nums1]
        