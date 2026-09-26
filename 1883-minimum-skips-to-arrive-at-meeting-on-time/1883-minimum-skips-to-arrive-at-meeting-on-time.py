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
        def dp(i, skips):
            """
            Returns the minimum total accumulated "dist-time" needed to process 
            the first `i` roads using `skips` total skips.
            """
            if skips < 0:
                return float("inf")
            if i == 0:
                return 0

            d = dist[i - 1]

            # Option 1: Rested after road i-2 (or it was starting at index 0)
            # Need to ceil the previous cumulative time/distance to the next multiple of speed.
            prev_rested = dp(i - 1, skips)
            option_rest = math.ceil(prev_rested / speed) * speed + d

            # Option 2: Skipped rest after road i-2
            prev_skipped = dp(i - 1, skips - 1)
            option_skip = prev_skipped + d

            return min(option_rest, option_skip)

        # Check the minimum number of skips (from 0 up to n - 1) that fits within hoursBefore
        for skips in range(n):
            if dp(n, skips) <= hoursBefore * speed:
                return skips

        return -1