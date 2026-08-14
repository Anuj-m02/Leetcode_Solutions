from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        n = len(nums)

        mod = int(1e9 + 7)

        @lru_cache(maxsize=None)
        def dp(indx , cnt) :

            if indx == n :
                if cnt == 1:
                    return 1
                else :
                    return 0

            curr_val = nums[indx]

            # each indx if zero whether to continue or break and start
            ans = 0
            if curr_val == 0 :
                if cnt == 0 :
                    ans = dp(indx+1 , cnt)
                elif cnt == 1 :
                    ans = (dp(indx+1 , 1) + dp(indx+1 , 0))%mod

            else :
                # if val is 1 , and cnt less than 1 then we can increase and cut or just contiune
                if cnt == 0 :
                    ans = (dp(indx+1 , 1))
                elif cnt == 1 :
                    ans = dp(indx+1 , 1)
            
            return ans
        
        return dp(0,0)



