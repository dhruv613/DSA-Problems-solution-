# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # Skip the duplicate node
            else:
                curr = curr.next  # Move to the next node\


# Example usage:    
# Creating a linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
solution = Solution()
new_head = solution.deleteDuplicates(head)
# Printing the modified linked list
curr = new_head
while curr:
    print(curr.val)  # Output should be 1 -> 2 -> 3
    curr = curr.next
print("End of list")    
