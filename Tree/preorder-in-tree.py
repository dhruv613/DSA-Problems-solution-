# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.stack = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #using stack

        if not root:
            return []
        
        self.stack = [root] # add root to stack
        self.result = [] #take result list to store the result
        while self.stack: # while stack is not empty
            node = self.stack.pop()  # pop the last element from stack and store it in node variable
            self.result.append(node.val) # add the node in result list
            if node.right:  # if right child of node is not null then add it to stack
                self.stack.append(node.right)
            if node.left:   # if left child of node is not null then add it to stack
                self.stack.append(node.left)
        return self.result 