# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate the length of the linked list
        l = 0
        current = head
        while current:
            l += 1
            current = current.next

        # If n is equal to the length of the list, remove the first node
        if n == l:
            return head.next

        # Traverse to the node just before the one to be removed
        current = head
        for _ in range(l - n - 1):
            current = current.next

        # Remove the nth node from the end
        current.next = current.next.next

        return head
    
example = ListNode(1)
example.next = ListNode(2)
example.next.next = ListNode(3)
example.next.next.next = ListNode(4)
example.next.next.next.next = ListNode(5)
result = Solution().removeNthFromEnd(example, 2)
# Print the resulting linked list
current = result
while current:
    print(current.val)  # Output: 1 -> 2 -> 3 -> 5
    current = current.next