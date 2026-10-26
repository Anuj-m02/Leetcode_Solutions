from typing import List
from functools import lru_cache

class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(i: int, taken: int) -> int:
            if i >= n:
                return 0

            # Option 1: Skip nums[i]
            ans = dp(i + 1, 0)

            # Option 2: Use s[i] to cover nums[i] (if s[i] == '1' and not already used)
            if s[i] == '1' and not taken:
                ans = max(ans, nums[i] + dp(i + 1, 0))

            # Option 3: Borrow s[i + 1] to cover nums[i] (if s[i + 1] == '1')
            if i + 1 < n and s[i + 1] == '1':
                ans = max(ans, nums[i] + dp(i + 1, 1))

            return ans

        return dp(0, 0)
# class Solution:
#     def maxTotal(self, nums: List[int], s: str) -> int:
        
#         n = len(nums)

#         left , right = None , None
#         pos = []
#         for indx in range(n) :
#             if s[indx] == "1" :
#                 # if not left :
#                 #     left = indx

#                 # if not right :
#                 #     right = indx

#                 pos.append(indx)
        
#         num_tokens = len(pos)
        
#         # if left == right :
#         #     return max(nums[:right+1])
        


#         @lru_cache(maxsize=None)
#         def dp(indx , prev_cov) :

#             if indx >= num_tokens :
#                 return 0

#             i = pos[indx]

#             #leave token at indx i
#             val1 = nums[i] if i != prev_cov else 0
#             res1 = val1 + dp(indx+1 , i)
            
#             # move token to i-1
#             res2 = 0
#             if i > 0 :
#                 val2 = nums[i-1] if (i-1) != prev_cov else 0
#                 res2 = val2 + dp(indx+1 , i-1)
            
#             return max(res1 , res2)
        
#         return dp(0 , -1)
            
#             # if s[indx+1] == "1" :
#             #     ans = max(ans , nums[indx] + dp(indx+1 , 0) , nums[indx+1] + dp(indx+1 , 1))

            
