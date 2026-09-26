# # class Solution:
# #     def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        

# #         n = len(dist)
# #         eps = 1e-9

# #         @lru_cache(maxsize=None)
# #         def dp(indx , time , rest):

# #             if indx >= n :
# #                 if time <= hoursBefore :
# #                     return 0
# #                 else :
# #                     return float("inf")

# #             ans = float("inf")
# #             # if rest
# #             if rest :
# #                 nxt_int_time = math.ceil(time)
# #                 rest_time = nxt_int_time - time

# #                 ans = min(ans , 1 + dp(indx+1 , nxt_int_time + dist[indx]/speed , 0))
# #                 ans = min(ans , dp(indx+1 , nxt_int_time + dist[indx]/speed, 1))
            
# #             if not rest :
# #                 add_time = dist[indx]/speed
# #                 nxt_int_time = math.ceil(time + add_time)
# #                 ans = min(ans , 1 + dp(indx+1 , nxt_int_time , 0))
# #                 ans = min(ans , dp(indx+1 , nxt_int_time , 1))          
            
# #             return ans

# #         ans = dp(0 , 0 , 0)
# #         if ans == float("inf") :
# #             return -1
# #         else :
# #             return ans

# from functools import lru_cache
# import math

# class Solution:
#     def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
#         n = len(dist)
#         EPS = 1e-9

#         @lru_cache(maxsize=None)
#         def dp(indx, time):
#             if indx == n:
#                 if time <= hoursBefore + EPS:
#                     return 0
#                 return float("inf")

#             add_time = dist[indx] / speed
            
#             # Option 1: Take rest after this road (cost: 0 skips)
#             # Round up to next integer hour mark (only required if not the last road)
#             if indx < n - 1:
#                 nxt_int_time = math.ceil(time + add_time - EPS)
#                 ans = dp(indx + 1, nxt_int_time)
#             else:
#                 ans = dp(indx + 1, time + add_time)

#             # Option 2: Skip rest after this road (cost: 1 skip)
#             # Add time directly without rounding up
#             skip_ans = 1 + dp(indx + 1, time + add_time)
            
#             return min(ans, skip_ans)

#         res = dp(0, 0.0)
#         return res if res != float("inf") else -1

from functools import lru_cache
import math

class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)

        @lru_cache(maxsize=None)
        def dp(indx, skips):
            # Base Case: All roads finished
            if indx >= n:
                return 0

            d = dist[indx]

            # Option 1: Take rest after this road (only possible if not the last road)
            # If it's the last road (indx == n - 1), no rest is taken, so no ceiling needed.
            # if indx < n - 1:
                # Calculate time spent so far after resting: ceil((current_dist + d) / speed) * speed
            rest_cost = math.ceil((dp(indx + 1, skips) + d) / speed) * speed
            # else:
            #     rest_cost = dp(indx + 1, skips) + d

            # Option 2: Skip rest after this road
            skip_cost = float("inf")
            if skips > 0:
                skip_cost = dp(indx + 1, skips - 1) + d

            return min(rest_cost, skip_cost)

        # Try minimum skips from 0 to n - 1
        for skips in range(n):
            if dp(0, skips) <= hoursBefore * speed:
                return skips

        return -1