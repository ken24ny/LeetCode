from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        answer = []
        track = 0
        if nums == []:
            return []
        else:
            for number in nums:
                track += number
                answer.append(track)
        
        return answer


     
            


