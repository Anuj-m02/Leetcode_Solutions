# # class Solution:
# #     def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        
# #         n , m = len(grid) , len(grid[0])
# #         k = min(k , n+m -1)
        
# #         @cache
# #         def dp(row , col , cost) :

# #             if row >= n or col >= m or cost > k :
# #                 return float("-inf")
            
# #             curr_cell = grid[row][col]
# #             new_cost = cost + (0 if curr_cell == 0 else 1)

# #             if new_cost > k :
# #                 return float("-inf")
         
# #             if row == n-1 and col == m-1 and cost <= k :
# #                 return curr_cell
            
            
# #             ans = float("-inf")
# #             down = dp(row+1 , col , new_cost)
# #             right = dp(row , col+1 , new_cost)

# #             ans = max(ans , curr_cell +  down , curr_cell + right)

# #             return ans
        
# #         ans = dp(0 , 0 , 0)
# #         if ans == float("-inf") :
# #             return -1
# #         else :
# #             return ans


# from functools import lru_cache
# from typing import List

# class Solution:
#     def maxPathScore(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         # Cap k to maximum possible path cost length to save states
#         k = min(k, n + m - 1)
        
#         @lru_cache(maxsize=None)
#         def f(i: int, j: int, c: int) -> int:
#             if i < 0 or j < 0 or c > k:
#                 return float("-inf")
            
#             x = grid[i][j]
#             cost = c + (1 if x != 0 else 0)
            
#             if cost > k:
#                 return float("-inf")
            
#             if i == 0 and j == 0:
#                 return grid[0][0]
            
#             res = x + max(f(i - 1, j, cost), f(i, j - 1, cost))
#             return res

#         ans = f(n - 1, m - 1, 0)
#         return ans if ans != float("-inf") else -1

from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        # A path can take at most n + m - 1 steps, so max cost is min(k, n + m - 1)
        k = min(k, n + m - 1)
        
        # 3D table initialized with -1 representing float("-inf") / unreachable states
        dp = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
        
        # Base case for top-left cell (0, 0)
        start_val = grid[0][0]
        start_cost = 0 if start_val == 0 else 1
        if start_cost <= k:
            dp[0][0][start_cost] = start_val

        # Fill table top-to-bottom, left-to-right
        for r in range(n):
            for c in range(m):
                val = grid[r][c]
                cost_inc = 0 if val == 0 else 1
                
                for cost in range(k + 1):
                    if dp[r][c][cost] == -1:
                        continue
                    
                    curr_score = dp[r][c][cost]
                    
                    # Move Down
                    if r + 1 < n:
                        next_val = grid[r + 1][c]
                        next_cost = cost + (0 if next_val == 0 else 1)
                        if next_cost <= k:
                            dp[r + 1][c][next_cost] = max(
                                dp[r + 1][c][next_cost], 
                                curr_score + next_val
                            )
                            
                    # Move Right
                    if c + 1 < m:
                        next_val = grid[r][c + 1]
                        next_cost = cost + (0 if next_val == 0 else 1)
                        if next_cost <= k:
                            dp[r][c + 1][next_cost] = max(
                                dp[r][c + 1][next_cost], 
                                curr_score + next_val
                            )
                            
        ans = max(dp[n - 1][m - 1])
        return ans if ans != -1 else -1