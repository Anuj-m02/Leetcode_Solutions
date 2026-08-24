class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n , m = len(obstacleGrid) ,len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 :
            return 0

        @cache
        def dp(row , col) :
            if row == n-1 and col == m-1 :
                if obstacleGrid[row][col] == 0 :
                    return 1
                else :
                    return 0
            
            right , down = 0 , 0
            if col < m-1 :
                if obstacleGrid[row][col+1] == 0 :
                    right = dp(row , col+1)
            
            if row < n-1 :
                if obstacleGrid[row+1][col] == 0 :
                    down = dp(row+1 , col)
            
            return right + down

        return dp(0,0)
            

        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # dp = [[0]*n for _ in range(m)]
        # #return self.f(m-1,n-1,dp)
        # if obstacleGrid[m-1][n-1] == 1 :
        #     return 0
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0 :
        #             dp[i][j] = 1
        #         else :
        #             up , left = 0,0
        #             if i > 0 and obstacleGrid[i-1][j] == 0:
        #                 up = dp[i-1][j]
        #             if j > 0 and obstacleGrid[i][j-1] == 0:
        #                 left = dp[i][j-1]
        #             dp[i][j] = up + left
        # return dp[m-1][n-1]