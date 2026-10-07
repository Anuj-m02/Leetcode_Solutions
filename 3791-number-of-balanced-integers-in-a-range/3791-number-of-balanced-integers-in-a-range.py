# class Solution:
#     def countBalanced(self, low: int, high: int) -> int:
        
#         m , n = len(str(low)) , len(str(high))

#         def count(num):
#             s = str(num)
#             n = len(s)

#             @lru_cache(maxsize=None)
#             def dp(indx , is_limit , is_lead , curr_even , curr_odd , length) : 

#                 if indx >= n : 
#                     if curr_even == curr_odd and length >= 2:
#                         return 1
#                     else :
#                         return 0

#                 res = 0

#                 upper = int(s[indx] if is_limit else 9)

#                 for digit in range(upper+1) :

#                     nxt_limit = is_limit and (digit == upper)

#                     if is_lead and digit == 0 :
#                         res += dp(indx+1 , nxt_limit , True , curr_even , curr_odd , 0)
                    
#                     else :
#                         pos = length + 1

#                         nxt_even = curr_even + (digit if pos%2 == 0 else 0)
#                         nxt_odd = curr_odd + (digit if pos%2 == 1 else 0)

#                         res += dp(indx+1 , nxt_limit , False , nxt_even , nxt_odd , length+1)
                
#                 return res
            
#             return dp(0 , True , True , 0 , 0 , 0)
    
#         return count(high) - count(low-1)

            

            

from functools import lru_cache

class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        
        def count(num: int) -> int:
            if num < 10:
                return 0
                
            s = str(num)
            n = len(s)

            # Max difference can be +/- 72, which is small enough for DP cache
            @lru_cache(maxsize=None)
            def dp(indx: int, is_limit: bool, is_lead: bool, diff: int, is_odd_pos: bool) -> int:
                if indx == n:
                    # Valid if digit sums cancel out (diff == 0) and it was not all leading zeros
                    return 1 if (diff == 0 and not is_lead) else 0

                res = 0
                upper = int(s[indx]) if is_limit else 9

                for digit in range(upper + 1):
                    next_limit = is_limit and (digit == upper)
                    
                    if is_lead and digit == 0:
                        # Leading zeros: state remains unplaced, parity doesn't flip yet
                        res += dp(indx + 1, next_limit, True, 0, True)
                    else:
                        # Add digit to odd or subtract from even sum
                        next_diff = diff + digit if is_odd_pos else diff - digit
                        res += dp(indx + 1, next_limit, False, next_diff, not is_odd_pos)

                return res

            return dp(0, True, True, 0, True)

        return count(high) - count(low - 1)