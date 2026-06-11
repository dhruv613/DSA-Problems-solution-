# Definition for singly-linked list.
from platform import node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# The problem is to delete a node in a singly linked list, given only access to that node.
# The solution is to copy the value of the next node to the current node, and then delete the next node by changing the next pointer of the current node to skip the next node. This effectively removes the next node from the linked list, while keeping the current node in place with its new value.
node = ListNode(4)
example = ListNode(4)
example.next = ListNode(5)
example.next.next = ListNode(1)
example.next.next.next = ListNode(9)
Solution().deleteNode(example.next)
print(example.next.val) # Output: 1