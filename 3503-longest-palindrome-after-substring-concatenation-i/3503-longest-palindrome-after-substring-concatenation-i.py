# # # # from collections import defaultdict , deque , Counter
# # # # import heapq
# # # # from functools import lru_cache


# # # # class Solution:
# # # #     def longestPalindrome(self, s: str, t: str) -> int:

# # # #         n , m = len(s) , len(t)

# # # #         @lru_cache
# # # #         def dp1(indx1 , indx2) :

# # # #             if indx1 >= n or indx2 < 0 :
# # # #                 return 0
            
# # # #             res = float("-inf")
# # # #             if s[indx1] == t[indx2] :
# # # #                 res = max(res , 2 + dp1(indx1+1 , indx2-1 ))
            
# # # #             res = max(res , dp1(indx1 + 1 , indx2))
# # # #             res = max(res , dp1(indx1 , indx2 - 1))

# # # #             return res
        

# # # #         @lru_cache
# # # #         def dp2(indx1 , indx2) :

# # # #             if indx1 >= n or indx2 < 0 :
# # # #                 return 0
            
# # # #             res = float("-inf")
# # # #             if s[indx1] == s[indx2] :
# # # #                 res = max(res , 2 + dp2(indx1+1 , indx2-1 ))
            
# # # #             res = max(res , dp2(indx1 + 1 , indx2))
# # # #             res = max(res , dp2(indx1 , indx2 - 1))

# # # #             return res
        
# # # #         @lru_cache
# # # #         def dp3(indx1 , indx2) :

# # # #             if indx1 >= m or indx2 < 0 :
# # # #                 return 0
            
# # # #             res = float("-inf")
# # # #             if t[indx1] == t[indx2] :
# # # #                 res = max(res , 2 + dp3(indx1+1 , indx2-1 ))
            
# # # #             res = max(res , dp3(indx1 + 1 , indx2))
# # # #             res = max(res , dp3(indx1 , indx2 - 1))

# # # #             return res
        
# # # #         return max(dp1(0,m-1) , dp2(0 , n-1) , dp3(0 , m-1))

# # # from functools import lru_cache

# # # class Solution:
# # #     def longestPalindrome(self, s: str, t: str) -> int:
# # #         n, m = len(s), len(t)

# # #         # LPS for a single string string (s or t)
# # #         @lru_cache(None)
# # #         def lps(string: str, indx1: int, indx2: int) -> int:
# # #             if indx1 > indx2:
# # #                 return 0
# # #             if indx1 == indx2:
# # #                 return 1
            
# # #             if string[indx1] == string[indx2]:
# # #                 return 2 + lps(string, indx1 + 1, indx2 - 1)
            
# # #             return max(lps(string, indx1 + 1, indx2), lps(string, indx1, indx2 - 1))

# # #         # Cross DP: Finds longest palindrome formed by pairing s[indx1] and t[indx2]
# # #         @lru_cache(None)
# # #         def dp1(indx1: int, indx2: int) -> int:
# # #             if indx1 >= n or indx2 < 0:
# # #                 return 0
            
# # #             res = 0
# # #             # Choice 1: Skip character in s
# # #             res = max(res, dp1(indx1 + 1, indx2))
            
# # #             # Choice 2: Skip character in t
# # #             res = max(res, dp1(indx1, indx2 - 1))

# # #             # Choice 3: Match characters from s and t
# # #             # When we find a valid match (s[indx1] == t[indx2]), we can either:
# # #             # 1. Continue pairing across s and t -> 2 + dp1(indx1 + 1, indx2 - 1)
# # #             # 2. Transition into single-string LPS for leftover s or leftover t in the middle
# # #             if s[indx1] == t[indx2]:
# # #                 match_res = 2 + dp1(indx1 + 1, indx2 - 1)
# # #                 leftover_s = 2 + lps(s, indx1 + 1, n - 1)
# # #                 leftover_t = 2 + lps(t, 0, indx2 - 1)
                
# # #                 res = max(res, match_res, leftover_s, leftover_t)

# # #             return res

# # #         return dp1(0, m - 1)

# # from functools import lru_cache

# # class Solution:
# #     def longestPalindrome(self, s: str, t: str) -> int:
# #         n, m = len(s), len(t)
# #         A = s + t
# #         total_len = n + m
# #         ans = 0

# #         @lru_cache(None)
# #         def lps(i: int, j: int) -> int:
# #             nonlocal ans
# #             if i > j:
# #                 return 0
# #             if i == j:
# #                 return 1

# #             if A[i] == A[j]:
# #                 res = 2 + lps(i + 1, j - 1)
# #                 # Valid match ONLY if i is in string 's' and j is in string 't'
# #                 if i < n and j >= n:
# #                     ans = max(ans, res)
# #                 return res

# #             return max(lps(i + 1, j), lps(i, j - 1))

# #         lps(0, total_len - 1)
# #         return ans

# class Solution:
#     def longestPalindrome(self, s: str, t: str) -> int:
#         n, m = len(s), len(t)
#         A = s + t
#         total = n + m
        
#         # dp[i][j] stores the LPS length for substring A[i...j]
#         dp = [[0] * total for _ in range(total)]
        
#         # Base cases
#         for i in range(total):
#             dp[i][i] = 1
            
#         ans = 0
        
#         # Fill DP table bottom-up
#         for i in range(total - 1, -1, -1):
#             for j in range(i + 1, total):
#                 if A[i] == A[j]:
#                     dp[i][j] = 2 + dp[i + 1][j - 1]
#                     # Update max length ONLY if s[i] and t[j] match across boundaries
#                     if i < n and j >= n:
#                         ans = max(ans, dp[i][j])
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
#         return ans

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def is_palindrome(str_val: str) -> bool:
            return str_val == str_val[::-1]

        ans = 0

        # Option 1: Palindromes contained entirely within s
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if is_palindrome(sub):
                    ans = max(ans, len(sub))

        # Option 2: Palindromes contained entirely within t
        for i in range(len(t)):
            for j in range(i, len(t)):
                sub = t[i : j + 1]
                if is_palindrome(sub):
                    ans = max(ans, len(sub))

        # Option 3: Substring from s + Substring from t
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_s = s[i : j + 1]
                for k in range(len(t)):
                    for l in range(k, len(t)):
                        sub_t = t[k : l + 1]
                        combined = sub_s + sub_t
                        if is_palindrome(combined):
                            ans = max(ans, len(combined))

        return ans