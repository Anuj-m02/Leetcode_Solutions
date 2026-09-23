from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache
import bisect

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        m = len(offers)

        offers.sort()
        start = []
        for s,e,g in offers :
            start.append(s)
        # start , end , gold sorted on basis of sort

        @lru_cache(maxsize=None)
        def dp(indx) :

            if indx >= m :
                return 0
            
            nxt_indx = bisect.bisect_left(start , offers[indx][1] + 1)
            # either sell all the houses in the range start , end for gold
            sell = offers[indx][2] + dp(nxt_indx)

            not_sell = dp(indx+1)

            return max(sell , not_sell)
        
        return dp(0)


