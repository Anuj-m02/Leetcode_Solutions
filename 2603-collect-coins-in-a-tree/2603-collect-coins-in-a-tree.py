from collections import defaultdict, deque
import heapq
from functools import lru_cache

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        
        n = len(coins)
        graph = defaultdict(list)
        degree = [0]*(n)

        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        
        queue = deque([])
        for node in range(n):
            if degree[node] == 1 and coins[node] == 0 :
                queue.append(node)
        
        while queue :
            node = queue.popleft()
            degree[node] = 0

            for neighbour in graph[node] :
                if degree[neighbour] == 0 :
                    continue
                degree[neighbour] -= 1
                if degree[neighbour] == 1 and coins[neighbour] == 0 :
                    queue.append(neighbour)

        queue = deque([]) 

        for node in range(n):
            if degree[node] == 1 :
                queue.append(node)
        
        # all leaf node and one iteration for there parent
        for _ in range(2) :
            size = len(queue)
            for _ in range(size) :
                node = queue.popleft()
                degree[node] = 0

                for neighbour in graph[node] :
                    if degree[neighbour] == 0 :
                        continue
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1 :
                        queue.append(neighbour)
        rem_edge = 0

        for u,v in edges :
            if degree[u] > 0 and degree[v] > 0 :
                rem_edge += 1
        
        return rem_edge*2




