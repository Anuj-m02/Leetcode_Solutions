from collections import defaultdict , deque, Counter
import heapq
from functools import lru_cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        length = len(strs)

        cnt = []
        for i in range(length):
            cnt_zero , cnt_one = strs[i].count("0") , strs[i].count("1")
            cnt.append((cnt_zero , cnt_one))

        @lru_cache(None)
        def dp(indx , ones , zeros) :
            
            if indx == length :
                return 0
            
            ans = float('-inf')
            # at each indx we have two options whether to pick it in subset or not

            not_pick = dp(indx+1 , ones ,zeros )

            pick = float("-inf")
            
            cnt_zero , cnt_one = cnt[indx]

            if cnt_zero <= zeros and cnt_one <= ones :
            
                pick = 1 + dp(indx+1 , ones-cnt_one , zeros-cnt_zero)

            return max(pick , not_pick)
        
        return dp(0,n,m)

