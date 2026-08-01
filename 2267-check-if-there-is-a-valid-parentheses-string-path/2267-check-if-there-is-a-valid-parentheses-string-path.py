# from collections import defaultdict , deque , Counter
# import heapq

# from functools import lru_cache

# class Solution:
#     def hasValidPath(self, grid: List[List[str]]) -> bool:
        
#         n , m = len(grid) , len(grid[0])

#         if grid[0][0] == ")" :
#             return False

#         if grid[n-1][m-1] == "(" :
#             return False
        
#         directions = [(0,1) , (1,0)]


#         # row , col , balance
#         queue = deque([(0,0,1)])
#         visited = {(0,0,1)}

#         while queue :
#             curr_row , curr_col , curr_bal = queue.popleft()

#             if curr_row == n-1 and curr_col == m-1 :
#                 if curr_bal == 0 :
#                     return True
#                 continue
            
#             rem_dist = (n-1-curr_row) + (m-1-curr_col)
#             if curr_bal > rem_dist :
#                 continue
            
#             for x , y in directions :
#                 new_row , new_col = curr_row + x , curr_row + y

#                 if 0 <= new_row < n and 0 <= new_col < m :
#                     new_bal = curr_bal + (1 if grid[new_row][new_col] == "(" else -1)

#                     if new_bal >= 0 and (new_row , new_col , new_bal) not in visited :
#                         visited.add((new_row , new_col , new_bal))
#                         queue.append((new_row , new_col , new_bal))
        

#         return False

from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 1. Total path length is m + n - 1. If it's odd, it's impossible.
        if (m + n - 1) % 2 != 0:
            return False
        
        # 2. Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # Queue stores tuples of: (row, col, balance)
        queue = deque([(0, 0, 1)])
        
        # Visited set stores: (row, col, balance)
        visited = {(0, 0, 1)}
        
        while queue:
            r, c, bal = queue.popleft()
            
            # Reached destination? Check if balance is 0
            if r == m - 1 and c == n - 1:
                if bal == 0:
                    return True
                continue
            
            # Prune if remaining distance is less than open brackets needing to be closed
            rem_dist = (m - 1 - r) + (n - 1 - c)
            if bal > rem_dist:
                continue

            # Try moving Down and Right
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    # Update balance: +1 for '(', -1 for ')'
                    nbal = bal + (1 if grid[nr][nc] == '(' else -1)
                    
                    # Valid balance and not visited yet
                    if nbal >= 0 and (nr, nc, nbal) not in visited:
                        visited.add((nr, nc, nbal))
                        queue.append((nr, nc, nbal))
                        
        return False