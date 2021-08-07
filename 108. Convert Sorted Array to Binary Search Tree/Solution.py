# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        result = TreeNode()

        if len(nums) == 0:
            result = None
            return result
        if len(nums) == 1:
            result.val = nums[0]
            return result       

        mid =  math.floor(len(nums) / 2)
        end = len(nums)
        left = nums[0:mid]
        right = nums[mid + 1:end]
        left_tree = self.sortedArrayToBST(left)
        right_tree = self.sortedArrayToBST(right)

        result.val = nums[mid]
        result.left = left_tree
        result.right = right_tree

        return result

