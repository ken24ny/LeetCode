class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(0,size + 1):
            if i not in nums:
                return i