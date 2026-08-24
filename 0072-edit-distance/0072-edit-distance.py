# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         m, n = len(word1), len(word2)
#         # dp[i][j] = min steps to convert word1[:i] to word2[:j]
#         dp = [[0] * (n + 1) for _ in range(m + 1)]

#         # base cases
#         for i in range(m + 1):
#             dp[i][0] = i  # delete all from word1
#         for j in range(n + 1):
#             dp[0][j] = j  # insert all to word1

#         # fill dp table
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 if word1[i - 1] == word2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = 1 + min(
#                         dp[i - 1][j - 1],  # replace
#                         dp[i - 1][j],      # delete
#                         dp[i][j - 1]       # insert
#                     )
        
#         return dp[m][n]
    
from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            # Base cases: if one string is exhausted, return length of the other
            if i == 0:
                return j
            if j == 0:
                return i
            
            # Characters match: move both pointers backward
            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)
            
            # Characters differ: try all 3 operations and take minimum + 1
            return 1 + min(
                dp(i - 1, j - 1),  # Replace
                dp(i - 1, j),      # Delete
                dp(i, j - 1)       # Insert
            )
        
        return dp(len(word1), len(word2))