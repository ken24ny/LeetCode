#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
    
#         queue1 = []
#         queue2 = []
#         result = []
#         queue1.append(root1)
#         queue2.append(root2)
#         if root1 is None:
#             return root2
#         if root2 is None:
#             return root1    
#         while len(queue1) > 0 or len(queue2) > 0:
#             node1 = queue1.pop()
#             node2 = queue2.pop()
#             if node1 is None:
#                 result.append(node2)
#             if node1 is None:
#                 result.append(node1) 
            
#             else:
#                 sum_node = TreeNode(node1.val + node2.val, None,None)
#             result.append(sum_node)
#             queue1.append(node1.left)
#             queue1.append(node1.right)
#             queue2.append(node1.left)
#             queue2.append(node1.right)
        
#         return result


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            if root1 and root2:
                sum = root1.val + root2.val
                sum_node = (sum,None,None)
                sum.left = self.mergeTrees(root1.left,root2.left)
                sum.right = self.mergeTrees(root1.right,root2.right)
        
        return sum_node

    