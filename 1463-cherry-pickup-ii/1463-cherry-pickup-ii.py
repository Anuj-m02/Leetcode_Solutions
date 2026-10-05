class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        
        n , m = len(grid) , len(grid[0])
        dirs = [-1 , 0 , 1]
        

        @lru_cache(maxsize=None)
        def dp(row , col1 , col2) :


            if row == n-1 :
                return 0
            
            ans = 0
            for dy1 in dirs :
                for dy2 in dirs :

            # for dx , dy in dirs :
                    new_row , new_col1 , new_col2 = row + 1 , col1 + dy1 , col2 + dy2
                    if 0 <= new_row < n and 0 <= new_col1 < m and 0 < new_col2 < m :
                        if (new_row , new_col1) != (new_row , new_col2) :
                            ans = max(ans , grid[new_row][new_col1] + grid[new_row][new_col2] + dp(new_row , new_col1 , new_col2))
                        
                        else :
                            ans = max(ans , grid[new_row][new_col1] + dp(new_row , new_col1 , new_col2))
            
            return ans
        
        if m > 1 :
            return dp(0 , 0 , m-1) + grid[0][0] + grid[0][m-1]
        
        else :
            return dp(0 , 0 , m-1) + grid[0][0]



