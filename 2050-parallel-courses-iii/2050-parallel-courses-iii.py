from collections import defaultdict , deque
import heapq

from functools import lru_cache

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        indegree = [0]*(n)


        for u,v in relations :
            u -= 1
            v -= 1
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([])
        max_time = [0]*(n)

        for node in range(n) :
            if indegree[node] == 0 :
                queue.append(node)
                max_time[node] = time[node]
        
        ans = 0
        while queue :
            curr_node = queue.popleft()

            for neighbour in graph[curr_node] :
                max_time[neighbour] = max(max_time[neighbour]  , max_time[curr_node] + time[neighbour])
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0 :
                    queue.append(neighbour)
        
        return max(max_time)

