
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    
    def maxDepth(self, root: 'Node') -> int:
        depth = 0

        if root is None:
            return 0
        
        queue = []
        queue.append(root)

        while len(queue) > 0:

            for i in range(0,len(queue)):
                current_node = queue.pop(0)
                if current_node.children:
                    for child in current_node.children:
                        queue.append(child)
            depth += 1
              
        
        return depth

            
            
            


        

        