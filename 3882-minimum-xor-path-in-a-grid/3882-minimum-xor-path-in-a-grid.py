# from functools import lru_cache

# class Solution:
#     def minCost(self, grid: list[list[int]]) -> int:
#         m, n = len(grid), len(grid[0])

#         @lru_cache(maxsize=None)
#         def dfs(r: int, c: int, current_xor: int) -> int:
#             current_xor ^= grid[r][c]

#             # Reached destination cell
#             if r == m - 1 and c == n - 1:
#                 return current_xor

#             res = float('inf')

#             # Move Down
#             if r + 1 < m:
#                 res = min(res, dfs(r + 1, c, current_xor))

#             # Move Right
#             if c + 1 < n:
#                 res = min(res, dfs(r, c + 1, current_xor))

#             return res

#         return dfs(0, 0, 0)

# class Solution:
#     def minCost(self, grid: list[list[int]]) -> int:
#         m, n = len(grid), len(grid[0])
        
#         # dp[r][c] stores a set of all reachable XOR sums at cell (r, c)
#         dp = [[set() for _ in range(n)] for _ in range(m)]
        
#         # Base case at start cell
#         dp[0][0].add(grid[0][0])
        
#         for r in range(m):
#             for c in range(n):
#                 val = grid[r][c]
                
#                 # From top neighbor
#                 if r > 0:
#                     for prev_xor in dp[r - 1][c]:
#                         dp[r][c].add(prev_xor ^ val)
                
#                 # From left neighbor
#                 if c > 0:
#                     for prev_xor in dp[r][c - 1]:
#                         dp[r][c].add(prev_xor ^ val)

#         # Return the minimum possible final XOR value at bottom-right cell
#         return min(dp[m - 1][n - 1])

from functools import lru_cache

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dfs(r: int, c: int) -> set:
            # Base case: reached bottom-right cell
            if r == m - 1 and c == n - 1:
                return {grid[r][c]}

            reachable_xors = set()

            # Move Down
            if r + 1 < m:
                for xor_val in dfs(r + 1, c):
                    reachable_xors.add(grid[r][c] ^ xor_val)

            # Move Right
            if c + 1 < n:
                for xor_val in dfs(r, c + 1):
                    reachable_xors.add(grid[r][c] ^ xor_val)

            return reachable_xors

        return min(dfs(0, 0))