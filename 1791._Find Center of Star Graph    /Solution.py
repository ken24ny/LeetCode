class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = []

        queue.append(cloned)
       
        while len(queue) > 0:
             node = queue.pop()
             
             if node.val == target.val:
                 return node
                 
             else:
                 if node.left is not None:
                    queue.append(node.left)
                    
                 if node.right is not None:
                    queue.append(node.right)            