class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        
        n , m = len(grid) , len(grid[0])

        mod = int(1e9) + 7

        def help(row , col , direction) :
            while 0 <= row < n and 0 <= col < m and grid[row][col] == 1 :
                if direction == "R" :
                    row += 1
                    direction = "D"
                
                else :
                    col += 1
                    direction = "R"
            
            return row , col

        @lru_cache(maxsize=None)
        def dp(row , col) :

            if row < 0 or col < 0 :
                return 0
            
            if row >= n or col >= m :
                return 0
            
            if row == n-1 and col == m-1 :
                return 1
            

            curr_cell = grid[row][col]
            ans = 0

            # move right
            if col + 1 < m :
                next_cell = grid[row][col+1]
                if next_cell == 0 :
                    ans += dp(row , col+1)%mod
                
                else :
                    # moving rigth and mirror occured so moving down
                    nr , nc = help(row+1 , col+1 , "D")
                    ans += dp(nr ,nc)%mod
            

            # move down
            if row+1 < n :
                next_cell = grid[row+1][col]
                if next_cell == 0 :
                    ans += dp(row+1 , col)%mod
                
                else :
                    # moving down and mirror occured so moving right
                    nr , nc = help(row+1 , col+1 , "R")
                    ans += dp(nr , nc)%mod
            
            return ans%mod
        
        return dp(0 , 0)%mod

