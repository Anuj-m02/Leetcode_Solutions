# class Solution:
#     def minCost(self, grid: List[List[int]]) -> int:
        
#         n , m = len(grid) , len(grid[0])

#         # 1 right , 2 left , 3 down , 4 up
#         dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         graph = defaultdict(list)
#         for row in range(n):
#             for col in range(m) :
#                 curr_dir = grid[row][col]
#                 for i, (dr, dc) in enumerate(dirs, start=1):
#                     nr, nc = row + dr, col + dc
                    
#                     # Ensure neighbor is strictly within grid bounds
#                     if 0 <= nr < n and 0 <= nc < m:
#                         cost = 0 if curr_dir == i else 1
#                         graph[(row, col)].append((nr, nc, cost))
#                 # if curr_dir == 1 :
#                 #     graph[(row , col)].append((row , col + 1 , 0))
#                 #     graph[(row , col)].append((row , col-1 , 1))
#                 #     graph[(row , col)].append((row + 1 , col , 1))
#                 #     graph[(row , col)].append((row-1 , col , 1))
#                 # elif curr_dir == 2 :
#                 #     graph[(row , col)].append((row , col - 1 , 0))
#                 #     graph[(row , col)].append((row , col+1 , 1))
#                 #     graph[(row , col)].append((row + 1 , col , 1))
#                 #     graph[(row , col)].append((row-1 , col , 1))
#                 # elif curr_dir == 3 :
#                 #     graph[(row , col)].append((row + 1 , col , 0))
#                 #     graph[(row , col)].append((row , col-1 , 1))
#                 #     graph[(row , col)].append((row , col + 1 , 1))
#                 #     graph[(row , col)].append((row-1 , col , 1))
#                 # else :
#                 #     graph[(row , col)].append((row -1 , col , 0))
#                 #     graph[(row , col)].append((row , col-1 , 1))
#                 #     graph[(row , col)].append((row + 1 , col , 1))
#                 #     graph[(row , col)].append((row , col + 1 , 1))

#         queue = deque([(0 , 0 , 0)])
#         # curr_row , curr_col , curr_wt
#         vis = set()

#         while queue :
#             curr_row , curr_col , curr_wt = queue.popleft()

#             if (curr_row , curr_col) in vis :
#                 continue
#             vis.add((curr_row , curr_col)) 

#             if curr_row == n-1 and curr_col == m-1 :
#                 return curr_wt
            
#             for neighbour_row , neighbour_col , new_wt in graph[(curr_row , curr_col)] :
#                 if 0 <= neighbour_row < n and 0 <= neighbour_col < m :
#                     if (neighbour_row , neighbour_col) not in vis :
#                         queue.append((neighbour_row , neighbour_col , new_wt + curr_wt))
        
#         return -1

from collections import defaultdict, deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # 1: right, 2: left, 3: down, 4: up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 1: Build the Adjacency List Graph
        graph = defaultdict(list)
        for row in range(n):
            for col in range(m):
                curr_dir = grid[row][col]
                for i, (dr, dc) in enumerate(dirs, start=1):
                    nr, nc = row + dr, col + dc
                    
                    # Ensure neighbor is strictly within grid bounds
                    if 0 <= nr < n and 0 <= nc < m:
                        cost = 0 if curr_dir == i else 1
                        graph[(row, col)].append((nr, nc, cost))

        # Step 2: 0-1 BFS Traversal
        queue = deque([(0, 0, 0)])  # (row, col, cost)
        vis = set()

        while queue:
            curr_row, curr_col, curr_wt = queue.popleft()

            if (curr_row, curr_col) in vis:
                continue
            vis.add((curr_row, curr_col)) 

            # Target reached
            if curr_row == n - 1 and curr_col == m - 1:
                return curr_wt
            
            for neighbour_row, neighbour_col, new_wt in graph[(curr_row, curr_col)]:
                if (neighbour_row, neighbour_col) not in vis:
                    # 0-1 BFS Queue Handling:
                    if new_wt == 0:
                        # Free move: Push to FRONT to process immediately
                        queue.appendleft((neighbour_row, neighbour_col, curr_wt))
                    else:
                        # Cost 1 move: Push to BACK to process later
                        queue.append((neighbour_row, neighbour_col, curr_wt + 1))
        
        return -1