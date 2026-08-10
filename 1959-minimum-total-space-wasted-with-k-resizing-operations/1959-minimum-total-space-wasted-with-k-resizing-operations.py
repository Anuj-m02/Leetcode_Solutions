from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:

        n = len(nums)

        if k == 0 :
            maxi = max(nums)
            total = 0
            for i in range(n):
                total += (maxi - nums[i])
            
            return total
        
        # maxi = max(nums)
        @lru_cache(None)
        def dp(indx , k_left ):

            if indx == n :
                if k_left >= -1 :
                    return 0
                else :
                    return float("inf")
            
            # now at each indx we have option to change size arr to its curr_num
            ans = float("inf")
            maxi = 0
            total = 0
            for j in range(indx , n):
                maxi = max(maxi , nums[j])
                total += nums[j]

                length = j-indx+1
                temp = (length*maxi)-total
                ans = min(ans , temp + dp(j+1 , k_left-1))
            
            return ans

        
        return dp(0,k)

