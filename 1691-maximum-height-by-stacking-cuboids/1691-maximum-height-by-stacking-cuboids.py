from functools import lru_cache
from collections import defaultdict , deque , Counter
import heapq

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        
        n = len(cuboids)

        for i in range(n) :
            a , b , c = cuboids[i]
            cuboids[i].sort(reverse=True)
        
        cuboids.sort(reverse=True)

        @lru_cache(maxsize=None)
        def dp(indx , a , b , c) :

            if indx == n :
                return 0
            
            
            #op1 dont take this cuboid
            op1 = dp(indx+1 , a , b , c)

            #op2 take this cuboid
            op2 = float("-inf")
            curr_a , curr_b , curr_c = cuboids[indx]
            if curr_a <= a and curr_b <= b and curr_c <= c :
                op2 = curr_a + dp(indx+1 , curr_a , curr_b , curr_c)
            
            return max(op1 , op2)
        
        return dp(0  , float("inf") , float("inf") , float("inf"))

