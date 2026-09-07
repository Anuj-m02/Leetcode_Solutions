# # class Solution:
# #     def distinctSubseqII(self, s: str) -> int:
        

# #         n = len(s)
# #         mod = int(1e9)+7

# #         def dp(indx , vis , continued) :

# #             if indx == n :
# #                 return 0
            
# #             # not take
# #             not_take = dp(indx+1 ,vis)

# #             if s[indx] not in vis :

# #                 take = (1 + dp(indx+1 , frozenset()))%mod


# from functools import lru_cache

# class Solution:
#     def distinctSubseqII(self, s: str) -> int:
#         n = len(s)
#         MOD = 10**9 + 7

#         @lru_cache(maxsize=None)
#         def dp(indx: int, visited_at_level: frozenset) -> int:
#             if indx == n:
#                 return 0
            
#             char = s[indx]
            
#             # Option 1: Skip the current character
#             ans = dp(indx + 1, visited_at_level)
            
#             # Option 2: Pick the current character IF it hasn't been picked 
#             # as the starting option at this level yet.
#             if char not in visited_at_level:
#                 # 1 for the character itself 
#                 # + dp(indx + 1, frozenset()) to continue building further from the next index
#                 ans = (ans + 1 + dp(indx + 1, frozenset())) % MOD
                
#                 # Mark 'char' as visited for any future choices at this index level,
#                 # so we don't pick another occurrence of 'char' starting at this level.
#                 ans = (ans + dp(indx + 1, visited_at_level.union({char})) - dp(indx + 1, visited_at_level)) % MOD

#             return (ans + MOD) % MOD

#         return dp(0, frozenset())

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26  # dp[c] stores count of distinct subsequences ending with character c
        
        for char in s:
            idx = ord(char) - ord('a')
            # New subsequences created by appending 'char' = total current subsequences + 1
            dp[idx] = (sum(dp) + 1) % MOD
            
        return sum(dp) % MOD