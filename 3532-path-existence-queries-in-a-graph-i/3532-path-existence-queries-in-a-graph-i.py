from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        

        parent = list(range(n+1))
        size = [1]*(n)

        def find(node) :
            if parent[node] != node :
                parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(x,y) :
            xr , yr = find(x) , find(y)
            if xr == yr :
                return
            
            if size[xr] > size[yr] :
                parent[yr] = xr
                size[xr] += size[yr]
            
            else :
                parent[xr] = yr
                size[yr] += xr
        
        m = len(queries)
        ans = [False]*(m)

        


        graph = defaultdict(list)
        for i in range(n-1):
            if abs(nums[i]-nums[i+1]) <= maxDiff :
                union(i,i+1)
                graph[i].append(i+1)
                graph[i+1].append(i)

        for i , (u , v) in enumerate(queries) :

            ur , vr = find(u) , find(v)

            if ur == vr :
                ans[i] = True
        
        return ans

