class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        s = str(n)
        m = len(s)
        
        # indx upto 9 , vis 2^10 digits 1024  , started 2
        @lru_cache(maxsize=None)
        def dp(indx  , vis , started , has_dup , is_limit) :
            if indx == m :
                return 1 if (started and has_dup) else 0
            
            # print(indx , vis , started)
            ans = 0
            limit = int(s[indx]) if is_limit else 9

            if not started :
                ans += dp(indx+1 , vis , False , False , False)

            low = 0 if started else 1
            for digits in range(low,limit+1) :

                nxt_limit = is_limit and (digits == limit)

                if digits in vis :
                    ans += dp(indx+1 , vis , True , True , nxt_limit)

                else :
                    ans += dp(indx+1 , vis | frozenset({digits}) , True , has_dup , nxt_limit)
            
            return ans
        
        return dp(0 , frozenset() , False , False , True) 
