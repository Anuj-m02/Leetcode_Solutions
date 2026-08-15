from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, string: str) -> int:
        
        s = set(string)
        d = defaultdict(int)

        left , right = 0 , 0

        res = -1

        for right , char in enumerate(string) :

            d[char] += 1
            while d[char] > 2  :
                d[string[left]] -= 1
                left += 1
            
            res = max(res , right-left+1)

        return res