class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        
        n ,m  = len(matrix) , len(matrix[0])

        @lru_cache(maxsize=None)
        def dp(row , col) :

            if row < 0 or col < 0 or matrix[row][col] == 0 :
                return 0
            

            ans = 1 + min(dp(row-1 , col) , dp(row , col-1),
                        dp(row-1 , col-1)) 
                        
            return ans
        

        total_sq = 0
        for row in range(n) :
            for col in range(m) :
                total_sq += dp(row ,col)
        
        return total_sq