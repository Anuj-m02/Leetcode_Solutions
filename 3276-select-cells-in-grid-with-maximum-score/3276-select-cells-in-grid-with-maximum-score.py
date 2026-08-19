# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache


# # class Solution:
# #     def maxScore(self, grid: List[List[int]]) -> int:
        
# #         n , m = len(grid) , len(grid[0])

# #         # memo = defaultdict(int)

# #         # @lru_cache(maxsize=None)
# #         def dp(row , visited) :

# #             if row == n :
# #                 return 0

# #             ans = float("-inf")
# #             ans = max(ans , dp(row+1 , visited))         
# #             for col in range(m):
# #                 if grid[row][col] not in visited :
# #                     ans = max(ans , grid[row][col] + dp(row+1 , visited | frozenset([grid[row][col]])))
            
# #             memo[row] = ans
# #             return ans
        
# #         return dp(0 , frozenset())


# from collections import defaultdict, deque, Counter
# import heapq
# from functools import lru_cache
# from typing import List

# class Solution:
#     def maxScore(self, grid: List[List[int]]) -> int:
        
#         n, m = len(grid), len(grid[0])

#         # Map each unique value to a list of (row, col) coordinates
#         # to ensure we check value uniqueness without putting raw values in frozenset
#         val_to_coords = defaultdict(list)
#         for r in range(n):
#             for c in range(m):
#                 val_to_coords[grid[r][c]].append((r, c))

#         @lru_cache(maxsize=None)
#         def dp(row, visited_rows, chosen_vals):
#             if row == n:
#                 return 0

#             # Option 1: Skip this row
#             ans = dp(row + 1, visited_rows, chosen_vals)

#             # Option 2: Pick a value from this row
#             for col in range(m):
#                 val = grid[row][col]
#                 if val not in chosen_vals:
#                     ans = max(
#                         ans, 
#                         val + dp(row + 1, visited_rows | frozenset([row]), chosen_vals | frozenset([val]))
#                     )

#             return ans

#         return dp(0, frozenset(), frozenset())

from collections import defaultdict, deque, Counter
import heapq
from functools import lru_cache
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])

        val_to_rows = defaultdict(set)
        for r in range(n):
            for c in range(m):
                val_to_rows[grid[r][c]].add(r)

        unique_vals = sorted(val_to_rows.keys(), reverse=True)
        total_vals = len(unique_vals)

        @lru_cache(maxsize=None)
        def dp(val_idx, visited_rows):
            if val_idx == total_vals:
                return 0

            # Option 1: Skip current value
            ans = dp(val_idx + 1, visited_rows)

            # Option 2: Choose this value for one available row
            val = unique_vals[val_idx]
            for r in val_to_rows[val]:
                if r not in visited_rows:
                    ans = max(ans, val + dp(val_idx + 1, visited_rows | frozenset([r])))

            return ans

        return dp(0, frozenset())