from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class DSU :
    def __init__(self , n) :
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
        else :
            self.parent[root_x] = root_y
        
        return True



class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        graph = defaultdict(list)
        parent = defaultdict(int)
        indegree = [0]*(n+1)
        dsu = DSU(n+1)

        temp1 = temp2 = None
        for u,v in edges :

            if parent[v] :
                temp1 = [parent[v] , v]
                temp2 = [u,v]
                break
            

            graph[u].append(v)
            parent[v] = u
            indegree[v] += 1
        
        for u , v in edges :
            if [u,v] == temp2 :
                continue
            if not dsu.union(u,v) :
                return temp1 if temp1 else [u,v]
        
        return temp2


        

        # mini = float("inf")
        # root = -1
        # for i , val in enumerate(indegree) :
        #     if mini > val :
        #         mini = val
        #         root = i
        
        # # we got the root
        # queue = deque([root])

        # while queue :
        #     curr_node = queue.popleft()
        #     for neighbour in graph[curr_node] :
        #         if neighbour not in parent[curr_node] :
        #             indegree[neighbour] -= 1
        #             if indegree[neighbour] == 0 :
        #                 queue.append(neighbour)
        
        



        # dsu = DSU(n)
        # ans = -1
        # for i , (u , v) in enumerate(edges) :
        #     if not dsu.union(u,v) :
        #         ans = i
        
        # return edges[ans]