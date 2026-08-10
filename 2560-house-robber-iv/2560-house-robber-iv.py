from collections import defaultdict , deque
import heapq
from functools import lru_cache


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        n = len(nums)
        low , high = 0 , max(nums)

        def check(mid) :
            @lru_cache(None)
            def dp(indx) :
                if indx >= n :
                    return 0
                
                not_pick = dp(indx+1)

                rob = 0
                if nums[indx] <= mid :
                    rob = 1 + dp(indx+2)
                
                return max(rob , not_pick)
            
            return dp(0) >= k




        ans = -1
        while low <= high :
            mid = (low+high)//2
            if check(mid) :
                ans = mid
                high = mid-1
            else :
                low = mid+1
        
        return ans

        # def dp(indx , k) :

        #     if indx == n and k <= 0 :
        #         return 0
        #     else :
        #         return float("-inf")
            
        #     # not rob
        #     not_pick = dp(indx+1 , k)
        #     #rob
        #     pick = max(nums[indx] , dp(indx+2 , k-1))

        #     return max(not_pick , pick)
        