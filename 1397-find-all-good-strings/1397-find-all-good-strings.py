from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:

        
        m = len(evil)
        mod = 10**9 + 7

        def get_nxt_evil(evil_indx , curr_char) :

            curr_str = evil[:evil_indx] + curr_char

            for length in range(min(len(curr_str) , m) , 0 , -1) :
                if evil.startswith(curr_str[-length :]) :
                    return length
            
            return 0


        @lru_cache(maxsize=None)
        def dp(indx , evil_indx , tight1 , tight2) :

            if evil_indx == m :
                return 0
            
            if indx == n :
                return 1
            
            if tight1 :
                low = s1[indx]
            else :
                low = "a"
            
            if tight2 :
                high = s2[indx]
            else :
                high = "z"
            
            total = 0

            for i in range(ord(low) , ord(high) + 1):
                curr_char = chr(i)

                nxt_evil_indx = get_nxt_evil(evil_indx , curr_char)

                nxt_tight1 = tight1 and (curr_char == low)
                nxt_tight2 = tight2 and (curr_char == high)

                total += dp(indx+1 , nxt_evil_indx , nxt_tight1 , nxt_tight2) % mod

            return total%mod

        return dp(0 ,0 ,True , True) 