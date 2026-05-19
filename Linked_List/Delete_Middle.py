# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Now, slow is at the middle node
        prev.next = slow.next  # Remove the middle node 
        return head

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
new_head = solution.deleteMiddle(head)
# Printing the modified linked list
curr = new_head
while curr:
    print(curr.val)  # Output should be 1 -> 2 -> 4 -> 5
    curr = curr.next
print("End of list")