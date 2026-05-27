# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next



# Example usage:
# Create two linked lists: 2 -> 4 -> 3 and 5 -> 6 -> 4
node1 = ListNode(2) 
node2 = ListNode(4)
node3 = ListNode(3) 
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6  
solution = Solution()   
result = solution.addTwoNumbers(node1, node4)
# Print the result (should represent the linked list 7 -> 0 -> 8)
while result:
    print(result.val, end="," if result.next else "")
    result = result.next
