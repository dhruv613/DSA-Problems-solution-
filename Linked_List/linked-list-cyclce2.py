# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        while curr and curr.next:
            if curr.val == "visited":
                return curr
            curr.val = "visited"
            curr = curr.next
        return None 