class DSU :

    def __init__(self , n) :
        self.n = n
        self.parent = list(range(n+1))
        self.size = [0]*(n)
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self , a ,b) :
        root_a ,  root_b = self.find(a) , self.find(b)
        if root_a == root_b :
            return False
        
        self.size[root_a] += self.size[root_b]
        self.parent[root_b] = root_a
        return True


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        if not grid or not grid[0] :
            return 0
        
        n , m = len(grid) , len(grid[0])

        dirs = [(0,1) , (0,-1) , (1,0) , (-1, 0)]

        dsu = DSU(n*m)

        has_land = False
        for row in range(n) :
            for col in range(m) :
                if grid[row][col] == 1 :
                    has_land = True
                    indx = row*m + col
                    dsu.size[indx] = 1
        
        if not has_land :
            return 0
 
        # vis = [[False]*m for _ in range(n)]

        for row in range(n) :
            for col in range(m) :
                if grid[row][col] == 1 :
                    for dx,dy in dirs :
                        new_row , new_col = row + dx , col + dy
                        if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1:
                            dsu.union(row*m + col , new_row*m + new_col)
                            # vis[new_row][new_col] = True
                    
                    # vis[row][col] = True
        
        return max(dsu.size)


