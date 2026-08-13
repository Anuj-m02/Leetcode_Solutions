from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)

        def check(string) :
            
            rev_str = string[::-1]
            cnt = 0
            for i in range(len(string)) :
                if string[i] != rev_str[i] :
                    cnt += 1
            return cnt//2


        @lru_cache(maxsize=None)
        def dp(indx , k_left , prev_indx) :

            if indx == n :
                if k_left == 0 and prev_indx == n :
                    return 0
                else :
                    return float('inf')
            
            if k_left <= 0 :
                return float('inf')
            
            # dont partition at this indx
            temp1 = dp(indx+1 , k_left , prev_indx)

            # partition at this indx

            temp2 = float("inf")
            substring = s[prev_indx:indx+1]

            cnt = check(substring)
            temp2 = cnt + dp(indx+1 , k_left-1 , indx+1)

            return min(temp1 , temp2)
        
        return dp(0 , k , 0)


