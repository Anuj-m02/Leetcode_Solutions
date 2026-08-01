from collections import defaultdict , deque , Counter
import heapq

from functools import lru_cache

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        n = len(nums)

        @lru_cache(maxsize = None)
        def dp(indx , rem):

            if indx == n :
                if rem == 0 :
                    return 0
                else :
                    return float("-inf")

            
            # option 1 skip
            not_take = dp(indx+1 , rem)

            new_rem = (rem + nums[indx])%3
            take = nums[indx] + dp(indx+1 , new_rem)

            return max(take , not_take)

        
        return dp(0,0)

            