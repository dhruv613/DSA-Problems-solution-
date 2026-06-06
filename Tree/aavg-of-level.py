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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        queue = Queue()
        queue.enqueue(root) 
        while not queue.is_empty():
            level_size = len(queue.items)  # Get the number of nodes at the current level
            level_nodes = []  # List to store the values of nodes at the current level
             
            for _ in range(level_size):
                node = queue.dequeue()  # Dequeue a node from the queue
                
                level_nodes.append(node.val)  # Add its value to the level list
                # Calculate the average for the current level and add it to the result

                # Enqueue left and right children if they exist
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            
             
            result.append(sum(level_nodes) / len(level_nodes))  # Add the current level's average to the result
        return result
