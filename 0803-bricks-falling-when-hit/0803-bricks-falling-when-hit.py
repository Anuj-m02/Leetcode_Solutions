# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache

# class DSU :
#     def __init__(self,n) :
#         self.parent = list(range(n))
#         self.size = [1]*(n)
    
#     def find(self , node) :
#         if self.parent[node] != node :
#             self.parent[node] = self.find(self.parent[node])
        
#         return self.parent[node]
    
#     def union(self , a , b) :
#         root_a , root_b = self.find(a) , self.find(b)

#         if root_a == root_b :
#             return False
        
#         self.size[root_a] += self.size[root_b]
#         self.parent[root_b] = root_a

#         return True
    
#     def get_size(self , node) :
#         return self.size[self.find(node)]


# class Solution:
#     def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        
#         # def check(grid) :

#         grid_copy = [row[:] for row in grid]
#         for row , col in hits :
#             if grid_copy[row][col] == 1 :
#                 grid_copy[row][col] = 2
        
#         dsu = DSU(n*m + 1)



#         n , m = len(grid) , len(grid[0])
#         q = len(hits)
#         dirs = [(1,0) , (0,1) , (-1,0) , (0,-1)]
#         roof = n*m 

#         for col in range(m) :
#             if grid_copy[0][col] == 1 :
#                 dsu.union(col , roof)
        
#         for row in range(n) :
#             for col in range(m) :
#                 if grid_copy[row][col] == 1 :
#                     indx = row*m + col
#                     for dx , dy in dirs :
#                         new_row , new_col = row + dx , col + dy
#                         if 0 <= new_row < n and 0 <= new_col < m and grid_copy[new_row][new_col] == 1 :
#                             dsu.union(indx , new_row*m + new_col)
        
#         ans = [0]*(q)

#         for i in range(q-1 , -1 , -1) :
#             row ,col = hits[i]

#             if grid[row][col] == 0 :
#                 continue
            
#             grid_copy[row][col] = 1
#             indx = row*m + col

#             prev_roof_size = dsu.get_size(roof)

#             if row == 0 :
#                 dsu.union(indx , roof)
            
#             for dx , dy in dirs :
#                 new_row , new_col = row + dx , col + dy
#                 if 0 <= new_row < n and 0 <= new_col < m and grid_copy[new_row][new_col] == 1 :
#                     dsu.union(indx , new_row*m + new_col)
            
#             if dsu.find(indx) == dsu.find(roof) :
#                 curr_roof_size = dsu.get_size(roof)
#                 ans[i] = max(0 , curr_roof_size - prev_roof_size-1)
            
#         return ans
            
#         # dsu.get_size(roof) - 1



#         # n , m = len(grid) , len(grid[0])
#         # q = len(hits)
#         # prev = check(grid)
        
#         # ans = []

#         # for row , col in hits :

#         #     prev = check(grid)

#         #     if grid[row][col] == 0 :
#         #         ans.append(0)
#         #         continue
            
#         #     grid[row][col] = 0
#         #     curr = check(grid)

#         #     dropped = max(0 , prev-curr-1)
#         #     ans.append(dropped)
        
#         # return ans
        

from collections import defaultdict, deque, Counter
import heapq
from functools import lru_cache

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        
        # Attach smaller tree to larger tree to keep balance
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.size[root_a] += self.size[root_b]
        self.parent[root_b] = root_a
        return True
    
    def get_size(self, node):
        return self.size[self.find(node)]


class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        n, m = len(grid), len(grid[0])
        roof = n * m
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # 1. Mark all hit bricks in a grid copy
        # 1 -> original brick, 2 -> hit brick
        grid_copy = [row[:] for row in grid]
        for r, c in hits:
            if grid_copy[r][c] == 1:
                grid_copy[r][c] = 2

        # 2. Build initial DSU for remaining unhit bricks (1s)
        dsu = DSU(n * m + 1)

        # Connect top row to virtual roof
        for col in range(m):
            if grid_copy[0][col] == 1:
                dsu.union(col, roof)

        # Connect rest of adjacent bricks
        for r in range(n):
            for c in range(m):
                if grid_copy[r][c] == 1:
                    idx = r * m + c
                    for dx, dy in dirs:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < m and grid_copy[nr][nc] == 1:
                            dsu.union(idx, nr * m + nc)

        ans = [0] * len(hits)

        # 3. Process hits in REVERSE order
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]

            # If the original cell was empty (0), hit has no effect
            if grid[r][c] == 0:
                continue

            grid_copy[r][c] = 1
            idx = r * m + c

            prev_roof_size = dsu.get_size(roof)

            # If added brick is on the top row, connect to roof directly
            if r == 0:
                dsu.union(idx, roof)

            # Union with adjacent existing bricks
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < m and grid_copy[nr][nc] == 1:
                    dsu.union(idx, nr * m + nc)

            # Check if this added brick is now attached to the roof
            if dsu.find(idx) == dsu.find(roof):
                curr_roof_size = dsu.get_size(roof)
                ans[i] = max(0, curr_roof_size - prev_roof_size - 1)

        return ans