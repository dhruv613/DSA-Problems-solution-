# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last = head
        l = 0

        while last and last.next:
            last = last.next
            l += 1
        l += 1

        if l == 0:
            return head
        k = k % l
        if k == 0:
            return head  

        last.next = head
        for _ in range(l - k):
            last = last.next
        new_head = last.next
        last.next = None
        return new_head