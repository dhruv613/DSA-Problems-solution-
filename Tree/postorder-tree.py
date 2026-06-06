# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.postorder(root)
        return self.ans