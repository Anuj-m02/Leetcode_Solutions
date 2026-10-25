class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        

        n , m = len(grid) , len(grid[0])

        def bfs(row , col) :
            queue = deque([(row , col)])
            grid[row][col] = 1

            while queue :
                curr_row , curr_col = queue.popleft()
                for dr , dc in [(-1,0) , (1,0) , (0,-1) , (0,1)] :
                    new_row , new_col = curr_row + dr , curr_col + dc
                    if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 0 :
                        grid[new_row][new_col] = 1
                        queue.append((new_row , new_col))
                        


        for row in range(n) :
            for col in range(m) :
                if (row == 0 or row == n-1 or col == 0 or col == m-1) and grid[row][col] == 0 :
                    bfs(row , col)
        

        cnt = 0
        for row in range(1 , n-1) :
            for col in range(1 , m-1) :
                if grid[row][col] == 0 :
                    cnt += 1
                    bfs(row , col)
        
        return cnt