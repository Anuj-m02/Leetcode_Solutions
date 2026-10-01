class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        
        n , m = len(grid) , len(grid[0])

        @lru_cache(maxsize=None)
        def dp(row , prev_col)  :

            if row >= n :
                return 0
            
            ans = float("inf")

            for col in range(m) :
                if col != prev_col :
                    ans = min(ans , grid[row][col] + dp(row+1 , col))

            return ans

        return dp(0 , -1) 
