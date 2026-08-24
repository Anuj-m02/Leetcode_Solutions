from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        @lru_cache(None)
        def match(i: int, j: int) -> bool:
            # Base Cases
            if i == n and j == m:
                return True
            if j == m:
                return False
            if i == n:
                return all(x == "*" for x in p[j:])

            # Match transitions
            if p[j] == s[i] or p[j] == "?":
                return match(i + 1, j + 1)
            elif p[j] == "*":
                # Option 1: match empty character (advance pattern index j)
                # Option 2: match one character from s (advance string index i)
                return match(i, j + 1) or match(i + 1, j)
            else:
                return False

        return match(0, 0)


from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def match(i , j):
            if i == 0  and j == 0 :
                return True
            if j == 0 :
                return False
            if i == 0 :
                return all(x == "*" for x in p[:j])

            if p[j-1] == s[i-1] or p[j-1] == "?" :
                return match(i-1,j-1)
            elif p[j-1] == "*" :
                return match(i,j-1) or match(i-1,j)
            else :
                return False
        return match(len(s),len(p))