from collections import defaultdict , deque, Counter
import heapq
from functools import lru_cache


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for u, v, w in edges :
            graph[u].append((v,w))
            graph[v].append((u , 2*w))
        
        # curr_dist , curr_node
        heap = [(0,0)]
        dist = [float("inf")]*(n)
        dist[0] = 0

        while heap :
            curr_dist , curr_node = heapq.heappop(heap)

            if curr_node == n-1 :
                return curr_dist

            if dist[curr_node] < curr_dist :
                continue
            
            for neighbour , weight in graph[curr_node] :
                new_wt = curr_dist + weight
                if dist[neighbour] > new_wt :
                    dist[neighbour] = new_wt
                    heapq.heappush(heap , (new_wt , neighbour))
        
        return -1

