from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        n = len(edges)
        indegree = [0]*(n)
        graph = defaultdict(list)

        for u in range(n) :
            if edges[u] != -1 :
                graph[u].append(edges[u])
                indegree[edges[u]] += 1
        
        queue = deque([])
        for i in range(n) :
            if indegree[i] == 0 :
                queue.append(i)
        
        while queue :
            curr_node = queue.popleft()
            neighbour = edges[curr_node]
            if neighbour != -1 :
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0 :
                    queue.append(neighbour)
        
        max_cycle_length = -1
        visited = [False]*(n)

        for i in range(n) :

            if indegree[i] > 0 and not visited[i] :
                cycle_length = 0
                curr = i

                while not visited[curr] :
                    visited[curr] = True
                    cycle_length += 1
                    curr = edges[curr]
                
                max_cycle_length = max(max_cycle_length , cycle_length)

        return max_cycle_length