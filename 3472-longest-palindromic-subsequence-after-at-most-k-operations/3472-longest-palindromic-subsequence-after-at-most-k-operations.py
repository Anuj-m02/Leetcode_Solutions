# from functools import lru_cache
# import heapq
# from collections import defaultdict , deque , Counter


# class Solution:
#     def longestPalindromicSubsequence(self, s: str, k: int) -> int:

#         n = len(s)

#         def cost(char1 , char2) :
#             ord1 , ord2  = ord(char1) ,  ord(char2)
#             d = abs(ord1 - ord2)
#             w = 26-d
#             return min(d , w)

#         # @lru_cache(maxsize=None)
#         @cache
#         def dp(left , right , k) :

#             if left > right :
#                 return 0
            
#             if left == right :
#                 return 1
            
#             if k == 0 :
#                 res = float("-inf")
#                 if s[left] == s[right] :
#                     res = max(res , 2 + dp(left+1 , right-1 , 0))
                
#                 res = max(res , dp(left+1 , right , 0))
#                 res = max(res , dp(left , right-1 , 0))
#                 res = max(res , dp(left+1 , right-1 , 0))
            
#             else :

#                 res = float("-inf")
#                 if s[left] == s[right] :
#                     res = max(res , 2 + dp(left+1 , right-1 ,k))
                
#                 c = cost(s[left] , s[right])
#                 if c <= k :
#                     res = max(res , 2 + dp(left+1 , right-1 , k-c))
                
#                 res = max(res , dp(left+1 , right , k))
#                 res = max(res , dp(left , right-1 , k))
#                 res = max(res , dp(left+1 , right-1 , k))
            
#             return res
        
#         return dp(0 , len(s) - 1 , k )

from functools import lru_cache

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        def cost(char1: str, char2: str) -> int:
            d = abs(ord(char1) - ord(char2))
            return min(d, 26 - d)

        @lru_cache(maxsize=None)
        def dp(left: int, right: int, rem_k: int) -> int:
            if left > right:
                return 0
            if left == right:
                return 1

            # Option 1: Match s[left] and s[right] if cost fits budget
            c = cost(s[left], s[right])
            res = 0
            if c <= rem_k:
                res = max(res, 2 + dp(left + 1, right - 1, rem_k - c))

            # Option 2: Skip s[left] or s[right]
            res = max(res, dp(left + 1, right, rem_k))
            res = max(res, dp(left, right - 1, rem_k))

            return res

        return dp(0, n - 1, k)