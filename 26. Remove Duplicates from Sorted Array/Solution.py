from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i + 1

        while j < len(nums):
            el1 = nums[i]
            el2 = nums[j]
            if el1 == el2:
                nums.remove(el1)

            else:
                i += 1
                j += 1

        return len(nums)


