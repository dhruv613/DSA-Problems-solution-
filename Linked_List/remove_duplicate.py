# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            # Move curr until the end of duplicates
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            # If prev's next is still curr, it means there were no duplicates
            if prev.next == curr:
                prev = prev.next  # Move prev to the next node
            else:
                prev.next = curr.next  # Skip all duplicates
            curr = curr.next  # Move to the next node

        return dummy.next  # Return the head of the modified list

# Example usage:
# Creating a linked list: 1 -> 1 -> 2 -> 3 
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
solution = Solution()
new_head = solution.deleteDuplicates(head)
# Printing the modified linked list
curr = new_head
while curr:
    print(curr.val)  # Output should be 2 -> 3
    curr = curr.next
print("End of list")
