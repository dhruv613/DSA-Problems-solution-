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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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
                
                # Enqueue left and right children if they exist
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            
            result.append(level_nodes)  # Add the current level's values to the result
        return result


# Example usage:
#[1, 2, 3, 4]
print(Solution().levelOrder(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))  # Output: [[1], [2, 3], [4]]