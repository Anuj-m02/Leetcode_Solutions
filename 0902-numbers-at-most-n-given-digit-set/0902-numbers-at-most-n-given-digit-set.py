# class Solution:
#     def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
#         n = len(digits)

#         @lru_cache(maxsize=None)
#         def dp(indx , string) :

#             if indx == n :
#                 if string and int(string) <= n:
#                     return 1
#                 else :
#                     return 0

            
#             # at this indx we have option to choose this indx
#             not_pick = dp(indx+1 , string)

#             # pick
#             pick1 = dp(indx+1 , string + digits[indx])
#             pick2 = dp(indx , string + digits[indx])

#             return pick1 + pick2 + not_pick
        
#         return dp(0 , "")

from functools import lru_cache
from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        s = str(n)
        k = len(s)

        @lru_cache(maxsize=None)
        def dp(indx , is_less , is_started) :
            
            if indx == k :
                if is_started :
                    return 1
                else :
                    return 0
            
            ans = 0
            # option 1 skip digit
            if not is_started :
                ans += dp(indx+1 , True , False)
            
            # option2   try picking availbale digit
            if is_less :
                limit = "9"
            else :
                limit = s[indx]
            
            for d in digits :
                if d > limit :
                    break
                nxt_less = is_less or (d < limit)
                ans += dp(indx+1 , nxt_less , True)
            
            return ans
        
        return dp(0 , False , False)

        # target_n = n
        # max_len = len(str(target_n))
        # valid_numbers = set()

        # def dfs(current_str: str):
        #     if current_str:
        #         if int(current_str) <= target_n:
        #             valid_numbers.add(current_str)
        #         else:
        #             return  # Stop expanding if current number exceeds target_n

        #     if len(current_str) == max_len:
        #         return

        #     # Try adding each allowed digit to the current string position
        #     for d in digits:
        #         dfs(current_str + d)

        # dfs("")
        # return len(valid_numbers)