class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        mod = int(1e9)+7

        @lru_cache(maxsize=None)
        def dp(zero_left , one_left , last_bit) :
            
            if zero_left == 0 and one_left == 0 :
                return 1
            
            ans = 0

            if last_bit == 1 :
                for k in range(1 , min(zero_left , limit) + 1) :
                    ans += dp(zero_left-k , one_left , 0) % mod
            
            elif last_bit == 0 :
                for k in range(1 , min(one_left , limit) + 1) :
                    ans += dp(zero_left , one_left - k , 1) % mod
            
            return ans % mod
        
        total = dp(zero , one , 0) % mod + dp(zero , one , 1)%mod

        return total%mod
