class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        mod = int(1e9) + 7

        @lru_cache(maxsize=None)
        def dp(indx) :

            if indx == 0 :
                return 1
            
            if indx < 0 :
                return 0
            
            # place "0" zero times
            ans1 = dp(indx-zero)%mod
            ans2 = dp(indx-one)%mod
            return (ans1+ans2)%mod


        # since both includesive high and low 
        # return dp(high+1)%mod - dp(low-1)%mod
        cnt = 0
        for length in range(low , high+1) :
            cnt += dp(length)%mod
        
        return cnt%mod