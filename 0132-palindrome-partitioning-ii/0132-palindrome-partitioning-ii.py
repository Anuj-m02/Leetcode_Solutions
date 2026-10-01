class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)

        is_pal = [[False]*n for _ in range(n)]
        for length in range(1 , n+1) :
            for i in range(n-length+1) :
                j = i + length - 1
                if s[i] == s[j] :
                    if length <= 2 or is_pal[i+1][j-1] :
                        is_pal[i][j] = True
            
        @lru_cache(maxsize=None)
        def dp(indx) :

            if is_pal[indx][n-1] :
                return 0
            
            min_cuts = float("inf")
            
            for j in range(indx , n) :
                if is_pal[indx][j] :
                    min_cuts = min(min_cuts , 1 + dp(j+1))
            
            return min_cuts
        
        return dp(0)