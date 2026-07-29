# class Solution:
#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
#         nxt = list(range(1,n+1))
#         nxt[n-1] = -1
#         curr_dist = n-1
#         ans = []
        
#         for u , v in queries :

#             if nxt[u] == -1 or nxt[u] >= v :
#                 ans.append(curr_dist)
            
#             else :

#                 curr = nxt[u]
#                 while curr != v :
#                     nxt[curr] , curr = -1 , nxt[curr]
#                     curr_dist -= 1
                
#                 nxt[u] = v
#                 ans.append(curr_dist)
            
#                 # curr = u
#                 # while curr < v :
#                 #     temp = nxt[curr]
#                 #     curr_dist -= 1
#                 #     curr = temp
                
#                 # curr_dist += 1
#                 # nxt[u] = v

#             # ans.append(curr_dist)
        
#         return ans

from sortedcontainers import SortedList
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Active nodes in the path from 0 to n-1
        active_nodes = SortedList(range(n))
        ans = []

        for u, v in queries:
            # Check if u and v are both still active in our path
            idx_u = active_nodes.bisect_left(u)
            idx_v = active_nodes.bisect_left(v)

            # If u is in the set and v is strictly to the right of u
            if idx_u < len(active_nodes) and active_nodes[idx_u] == u:
                # Remove all nodes strictly between u and v
                # Note: bisect_right(u) finds the first element > u
                start_remove = active_nodes.bisect_right(u)
                end_remove = active_nodes.bisect_left(v)

                # Delete slices of nodes that are bypassed
                del active_nodes[start_remove:end_remove]

            # Current distance is number of active nodes - 1
            ans.append(len(active_nodes) - 1)

        return ans




