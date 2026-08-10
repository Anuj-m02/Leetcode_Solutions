from functools import lru_cache
from collections import defaultdict , deque , Counter
import heapq
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        n = len(power)

        # @lru_cache(None)
        # def dp(indx , s):

        #     if indx == n :
        #         return 0

        #     # not pick current_spell
        #     not_pick = dp(indx+1 , s)

        #     pick = float("-inf")
        #     # pick current spell but add in s
        #     a , b , c , d = power[indx]-2 , power[indx]-1 , power[indx]+1 , power[indx]+2
        #     if power[indx] not in s :
        #         pick = power[indx] + dp(indx+1 , s | frozenset([a,b,c,d]))

        #     return max(not_pick , pick)
        
        # return dp(0,frozenset())

        freq = Counter(power)
        unique = sorted(freq.keys())
        n = len(unique)

        @lru_cache(maxsize=None)
        def dp(indx) :
            if indx == n :
                return 0
            
            not_pick = dp(indx+1)

            nxt_indx = bisect.bisect_right(unique , unique[indx]+2)
            add = unique[indx]*freq[unique[indx]]
            pick = add + dp(nxt_indx)
        
            return max(not_pick , pick)
        
        return dp(0)
