from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        

        graph = defaultdict(list)
        for indx in range(n-1) :
            graph[indx].append(indx+1)
            # graph[indx+1].append(indx)
        
        def bfs(graph) :

            queue = deque([(0 , 0)])
            dist = [float("inf")]*n
            dist[0] = 0

            while queue :
                curr_node , curr_dist = queue.popleft()
                if dist[curr_node] < curr_dist :
                    continue

                for neighbour in graph[curr_node] :
                    new_dist = curr_dist + 1
                    if dist[neighbour] > new_dist :
                        dist[neighbour] = new_dist
                        queue.append((neighbour , new_dist))

            return dist[n-1] 

        res = []
        for u,v in queries :
            graph[u].append(v)
            # graph[v].append(u)

            ans = bfs(graph)
            res.append(ans)
        
        return res

