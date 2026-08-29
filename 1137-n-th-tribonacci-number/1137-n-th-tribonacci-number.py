class Solution:
    def tribonacci(self, n: int) -> int:


        
        @lru_cache(maxsize=None)
        def dp(curr_n) :

            if curr_n == 0 :
                return 0
            if curr_n == 1 :
                return 1
            if curr_n == 2 :
                return 1
            

            return dp(curr_n-1) + dp(curr_n-2) + dp(curr_n-3)
        
        return dp(n)