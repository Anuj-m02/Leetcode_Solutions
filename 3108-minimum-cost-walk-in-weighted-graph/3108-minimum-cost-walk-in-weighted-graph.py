from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class DSU :
    def __init__(self , n) :
        self.n = n
        self.parent = list(range(n))
        self.size = [1]*(n)
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self , x , y) :
        root_x , root_y = self.find(x) , self.find(y)

        if root_x == root_y :
            return False
        
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        return True


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        

        # bitwise and always decrrease or remain same never increase
        dsu = DSU(n)
        comp_wt = defaultdict(lambda : -1)
        for u , v , wt in edges :
            dsu.union(u,v)
        
        for u,v,wt in edges :
            comp_id = dsu.find(u)
            curr_wt = comp_wt[comp_id]
            comp_wt[comp_id] = wt & curr_wt
        
        ans = []
        for u,v in query :
            if u == v :
                ans.append(0)
                continue

            root_u , root_v = dsu.find(u) , dsu.find(v)

            if root_u != root_v :
                ans.append(-1)
            
            else :
                ans.append(comp_wt[root_u])
        
        return ans




