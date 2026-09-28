# from functools import lru_cache


# class Solution:
#     def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        

#         @lru_cache(maxsize=None)
#         def dp(row , col):

#             # if row >= m or col >= n :
#             #     return float("inf")
            
#             if row == m-1 and col == n-1 :
#                 return 0
            

#             # curr_cost = (row+1)*(col+1)
#             ans = float("inf")

#             if row+1 < m :
#                 cost = (row+2)*(col+1) + waitCost[row+1][col]
#                 ans = min(ans , dp(row+1 , col) + cost)

#             if col+1 < n :
#                 cost = (row+1)*(col+2) + waitCost[row][col+1]
#                 ans = min(ans , dp(row , col+1) + cost)
            
#             return ans

#             # # odd
#             # if parity == 1 :

#             #     ans = min(ans , dp(row+1 , col , 1-parity) + (row+1+1)*(col+1) , dp(row , col+1 , 1-parity) + (row+1)*(col+1+1))
            
#             # else :
#             # #     ans = min(ans, dp(row , col , 1-parity) + waitCost[row][col])
            
#             # return ans
        
#         total = 1 + waitCost[0][0] + dp(0,0) - waitCost[m-1][n-1]
#         return total



            
from functools import lru_cache
import sys

sys.setrecursionlimit(200000)

class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(row, col):
            # Reached destination: no further cost
            if row == m - 1 and col == n - 1:
                return 0
            
            ans = float("inf")
            
            # Move Down
            if row + 1 < m:
                # Pay next cell entry cost
                cost = (row + 2) * (col + 1)
                # If next cell is NOT destination, pay its waitCost too
                if not (row + 1 == m - 1 and col == n - 1):
                    cost += waitCost[row + 1][col]
                ans = min(ans, dp(row + 1, col) + cost)
                
            # Move Right
            if col + 1 < n:
                # Pay next cell entry cost
                cost = (row + 1) * (col + 2)
                # If next cell is NOT destination, pay its waitCost too
                if not (row == m - 1 and col + 1 == n - 1):
                    cost += waitCost[row][col + 1]
                ans = min(ans, dp(row, col + 1) + cost)
                
            return ans
        
        # Start at (0, 0): Pay initial entry cost (1) + dp from (0, 0)
        return 1 + dp(0, 0)