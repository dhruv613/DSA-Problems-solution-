# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = True

    def Depth(self, root: TreeNode) -> int:
        # Base case: if the tree is empty, depth is 0
        if not root:
            return 0
        
        # Recursively find the depth of each subtree
        left_depth = self.Depth(root.left)
        right_depth = self.Depth(root.right)

        if abs(left_depth - right_depth) > 1:
            self.ans = False

        return max(left_depth, right_depth) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
\
        self.Depth(root)
        return self.ans


# Example usage:
# Constructing a balanced binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left = TreeNode(5)
root.left.left = TreeNode(7)
solution = Solution()
print(solution.isBalanced(root))  # Output: 