from collections import defaultdict , deque
import heapq
from functools import lru_cache


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        n = len(nums)
        low , high = 0 , max(nums)

        def check(mid) :
            cnt = 0
            indx = 0 
            while indx < n :
                if nums[indx] <= mid :
                    cnt += 1
                    indx += 2
                else :
                    indx += 1
            
            return cnt >= k


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
        