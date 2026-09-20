# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        
#         graph = defaultdict(list)
#         for u,v,w in edges :
#             graph[u].append((v,w))
        
#         curr_wt , curr_node , curr_k = 0 , 0 , 1
#         heap = [(curr_wt , curr_node , curr_k)]
#         dist = defaultdict(lambda : float("inf"))
#         dist[(curr_node , curr_k)] =  curr_wt


#         while heap :
#             curr_wt , curr_node , curr_k = heapq.heappop(heap)
#             if curr_node == n-1  and curr_k <= k :
#                 return curr_wt
            
#             if dist[(curr_node , curr_k)] < curr_wt :
#                 continue
            
#             curr_label = labels[curr_node]

#             for neighbour , wt in graph[curr_node] :
#                 new_label = labels[neighbour]

#                 if new_label == curr_label and curr_k < k :
#                     new_dist = curr_wt + wt
#                     if dist[(neighbour , curr_k+1)] > new_dist :
#                         dist[(neighbour, curr_k+1)] = new_dist
#                         heapq.heappush(heap , (new_dist , neighbour , curr_k+1))
                
#                 else :
#                     new_dist = curr_wt + wt
#                     new_k = 1
#                     if dist[(neighbour , new_k)] > new_dist :
#                         dist[(neighbour, new_k)] = new_dist
#                         heapq.heappush(heap , (new_dist , neighbour , new_k))
            
        
#         return -1

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        
        # Initial state: node 0 starts with consecutive count 1
        # Priority queue stores: (distance, node, consecutive_count)
        heap = [(0, 0, 1)]
        dist = defaultdict(lambda: float('inf'))
        dist[(0, 1)] = 0

        while heap:
            curr_wt, curr_node, curr_k = heapq.heappop(heap)

            if curr_node == n - 1:
                return curr_wt

            if dist[(curr_node, curr_k)] < curr_wt:
                continue

            curr_label = labels[curr_node]

            for neighbour, wt in graph[curr_node]:
                new_label = labels[neighbour]

                if new_label == curr_label:
                    # Same label: increment streak count
                    new_k = curr_k + 1
                else:
                    # Different label: reset streak count to 1
                    new_k = 1

                # Only proceed if the new streak count is <= k
                if new_k <= k:
                    new_dist = curr_wt + wt
                    if new_dist < dist[(neighbour, new_k)]:
                        dist[(neighbour, new_k)] = new_dist
                        heapq.heappush(heap, (new_dist, neighbour, new_k))

        return -1