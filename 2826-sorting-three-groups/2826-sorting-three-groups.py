from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n = len(nums)


        @lru_cache(maxsize=None)
        def dp(indx , prev) :

            if indx == n :
                return 0
            
            curr_num = nums[indx]

            op1 = float('inf')
            if curr_num >= prev :
                op1 = dp(indx+1 , curr_num)
            
            op2 = 1 + dp(indx+1  , prev)

            return min(op1 , op2)
        
        return dp(0, -1)