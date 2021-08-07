#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # counter = []
    # depth = 0

    # def helloworld(self):
    #     print(Solution.depth)  

    
    # def test(self):  
    #     i = 
    #     while i < 5:
    #         Solution.counter.insert(i,[i])
    #         i += 1

    #     print(Solution.counter)

    def deepestLeavesSum(self,root):
        queue = []
        queue.append(root)
        result = 0
        while len(queue) > 0:
            size = len(queue)
            result = 0
            for i in range(0,size):
                
                node = queue.pop(0)
                result += node.val
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
        
        print(result)
        return result

        



    # def deepestLeavesSum(self, root):  
    #     print(Solution.depth)
    #     Solution.counter.insert(Solution.depth,Solution.counter[Solution.depth].append[root.val])
    #     Solution.depth += 1
        
        
    #     if root.left != None:
    #         self.deepestLeavesSum(root.left)
            
    #     if root.right!= None:
    #         self.deepestLeavesSum(root.right)
            
    #     print(Solution.counter)


tn1 = TreeNode(7,None,None)
tn2 = TreeNode(8,None,None)
tn3 = TreeNode(4,tn1,None)
tn4 = TreeNode(5,None,None)
tn5 = TreeNode(6,None,tn2)
tn6 = TreeNode(2,tn3,tn4)
tn7 = TreeNode(3,None,tn5)
tn8 = TreeNode(1,tn6,tn7)
Solution().deepestLeavesSum(root = tn8)
#Solution().test()
