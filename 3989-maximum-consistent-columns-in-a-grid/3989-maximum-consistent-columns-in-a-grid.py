class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        
        n , m = len(grid) , len(grid[0])

        @lru_cache(maxsize=None)
        def dp(col_indx , prev_indx) :

            if col_indx >= m :
                return 0
            
            op1 = dp(col_indx +1 , prev_indx)

            # check whether we can pcik this col_indx or not
            if prev_indx == -1 :
                op2 = 1 + dp(col_indx+1 , col_indx)
            else :
                op2 = 0
                chk = True
                for row in range(n) :
                    if abs(grid[row][col_indx] - grid[row][prev_indx]) > limit :
                        chk = False
                        break
                
                if chk :
                    op2 = 1+dp(col_indx+1 , col_indx)
            
            return max(op1 , op2)
        
        return dp(0 , -1)
