# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:

#         graph = defaultdict(list)

#         for u , v , w in edges :
#             graph[u].append((v,w))
#             graph[v].append((u,w))
        
#         def check(mid):
#             # at most k hvy edges , wt > mid hvy edge
#             # curr_node , curr_hvy_edges
#             queue = deque([])
#             queue.append((source , 0))
#             vis = [0]*(n)
#             vis[source] = 1

#             while queue :
#                 curr_node , curr_hvy_edges = queue.popleft()

#                 if curr_node == target :
#                     if curr_hvy_edges <= k :
#                         return True
                
#                 for neighbour , wt in graph[curr_node] :
#                     if not vis[neighbour]  :
#                         if wt > mid :
#                             curr_hvy_edges += 1
#                             vis[neighbour] = 1
#                             queue.append((neighbour , curr_hvy_edges))
#                         else :
#                             vis[neighbour] = 1
#                             queue.appendleft((neighbour , curr_hvy_edges))
            
#             return False
                        


#         ans = -1
#         low , high = 0 , int(1e5)
#         while low <= high :
#             mid = (low+high)//2
#             if check(mid) :
#                 ans = mid
#                 high = mid-1
#             else :
#                 low = mid+1
        
#         return ans

from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        max_weight = 0
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            max_weight = max(max_weight, w)
        
        def check(mid):
            # dist[node] stores the minimum heavy edges needed to reach 'node'
            dist = [float('inf')] * n
            dist[source] = 0
            
            # 0-1 BFS Deque
            dq = deque([source])

            while dq:
                curr = dq.popleft()

                if curr == target:
                    return dist[target] <= k
                
                for neighbour, wt in graph[curr]:
                    # Cost is 0 if wt <= mid (light), 1 if wt > mid (heavy)
                    cost = 1 if wt > mid else 0
                    
                    if dist[curr] + cost < dist[neighbour]:
                        dist[neighbour] = dist[curr] + cost
                        
                        # Cost 0 goes to front, Cost 1 goes to back
                        if cost == 0:
                            dq.appendleft(neighbour)
                        else:
                            dq.append(neighbour)
            
            return dist[target] <= k

        ans = -1
        low, high = 0, max_weight

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans