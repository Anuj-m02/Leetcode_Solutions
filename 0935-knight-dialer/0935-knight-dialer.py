# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache


# # class Solution:
# #     def knightDialer(self, n: int) -> int:
        
# #         # 8 dirs
# #         knight_dirs = [(-2,1) , (-2,-1) , (-1 , 2) , (-1 , -2) , (2,1) , (2,-1) , (1 , 2) , (1, -2)]

# #         mod = int(1e9) + 7

# #         grid = [["1","2","3"] , ["4","5","6"] , ["7","8","9"] , ["*" , "0" , "#"]]


# #         def check(curr_row , curr_col) :
            
# #             vis = set()
# #             # curr_row , curr_col , curr_length
# #             vis.add(grid[curr_row][curr_col])
# #             queue = deque([(curr_row , curr_col , 1 , grid[curr_row][curr_col])])
# #             cnt = 0

# #             while queue :
# #                 curr_row , curr_col , curr_length , curr_string = queue.popleft()
# #                 if curr_length == n :
# #                     cnt += 1
# #                     continue
                
# #                 for dx , dy in knight_dirs :
# #                     new_row , new_col = curr_row + dx , curr_col + dy
# #                     if 0 <= new_row < 4 and 0 <= new_col < 3 :
# #                         if grid[new_row][new_col] != "*" and grid[new_row][new_col] != "#" :
# #                             if curr_string + grid[new_row][new_col] not in vis :
# #                                 queue.append((curr_row , curr_col , curr_length + 1 , curr_string + grid[new_row][new_col]))
            
# #             return cnt%mod


# #         ans = 0
# #         for i in range(4) :
# #             for j in range(3) :
# #                 if grid[i][j] != "*" and grid[i][j] != "#" :
# #                     ans += check(i , j)%mod
        
# #         return ans%mod

# from collections import deque

# class Solution:
#     def knightDialer(self, n: int) -> int:
#         if n == 1:
#             return 10

#         knight_dirs = [(-2,1), (-2,-1), (-1,2), (-1,-2), (2,1), (2,-1), (1,2), (1,-2)]
#         mod = 10**9 + 7
#         grid = [["1","2","3"], ["4","5","6"], ["7","8","9"], ["*", "0", "#"]]

#         def count_paths(start_r, start_c):
#             # Tuple: (current_row, current_col, current_length)
#             queue = deque([(start_r, start_c, 1)])
#             cnt = 0

#             while queue:
#                 r, c, length = queue.popleft()

#                 if length == n:
#                     cnt = (cnt + 1) % mod
#                     continue

#                 for dx, dy in knight_dirs:
#                     nr, nc = r + dx, c + dy
#                     if 0 <= nr < 4 and 0 <= nc < 3:
#                         if grid[nr][nc] not in ("*", "#"):
#                             # Append the NEW coordinates (nr, nc)
#                             queue.append((nr, nc, length + 1))
#             return cnt

#         ans = 0
#         for i in range(4):
#             for j in range(3):
#                 if grid[i][j] not in ("*", "#"):
#                     ans = (ans + count_paths(i, j)) % mod

#         return ans

from functools import lru_cache

class Solution:
    def knightDialer(self, n: int) -> int:
        knight_dirs = [(-2,1), (-2,-1), (-1,2), (-1,-2), (2,1), (2,-1), (1,2), (1,-2)]
        mod = 10**9 + 7
        grid = [["1","2","3"], ["4","5","6"], ["7","8","9"], ["*", "0", "#"]]

        # Memoize results for (row, col, remaining_steps)
        @lru_cache(None)
        def dfs(r: int, c: int, remaining: int) -> int:
            if remaining == 1:
                return 1
            
            paths = 0
            for dx, dy in knight_dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < 4 and 0 <= nc < 3 and grid[nr][nc] not in ("*", "#"):
                    paths = (paths + dfs(nr, nc, remaining - 1)) % mod
            
            return paths

        ans = 0
        for i in range(4):
            for j in range(3):
                if grid[i][j] not in ("*", "#"):
                    ans = (ans + dfs(i, j, n)) % mod
        
        return ans