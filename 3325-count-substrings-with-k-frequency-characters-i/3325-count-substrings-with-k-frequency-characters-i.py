from collections import defaultdict , deque ,Counter
import heapq
from functools import lru_cache

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:

        n = len(s)
        d = defaultdict(int)
        left , right = 0 , 0
        cnt = 0

        def check(d) :

            for key in d:
                if d[key] >= k :
                    return True
            return False

        while right < n :

            curr_char = s[right]

            d[curr_char] += 1
            
            while check(d) :
                cnt += (n-right)
                temp = s[left]
                d[temp] -= 1
                left += 1
            
            right += 1
        
        return cnt