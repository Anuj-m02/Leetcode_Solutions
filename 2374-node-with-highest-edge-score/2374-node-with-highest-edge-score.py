from collections import defaultdict , deque , Counter

class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        n = len(edges)
        graph = defaultdict(list)

        ans = [0]*(n)

        for i in range(n) :
            # i -> edge[i]
            ans[edges[i]] += i
        
        maxi , maxi_indx = -1 , -1
        for i in range(n) :
            if ans[i] > maxi :
                maxi = ans[i]
                maxi_indx = i
        
        return maxi_indx