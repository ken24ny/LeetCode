#Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base
        if root is None:
            return 0
        else:
            
            depth = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        return depth
            

# tests
sol = Solution()
# when root is null
print(sol.maxDepth(None))

# when root is null
tn1 = TreeNode(15,None,None)
tn2 = TreeNode(7,None,None)  
tn3 = TreeNode(9,None,None)  
tn4 = TreeNode(20,tn1,tn2) 
tn5 = TreeNode(20,tn3,tn4) 

print(sol.maxDepth(tn5))