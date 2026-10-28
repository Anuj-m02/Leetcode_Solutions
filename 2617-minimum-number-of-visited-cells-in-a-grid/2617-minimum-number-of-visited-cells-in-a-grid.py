# class Solution:
#     def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        
#         n , m = len(grid) , len(grid[0])

#         dist = [[float("inf")]*m for _ in range(n)]
#         # curr_no_of_cell , curr_row , curr_col
#         heap = [(1 , 0 , 0)]
#         dist[0][0] = 1

#         while heap :
#             curr_cell , curr_row , curr_col = heapq.heappop(heap)

#             if curr_row == n-1 and curr_col == m-1 :
#                 return curr_cell
            
#             if dist[curr_row][curr_col] < curr_cell :
#                 continue
            
#             #rightward
#             for k in range(curr_col+1 , min(m , curr_col + grid[curr_row][curr_col] + 1)) :

#                 if dist[curr_row][k] > 1 + curr_cell :
#                     dist[curr_row][k] = 1 + curr_cell
#                     heapq.heappush(heap , (1+curr_cell , curr_row , k))

#                 else :
#                     continue
                
#             # downward
#             for k in range(curr_row +1, min(n , curr_row + grid[curr_row][curr_col] + 1)) :

#                 if dist[k][curr_col] > 1 + curr_cell :
#                     dist[k][curr_col] = 1 + curr_cell
#                     heapq.heappush(heap , (1+curr_cell , k , curr_col))

#                 else :
#                     continue

#         return -1            
from collections import deque
from typing import List

class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if m == 1 and n == 1:
            return 1

        # One DSU per row (tracks unvisited columns)
        row_dsu = [DSU(n) for _ in range(m)]
        # One DSU per column (tracks unvisited rows)
        col_dsu = [DSU(m) for _ in range(n)]

        # Queue stores (row, col, distance)
        queue = deque([(0, 0, 1)])

        # Mark starting cell as visited by linking it to the next index
        row_dsu[0].union(0, 1)
        col_dsu[0].union(0, 1)

        while queue:
            r, c, dist = queue.popleft()
            max_jump = grid[r][c]

            # 1. Rightward movement
            limit_col = min(n - 1, c + max_jump)
            next_c = row_dsu[r].find(c + 1)
            while next_c <= limit_col:
                if r == m - 1 and next_c == n - 1:
                    return dist + 1
                queue.append((r, next_c, dist + 1))
                # Mark as visited in both row and col DSUs
                row_dsu[r].union(next_c, next_c + 1)
                col_dsu[next_c].union(r, r + 1)
                # Jump to the next unvisited cell in this row
                next_c = row_dsu[r].find(next_c + 1)

            # 2. Downward movement
            limit_row = min(m - 1, r + max_jump)
            next_r = col_dsu[c].find(r + 1)
            while next_r <= limit_row:
                if next_r == m - 1 and c == n - 1:
                    return dist + 1
                queue.append((next_r, c, dist + 1))
                # Mark as visited in both row and col DSUs
                row_dsu[next_r].union(c, c + 1)
                col_dsu[c].union(next_r, next_r + 1)
                # Jump to the next unvisited cell in this column
                next_r = col_dsu[c].find(next_r + 1)

        return -1