class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0 :
            return 1

        
        @lru_cache(maxsize=None)
        def dp(steps , vis) :

            if steps == 0 :
                return 1

            cnt = 0            
            for digit in range(0,10) :
                if digit not in vis :
                    cnt += dp(steps-1 , vis | {digit})
            
            return cnt
        
        ans = 1
        for length in range(1 , n+1) :
            for first_digit in range(1,10):
                ans += dp(length-1 , frozenset({first_digit}))
        
        return ans