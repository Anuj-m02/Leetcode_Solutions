# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         islands = 0
#         visited = set()
#         rows, cols = len(grid), len(grid[0])

#         def bfs(r, c):
#             q = deque()
#             visited.add((r, c))
#             q.append((r, c))

#             while q:
#                 row, col = q.popleft()
#                 directions = [[1,0],[-1,0],[0,1],[0,-1]]

#                 for dr, dc in directions:
#                     r, c = row + dr, col + dc
#                     if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
#                         q.append((r, c))
#                         visited.add((r, c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     islands += 1
#                     bfs(r, c)

#         return islands


class UnionFind:
    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        self.parent = {}
        self.count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    node = r * cols + c
                    self.parent[node] = node
                    self.count += 1

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1  # Reduce island count when merging two components


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        dsu = UnionFind(grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Only look down and right to avoid redundant unions
                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if nr < rows and nc < cols and grid[nr][nc] == "1":
                            dsu.union(r * cols + c, nr * cols + nc)

        return dsu.count