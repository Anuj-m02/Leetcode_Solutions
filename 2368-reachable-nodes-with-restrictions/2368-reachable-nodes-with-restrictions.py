from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        graph = defaultdict(list)
        restricted = set(restricted)
        for u , v in edges :
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([0])
        vis = set()
        vis.add(0)
        cnt = 0

        while queue :
            curr_node = queue.popleft()
            cnt += 1

            for neighbour in graph[curr_node] :
                if neighbour not in restricted and neighbour not in vis:
                    queue.append(neighbour)
                    vis.add(neighbour)
            
        return cnt