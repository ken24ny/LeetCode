from typing import List
class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # find unique elements in the groupSize array
        # create the dictionary 
        # divide and create the result
        result = []
        uniqueset = set(groupSizes)
        uniquelist = list(uniqueset)
        mydict = {}
        for i in range(0,len(uniquelist)):
            mydict.update({uniquelist[i]: []})
        
        for i in range(0,len(groupSizes)):
            for key in mydict:
                if key == groupSizes[i]:
                    mydict[key].append(i)
        
        print(mydict)
                    

        for key in mydict:
            if len(mydict[key]) > key:
                groupsize = int(len(mydict[key]) / key)
                eachgroup = []
                i = 0
                for j in range(0,groupsize):
                    eachgroup = []
                    while len(eachgroup) < key:
                        eachgroup.append(mydict[key][i])
                        i = i+1           
                    
                    result.append(eachgroup)

            else:
                result.append(mydict[key])

        return result


sol = Solution()
#print(sol.groupThePeople([3,3,3,3,3,1,3]))  # -->   [[5],[0,1,2],[3,4,6]]
#print(sol.groupThePeople([2,1,3,3,3,2]))
#print(sol.groupThePeople([2,2,1,1,1,1,1,1]))

#print(set([1,2,2,3,4,5,5]))

