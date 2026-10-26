# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache

# # class DSU :
# #     def __init__(self,n) :
# #         self.size = [1]*(n)
# #         self.parent = list(range(n))
# #         self.comp = n
# #         self.total = [0]*(n)
    
# #     def find(self , node) :
# #         if self.parent[node] != node :
# #             self.parent[node] = self.find(self.parent[node])
        
# #         return self.parent[node]
    
# #     def union(self , a , b) :
# #         root_a , root_b = self.find(a) , self.find(b)

# #         if root_a == root_b :
# #             return False
        
# #         self.size[root_b] += self.size[root_a]
# #         self.parent[root_a] = root_b

# #         self.total[root_b] += self.total[root_a]
# #         self.total[root_a] = 0

# #         self.comp -= 1

# #         return True



# # class Solution:
# #     def countIslands(self, grid: List[List[int]], k: int) -> int:
        
# #         n , m = len(grid) , len(grid[0])

# #         dsu = DSU(n*m)
# #         vis = [[False]*m for _ in range(n)]

# #         dirs = [(-1,0) , (1,0) , (0,-1) , (0,1)]


# #         for i in range(n) :
# #             for j in range(m) :
# #                 if grid[i][j] > 0 :
# #                     dsu.total[i*m + j] = grid[i][j]
        
# #         for i in range(n):
# #             for j in range(m) :
# #                 if grid[i][j] != 0 :
# #                     cell_id = i*m + j

# #                     if j + 1 < m and grid[i][j] != 0 :
# #                         dsu.union(cell_id , i*m + (j+1))
                    
# #                     if i + 1 < n and grid[i][j] != 0 :
# #                         dsu.union(cell_id , (i+1)*m + j)
        
# #         ans = 0
# #         for i in range(n):
# #             for j in range(m) :
# #                 if grid[i][j] != 0 :
# #                     cell_id = i*m + j

# #                     if dsu.parent[cell_id] == cell_id and dsu.total[cell_id] % k == 0 :
# #                         ans += 1
        
# #         return ans


# #         # for i in range(n) :
# #         #     for j in range(m) :
# #         #         if grid[i][j] != 0 and not vis[i][j] :
# #         #             cell_id = i*m + j
# #         #             root = dsu.find(cell_id)
# #         #             dsu.total[cell_id] += grid[i][j] 
# #         #             for dx , dy in dirs :
# #         #                 new_row , new_col = i + dx , j + dy
# #         #                 if 0 <= new_row < n and 0 <= new_col < m :
# #         #                     if grid[new_row][new_col] != 0 :
# #         #                         new_id = new_row*m + new_col
# #         #                         dsu.total[new_id] += grid[new_row][new_col]
# #         #                         vis[new_row][new_col] = 1
        
# #         # ans = 0
# #         # for vals in dsu.total :
# #         #     if vals%k == 0 :
# #         #         ans += 1
        
# #         # return ans


# class Solution:
#     def countIslands(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         visited = set()
#         count = 0
        
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] > 0 and (i, j) not in visited:
#                     island_sum = 0
#                     queue = deque([(i, j)])
#                     visited.add((i, j))
                    
#                     while queue:
#                         r, c = queue.popleft()
#                         island_sum += grid[r][c]
                        
#                         for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#                             nr, nc = r + dr, c + dc
#                             if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 0 and (nr, nc) not in visited:
#                                 visited.add((nr, nc))
#                                 queue.append((nr, nc))
                    
#                     if island_sum % k == 0:
#                         count += 1
                        
#         return count

from collections import defaultdict, deque, Counter
import heapq
from functools import lru_cache
from typing import List

class DSU:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = list(range(n))
        self.comp = n
        self.total = [0] * n  # Array is cleaner & faster than defaultdict
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False
        
        # Merge small tree into large tree
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        # Combine total sum modulo k
        self.total[root_a] += self.total[root_b]
        self.total[root_b] = 0

        self.comp -= 1
        return True


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dsu = DSU(n * m)

        # Step 1: Initialize component totals with cell values for positive land cells
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    dsu.total[i * m + j] = grid[i][j]

        # Step 2: Union adjacent land cells (right and down are sufficient)
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    cell_id = i * m + j
                    # Union right neighbor
                    if j + 1 < m and grid[i][j + 1] > 0:
                        dsu.union(cell_id, i * m + (j + 1))
                    # Union down neighbor
                    if i + 1 < n and grid[i + 1][j] > 0:
                        dsu.union(cell_id, (i + 1) * m + j)

        # Step 3: Count component roots whose total sum is divisible by k
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    cell_id = i * m + j
                    # Check if cell_id is a root of an island
                    if dsu.parent[cell_id] == cell_id and dsu.total[cell_id] % k == 0:
                        ans += 1
        
        return ans