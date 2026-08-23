from collections import defaultdict ,deque ,Counter
import heapq
from functools import lru_cache

class DSU :

    def __init__(self , n):
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.comp = n
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self , a , b):
        root_a , root_b = self.find(a) , self.find(b)

        if root_a == root_b :
            return False
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:


        ans = [False]*(len(queries))

        dsu = DSU(n)

        for indx , q in enumerate(queries) :
            queries[indx].append(indx)
        
        edgeList.sort(key = lambda x : x[2])
        queries.sort( key = lambda x : x[2])
        graph = defaultdict(list)
        # seen = set()
        # for u , v , wt in edgeList :
        #     # since edgelist sorted take the first minimum one only
        #     if (u,v) in seen or (v,u) in seen :
        #         continue
        #     seen.add((u,v))
        #     graph[u].append((v,wt))
        #     graph[v].append((u,wt))
        
        i = 0
        for start , end , limit , indx in queries :

            while i < len(edgeList) and edgeList[i][2] < limit :
                dsu.union(edgeList[i][0] , edgeList[i][1])
                i += 1
            
            if dsu.find(start) == dsu.find(end) :
                ans[indx] = True
            
        
        return ans




        
        # print(edgeList)