# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If the node is a leaf node, return 1
        if not root.left and not root.right:
            return 1
        
        # If the left subtree is None, recursively find the depth of the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If the right subtree is None, recursively find the depth of the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both subtrees are present, return the minimum of the two depths plus one for the current node
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 