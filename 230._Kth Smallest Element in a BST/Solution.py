# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        queue = []
        queue.append(root)
        all_nodes = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            all_nodes.append(current_node.val)
            queue.add(current_node.left)
            queue.add(current_node.right)
        
        return all_nodes.sort()[k -1]


        