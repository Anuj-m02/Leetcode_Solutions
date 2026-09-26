from fractions import Fraction
import heapq
from functools import lru_cache
from collections import defaultdict , deque  , Counter

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        

        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(indx , val) :

            if indx >= n :
                if val == k :
                    return 1
                else :
                    return 0
                

            
            ans1 ,ans2 , ans3 = 0 , 0 , 0
            ans1 = dp(indx+1  , val*nums[indx])
            ans2 = dp(indx+1 , Fraction(val , nums[indx]))
            ans3 = dp(indx+1 , val)

            return ans1+ans2+ans3
        
        return dp(0 , 1)