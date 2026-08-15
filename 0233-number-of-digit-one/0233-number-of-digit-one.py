from collections import defaultdict , deque  , Counter
import heapq
from functools import lru_cache


class Solution:
    def countDigitOne(self, n: int) -> int:

        if n == 0 :
            return 0
        
        s = str(n)
        length = len(s)
        
        # n is going from 0 to 1e9 so  9 poistion and at each pos we can have digit 1 
        # once every 10 num , 10 times in 100 , 100 in 1000 , 10000 in 10k

        @lru_cache(None)
        def dp(indx , count , is_less) :

            if indx == length :
                return count
            
            total_ones = 0
            if is_less :
                limit = 9
            else :
                limit = int(s[indx])
            
            for digit in range(limit+1):
                new_count = count + (1 if digit == 1 else 0)
                new_is_less = is_less or (digit < limit)

                total_ones += dp(indx+1 , new_count , new_is_less)
            
            return total_ones
        
        return dp(0,0,False)
