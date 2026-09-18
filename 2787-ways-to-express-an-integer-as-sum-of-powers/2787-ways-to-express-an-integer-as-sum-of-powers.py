class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        # since n is upto 300 
        mod = int(1e9)+7

        @lru_cache(maxsize=None)
        def dp(total , num):


            if total == 0 :
                return 1

            if total < 0 or num**x > total:
                return 0
            
            take = dp(total - num**x , num+1)%mod
            skip = dp(total , num+1)%mod
            
            # ans = 0
            # for num in range(1 , 300) :
            #     if num**x > total :
            #         break
                
            #     else :
            #         ans += dp(total-num**x , x)%mod

            # return ans%mod

            return (take + skip)%mod
        
        return dp(n , 1)%mod

            


