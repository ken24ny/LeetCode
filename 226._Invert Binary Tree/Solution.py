# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root is None:
            return None
    
        temp_left  = root.left
        root.left = root.right
        root.right = temp_left

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        
        return root