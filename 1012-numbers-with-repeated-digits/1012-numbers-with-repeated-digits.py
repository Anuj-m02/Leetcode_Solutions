# class Solution:
#     def numDupDigitsAtMostN(self, n: int) -> int:

#         s = str(n)
#         m = len(s)
        
#         # indx upto 9 , vis 2^10 digits 1024  , started 2
#         @lru_cache(maxsize=None)
#         def dp(indx  , vis , started , has_dup , is_limit) :
#             if indx == m :
#                 return 1 if (started and has_dup) else 0
            
#             # print(indx , vis , started)
#             ans = 0
#             limit = int(s[indx]) if is_limit else 9

#             if not started :
#                 ans += dp(indx+1 , vis , False , False , False)

#             low = 0 if started else 1
#             for digits in range(low,limit+1) :

#                 nxt_limit = is_limit and (digits == limit)

#                 if digits in vis :
#                     ans += dp(indx+1 , vis , True , True , nxt_limit)

#                 else :
#                     ans += dp(indx+1 , vis | frozenset({digits}) , True , has_dup , nxt_limit)
            
#             return ans
        
#         return dp(0 , frozenset() , False , False , True) 

from functools import lru_cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        m = len(s)
        
        # Eliminates has_dup state entirely
        @lru_cache(maxsize=None)
        def dp(indx, vis, started, is_limit):
            if indx == m:
                # Return 1 for every valid unique-digit number constructed
                return 1 if started else 0
            
            ans = 0
            limit = int(s[indx]) if is_limit else 9
            
            # Option to leave this position blank if not started
            if not started:
                ans += dp(indx + 1, vis, False, False)
            
            low = 0 if started else 1
            for digit in range(low, limit + 1):
                # Skip duplicate digits completely
                if digit not in vis:
                    nxt_limit = is_limit and (digit == limit)
                    ans += dp(indx + 1, vis | frozenset({digit}), True, nxt_limit)
            
            return ans
        
        # Total numbers from 1 to N minus numbers with unique digits
        return n - dp(0, frozenset(), False, True)