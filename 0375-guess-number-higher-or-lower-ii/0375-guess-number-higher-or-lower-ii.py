from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:

        @lru_cache(None)
        def dp(left , right) :

            if left >= right :
                return 0
            
            ans = float("inf")
            for num in range(left , right+1) :
                low = dp(left , num-1)
                high = dp(num+1 , right)
                ans = min(ans , num + max(low , high))
            
            return ans
        
        return dp(0,n)
