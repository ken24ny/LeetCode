class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = []
        size = len(edges)
        for i in range(0,size):
            if(edges[i][0] in result):
                return edges[i][0]
            #result.append(edges[i][0])
            if(edges[i][1] in result):
                return edges[i][1]

            result.extend([edges[i][0],edges[i][1]])
            #result.append(edges[i][1])

# Can (2,1) and (1,2) both exist?