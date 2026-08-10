from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        # prev = 0 even , 1 odd , 2 continuing
        n = len(nums)
        for indx in range(n) :
            nums[indx] = nums[indx]%2
        
        # now nums is either 0 or 1 
        # even even , even odd , odd even , odd odd

        # all evens
        @lru_cache(None)
        def dp1(indx):

            if indx == n :
                return 0
            
            not_pick = dp1(indx+1)
            pick = float("-inf")
            if nums[indx] == 0 :
                pick = 1 + dp1(indx+1)
            
            return max(pick , not_pick)

        # all odds
        @lru_cache(None)
        def dp2(indx):

            if indx == n :
                return 0
            
            not_pick = dp2(indx+1)
            pick = float("-inf")
            if nums[indx] == 1 :
                pick = 1 + dp2(indx+1)
            
            return max(pick , not_pick)
        
        @lru_cache(None)
        def dp3(indx , prev) :

            if indx == n :
                return 0
            not_pick = dp3(indx+1 , prev)
            pick = float("-inf")
            if prev != nums[indx] :
                pick = 1 + dp3(indx+1 , nums[indx])
            
            return max(not_pick , pick)
        

        ans1 , ans2 , ans3 = dp1(0) , dp2(0) , dp3(0,-1)
        return max(ans1 , ans2 , ans3)

