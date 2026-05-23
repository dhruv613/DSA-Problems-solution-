# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenthA, lenthB = 0, 0

        currA = headA
        currB = headB
        while currA or currB:
            if currA:
                lenthA += 1
                currA = currA.next
            if currB:
                lenthB += 1
                currB = currB.next

        # Determine the longer and shorter list
        if lenthA > lenthB:
            longer, shorter = headA, headB
            diff = lenthA - lenthB
            print(diff)
        else:
            longer, shorter = headB, headA
            diff = lenthB - lenthA
            print(diff)

        # Advance the pointer of the longer list by the difference in lengths
        for _ in range(diff):
            longer = longer.next

        # Move both pointers until they meet at the intersection
        while longer and shorter:
            if longer == shorter:
                return longer  # Intersection found
            longer = longer.next
            shorter = shorter.next

        return None  # No intersection found
# Example usage:
# Create two linked lists that intersect
# List A: 1 -> 2 -> 3
# List B: 4 -> 5 -> 3 (intersects at node with value 3)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node6.next = node5  # Continue the list after intersection
node5.next = node2  # Intersection at node3
solution = Solution()
intersection_node = solution.getIntersectionNode(node1, node4)
if intersection_node:
    print(f"Intersection at node with value: {intersection_node.val}")
else:
    print("No intersection found.")
