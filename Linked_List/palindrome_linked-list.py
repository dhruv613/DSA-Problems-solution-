# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # Find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        # Compare the first half and the reversed second half
        left = head
        right = prev
        while right:  # Only need to compare until the end of the shorter half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True  # If all values matched, it's a palindrome
        

# Example usage:
# Creating a linked list: 1 -> 2 -> 2 -> 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
solution = Solution()
print(solution.isPalindrome(head))  # Output should be True
# Creating a linked list: 1 -> 2 -> 3
head2 = ListNode(1)
head2.next = ListNode(2)
print(solution.isPalindrome(head2))  # Output should be False
