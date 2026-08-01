from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def chk(num) :
            
            s = str(num)
            n = len(s)

            cnt = 0

            if n < 3 :
                return cnt

            for indx in range(1,n-1):
                if s[indx-1] < s[indx] and s[indx+1] < s[indx] :
                    cnt += 1
                if s[indx-1] > s[indx] and s[indx+1] > s[indx] :
                    cnt += 1

            return cnt



        ans = 0
        for num in range(num1 , num2+1) :
            ans += chk(num)
        
        return ans