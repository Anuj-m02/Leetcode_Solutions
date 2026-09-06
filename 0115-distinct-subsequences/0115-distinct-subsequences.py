class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache
        n, m = len(s), len(t)

        @lru_cache(None)
        def count(i, j):
            if j == m:
                return 1  # matched all of t
            if i == n:
                return 0  # s exhausted

            if s[i] == t[j]:
                # Take s[i] or skip it
                return count(i + 1, j + 1) + count(i + 1, j)
            else:
                return count(i + 1, j)

        return count(0, 0)
