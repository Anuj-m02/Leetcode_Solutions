import heapq
from collections import defaultdict , deque

class Solution:
    def maximumInvitations(self, favourite: List[int]) -> int:
        n = len(favourite)

        graph = defaultdict(list)
        indegree = [0]*(n)

        for i in range(n):
            graph[i].append(favourite[i])
            indegree[favourite[i]] += 1

        depth = [0]*(n)
        queue = deque([]) 

        for i in range(n) :
            if indegree[i] == 0 :
                queue.append(i)
        
        while queue :
            u = queue.popleft()
            neighbour = favourite[u]
            depth[neighbour] = max(depth[neighbour] , depth[u] + 1)
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0 :
                queue.append(neighbour)
        
        max_cycle = 0
        total_2_cycles = 0
        visited = [False]*(n)

        for node in range(n):

            if indegree[node] > 0 and not visited[node] :
                cycle_len = 0
                curr = node
                while not visited[curr] :
                    visited[curr] = True
                    cycle_len += 1
                    curr = favourite[curr]
                
                if cycle_len == 2 :
                    u , v = node , favourite[node]

                    total_2_cycles += (depth[u] + 1) + (depth[v]+1)
                
                else :
                    max_cycle = max(max_cycle , cycle_len )
        
        return max(max_cycle , total_2_cycles)
