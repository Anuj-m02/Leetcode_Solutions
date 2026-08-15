from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        
        mod = 10**9 + 7

        # at the k-1th pos we need the maximum val or later on

        @lru_cache(maxsize=None)
        def dp(indx , cost , max_val) :

            if indx == n :
                return 1 if cost == k else 0
            
            if cost > k :
                return 0
            
            total = 0

            for i in range(1 , m+1) :
                if i > max_val :
                    total += (dp(indx+1 , cost + 1 , i))%mod
                else :
                    total += (dp(indx+1 , cost , max_val))%mod
            
            return total%mod

            # # pick num <= curr_max_val
            # if max_val > 0 :
            #     total += (max_val * dp(indx+1 , cost , max_val ))%mod
            
            # # pick new number > max_val search cost + 1
            # for new_val in range(max_val + 1 , m+1 ):
            #     total += (dp(indx+1 , cost + 1 , new_val))%mod
            
            # return total
            
        return dp(0,0,0)

            


