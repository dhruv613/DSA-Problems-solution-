# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return None

        curr = root
        if curr.val == val:
            if curr.left==None and curr.right==None:
                return None                              # if the node to be deleted is a leaf node, simply return None
            elif curr.left!=None and curr.right==None:
                return curr.left                         # if the node to be deleted has only a left child, return the left child to replace the node
            elif curr.left==None and curr.right!=None:
                return curr.right                        # if the node to be deleted has only a right child, return the right child to replace the node
            else:
                temp = curr.right                        # if the node to be deleted has two children, find the minimum value in the right subtree (the leftmost node in the right subtree) and replace the value of the node to be deleted with that minimum value, then delete the minimum value node from the right subtree
                while temp.left!=None:
                    temp = temp.left
                temp.left = curr.left
                return curr.right
        elif curr.val > val:
            curr.left = self.deleteNode(curr.left, val)   # if the value to be deleted is less than the value of the current node, recursively call the deleteNode function on the left subtree
        else:
            curr.right = self.deleteNode(curr.right, val) # if the value to be deleted is greater than the value of the current node, recursively call the deleteNode function on the right subtree
        return curr