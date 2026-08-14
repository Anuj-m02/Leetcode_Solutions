from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache
import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        n , m = len(arr1) , len(arr2)
        arr2.sort()


        @lru_cache(maxsize=None)
        def dp(indx , prev_val):

            if indx == n :
                return 0
            
            curr_val = arr1[indx]
            cost = float("inf")

            # if curr_val > prev_val , we can skip
            # if curr_val < prev_val replace from arr2

            if curr_val > prev_val :
                cost = min(cost ,  dp(indx+1 , curr_val))

            pos = bisect.bisect_right(arr2 , prev_val)

            if pos < m :
                cost = min(cost , 1 + dp(indx+1 , arr2[pos]))
            
            return cost
        
        ans = dp(0,-1)

        if ans == float("inf") :
            return -1
        return ans
             
            

