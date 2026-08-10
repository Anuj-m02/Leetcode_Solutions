# from collections import defaultdict , deque ,Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def maxScore(self, grid: List[List[int]]) -> int:
#         n , m = len(grid) , len(grid[0])

#         @lru_cache(None)
#         def dp(row , col) :

#             max_gain = float("-inf")
            
#             # has option whether to go to right means in this row only
#             temp1 = float("-inf")
#             for new_col in range(col+1 , m):
#                 diff = grid[row][new_col] - grid[row][col]
#                 max_gain = max(max_gain , diff , diff + dp(row , new_col))
#             # has option to go to down so same column only
#             temp2 = float("-inf")
#             for new_row in range(row+1 , n):
#                 diff = grid[new_row][col] - grid[row][col]
#                 max_gain = max(max_gain , diff  , diff+ dp(new_row , col))
            
#             return max_gain
        

#         ans = float("-inf")
#         for row in range(n):
#             for col in range(m):
#                 ans = max(ans , dp(row , col))
#         return ans


from functools import lru_cache
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(row: int, col: int) -> int:
            max_gain = float("-inf")

            # Option 1: Move right by at least 1 step
            if col + 1 < m:
                diff = grid[row][col + 1] - grid[row][col]
                max_gain = max(max_gain, diff, diff + dp(row, col + 1))

            # Option 2: Move down by at least 1 step
            if row + 1 < n:
                diff = grid[row + 1][col] - grid[row][col]
                max_gain = max(max_gain, diff, diff + dp(row + 1, col))

            return max_gain

        ans = float("-inf")
        for r in range(n):
            for c in range(m):
                ans = max(ans, dp(r, c))

        return ans