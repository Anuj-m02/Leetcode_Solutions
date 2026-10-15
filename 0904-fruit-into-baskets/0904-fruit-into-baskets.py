from collections import Counter
class Solution:
    def totalFruit(self, s: List[int]) -> int:
        # if len(s) == 1 :
        #     return 1
        # if len(s) == 2 :
        #     return 2
        left = 0
        right = 0
        n = len(s)
        d = Counter()
        cnt = 0
        maxi = -1
        for right in range(n):
            d[s[right]] += 1
            if d[s[right]] == 1 :
                cnt += 1
            while cnt > 2 :
                d[s[left]] -= 1
                if d[s[left]] == 0 :
                    del d[s[left]]
                    cnt -= 1
                left += 1
            if cnt <= 2 :
                maxi = max(maxi , right-left+1)
        return maxi
