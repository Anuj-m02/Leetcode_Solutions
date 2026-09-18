from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        
        d = Counter(s)
        n = len(s)
        first = [n]*(26)
        last = [-1]*(26)

        for indx , char in enumerate(s) :
            c = ord(char)-ord("a")
            first[c] = min(first[c] , indx)
            last[c] = indx
        
        intervals = []

        for c in range(26) :
            if last[c] == -1 :
                continue
            left , right = first[c] , last[c]
            valid = True

            indx = left
            while indx <= right :
                x = ord(s[indx]) - ord("a")

                if first[x] < left :
                    valid = False
                    break
                right = max(right , last[x])
                indx += 1
            
            if valid :
                intervals.append((right , left))
        
        intervals.sort()
        ans = []
        prev_end = -1
        
        for right , left in intervals :
            if left > prev_end :
                ans.append(s[left:right+1])
                prev_end = right
        
        return ans
