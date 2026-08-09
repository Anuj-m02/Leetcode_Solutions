from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:

        diff = []
        for s,t in zip(start , target) :
            if s != t :
                diff.append(1)
            else :
                diff.append(0)
        
        # parity always changes in +2 , 0 ,-2
        if sum(diff) % 2 != 0 :
            return [-1]

        graph = defaultdict(list)
        degree = [0]*(n)

        for i , (u,v) in enumerate(edges) :
            graph[u].append((v,i))
            graph[v].append((u,i))
            degree[v] += 1
            degree[u] += 1
        
        queue = deque([])
        for node in range(n) :
            if degree[node] == 1 :
                queue.append(node)
            
        ans = []

        while queue :
            curr_node = queue.popleft()

            if not graph[curr_node] :
                continue
            
            parent , edge_indx = graph[curr_node].pop()
            graph[parent].remove((curr_node , edge_indx))

            if diff[curr_node] == 1 :
                ans.append(edge_indx)
                diff[curr_node] =  1-diff[curr_node]
                diff[parent] =  1-diff[parent]
            
            degree[parent] -= 1
            if degree[parent] == 1 :
                queue.append(parent)
        
        if any(d == 1 for d in diff) :
            return [-1]
        
        ans.sort()
        return ans

        