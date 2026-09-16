from collections import defaultdict , deque 
import heapq
from functools import lru_cache


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        visited = [0]*(n)
        disc = [float("inf")]*n
        low = [float("inf")]*n

        graph = defaultdict(list)
        ans = []

        for u,v in connections :
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node , parent , time) :
            visited[node] = 1
            time += 1
            disc[node] = time
            low[node] = time

            for neighbour in graph[node] :
                if not visited[neighbour] :
                    dfs(neighbour , node , time)
                    low[node] = min(low[node]  , low[neighbour])
                    if low[neighbour] > disc[node] :
                        ans.append((node , neighbour))
                
                elif neighbour != parent :
                    low[node] = min(low[node] , disc[neighbour])
                else :
                    continue
        
        dfs(0 , None , 0)
        return ans