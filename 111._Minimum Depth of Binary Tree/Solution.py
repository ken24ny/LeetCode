# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isLeaf(self, root: TreeNode):
        if(root.left is None and root.right is None):
            return True
        else:
            return False

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            if self.minDepth(root.left) == 0 or self.minDepth(root.right) == 0:
                return 1 + max(self.minDepth(root.left),self.minDepth(root.right))
            
            else:
                return 1 + min(self.minDepth(root.left),self.minDepth(root.right))





                    


sol = Solution()
tn1 = TreeNode(9,None,None)
tn2 = TreeNode(15,None,None)
tn3 = TreeNode(7,None,None)
tn4 = TreeNode(20,tn2,tn3)
tn5 = TreeNode(3,tn1,tn4)
#print(sol.isLeaf(tn1))
print(sol.minDepth(tn5))