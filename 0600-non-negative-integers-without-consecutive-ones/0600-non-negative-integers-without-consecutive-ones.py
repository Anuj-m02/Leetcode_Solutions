class Solution:
    def findIntegers(self, n: int) -> int:
        
        s = bin(n)[2:]
        m = len(s)

        @lru_cache(maxsize=None)
        def dp(indx , prev_is_one , is_tight) :

            if indx >= m :
                return 1

            if is_tight :
                limit = int(s[indx])
            else :
                limit = 1
            
            ans = 0

            for digit in range(limit+1):
                if prev_is_one and digit == 1 :
                    continue

                nxt_tight = is_tight and (digit == limit)
                nxt_prev_one = (digit == 1)

                ans += dp(indx+1 , nxt_prev_one , nxt_tight)

            return ans

        return dp(0 , False , True) 
