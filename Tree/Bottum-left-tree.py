class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = Queue()
        queue.enqueue(root) 
        bottom_left_value = root.val  # Initialize with the root value
        
        while not queue.is_empty():
            level_size = len(queue.items)  # Get the number of nodes at the current level
            
            for i in range(level_size):
                node = queue.dequeue()

                # Update the bottom left value for the first node of each level
                if i == 0:
                    bottom_left_value = node.val

                # Enqueue left and right children if they exist
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        return bottom_left_value
        
