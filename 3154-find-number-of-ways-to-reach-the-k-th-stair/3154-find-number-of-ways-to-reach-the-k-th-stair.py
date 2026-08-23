class Solution:
    def waysToReachStair(self, k: int) -> int:
        
        
        @lru_cache(maxsize=None)
        def dp(stair , jump , prev_down) :

            if stair > k+1 :
                return 0

            if stair == k :
                ans = 1
            else :
                ans = 0 
            
            # ans = 0
            ans += dp(stair + 2**jump , jump+1 , 0)

            if not prev_down and stair > 0 :
                ans += dp(stair-1 , jump , 1)
            
            return ans
            
            # op1 , op2 = 0 , 0
            # if stair == 0 :
            #     op1 = 1 + dp(stair + 2^jump , jump+1 , 1)
            
            # if prev == 0 :
            #     op1 = 1 + dp(stair + 2^jump , jump+1 , 1)
            
            # else :
            #     op1 = 1 + dp(stair + 2^jump , jump+1 , 1)
            #     op2 = 1 + dp(stair-1 , jump , 0)
            
            # return op1+op2
        
        return dp(1 , 0 , 0)