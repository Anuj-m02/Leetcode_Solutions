# class Solution:
#     def sumOfPower(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         nums.sort()
#         mod = int(1e9) + 7

#         @lru_cache(maxsize=None)
#         def dp(indx , started , ended) :
            
#             if ended :
#                 return 1
            
#             if indx >= n :
#                 return 0

#             ans = 0
#             if not started :
#                 ans = (dp(indx+1 , False , False)) + (nums[indx]*dp(indx+1 , True , False))
#             # not take this indx

#             else :
#                # alrdy started do we wish to end here or not 
#                # continue and not take this indx
#                 ans += dp(indx+1 , True , False)%mod
#                 # continue but take this indx
#                 ans += dp(indx+1 , True , False)%mod
#                 # end at this indx

#                 ans += (nums[indx]**2)*(dp(indx+1 , True , True))%mod
            
#             return ans%mod
        
#         return dp(0 , False , False)



from functools import lru_cache
from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mod = int(1e9) + 7

        @lru_cache(maxsize=None)
        def dp(indx, started, ended):
            if ended:
                return 1

            if indx >= n:
                return 0

            ans = 0

            if not started:
                # Skip nums[indx]
                ans = dp(indx + 1, False, False)

                # Start a group: nums[indx] is its minimum
                ans += nums[indx] * dp(indx + 1, True, False)

                ans += nums[indx]**3 * dp(indx+1 , True , True)

            else:
                # Skip nums[indx]
                ans += dp(indx + 1, True, False)

                # Take nums[indx] as an interior element
                ans += dp(indx + 1, True, False)

                # End the group: nums[indx] is its maximum
                ans += (nums[indx] ** 2) * dp(indx + 1, True, True)

            return ans % mod

        return dp(0, False, False)
