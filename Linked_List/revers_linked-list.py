# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev  # Reverse the current node's pointer
            prev = curr  # Move prev to the current node
            curr = next_node  # Move to the next node
        return prev  # Return the new head of the reversed list

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
new_head = solution.reverseList(head)
# Printing the reversed linked list
curr = new_head
while curr:
    print(curr.val)  # Output should be 5 -> 4 -> 3 -> 2 -> 1
    curr = curr.next
print("End of list")