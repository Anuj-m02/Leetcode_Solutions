# class Solution:
#     def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
#         n = len(floor)

#         if numCarpets * carpetLen >= n :
#             return 0
        

#         @lru_cache(maxsize=None)
#         def dp(indx , carpet_used) :

#             if indx >= n :
#                 if carpet_used <= numCarpets :
#                     return 0
#                 else :
#                     return float("inf")
            

#             curr_tile = floor[indx]
#             ans = float("inf")
#             # option 1 dont place carpet here
#             if curr_tile == "1" :
#                 ans = min(ans , 1 + dp(indx+1 , carpet_used))
#             else :
#                 ans = min(ans , dp(indx+1 , carpet_used))
            

#             # place carpte here
#             if curr_tile == "1" :
#                 ans = min(ans , dp(indx + carpetLen , carpet_used+1))
#             else :
#                 ans = min(ans , dp(indx + carpetLen , carpet_used+1))
            
#             return ans
        
#         return dp(0 , 0)

from functools import lru_cache

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)

        if numCarpets * carpetLen >= n:
            return 0

        @lru_cache(maxsize=None)
        def dp(indx, carpet_used):
            if indx >= n:
                return 0 if carpet_used <= numCarpets else float("inf")
            
            # Option 1: Don't place carpet here
            cost = 1 if floor[indx] == "1" else 0
            ans = cost + dp(indx + 1, carpet_used)

            # Option 2: Place carpet here (if available)
            if carpet_used < numCarpets:
                ans = min(ans, dp(indx + carpetLen, carpet_used + 1))

            return ans

        return dp(0, 0)