# # from functools import lru_cache

# # class Solution:
# #     def stoneGameVIII(self, stones: List[int]) -> int:
        
# #         n = len(stones)

# #         prefix = [0]*(n+1)
# #         for i in range(n) :
# #             prefix[i+1] = prefix[i] + stones[i]

# #         @lru_cache(maxsize=None)
# #         def dp(left , right , turn):

# #             if left == right :
# #                 return 0
            
# #             if turn == 0 :
# #                 ans = float("inf")

# #                 for x in range(left , right+1) :

# #                     total = prefix[x]-prefix[left]
# #                     stones[x] = total 
# #                     ans = max(ans , total + dp(x , right , 1-turn))
            
# #             if turn == 1 :
# #                 ans = float('inf')

# #                 for x in range(left , right+1):
# #                     total = prefix[x]-prefix[left]
# #                     stones[x] = total 
# #                     ans = min(ans , -total + dp(x , right , 1-turn))
            
# #             return ans
        
# #         return dp(0,n-1,0)


# from functools import lru_cache
# from typing import List

# class Solution:
#     def stoneGameVIII(self, stones: List[int]) -> int:
#         n = len(stones)

#         # Build 1-indexed prefix sums of the ORIGINAL array
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i] + stones[i]

#         @lru_cache(maxsize=None)
#         def dp(i, turn):
#             # Base case: if no more valid moves (must pick x >= 2, i.e., index i >= 1)
#             if i >= n - 1:
#                 return 0
            
#             # Alice's turn (turn == 0): maximize difference
#             if turn == 0:
#                 ans = float("-inf")
#                 # Player can pick any index x from i + 1 to n - 1
#                 for x in range(i + 1, n):
#                     score = prefix[x + 1]
#                     ans = max(ans, score + dp(x, 1 - turn))
#                 return ans
            
#             # Bob's turn (turn == 1): minimize Alice's difference
#             else:
#                 ans = float("inf")
#                 for x in range(i + 1, n):
#                     score = prefix[x + 1]
#                     ans = min(ans, -score + dp(x, 1 - turn))
#                 return ans
        
#         # Start game: the first turn chooses x >= 2 (index >= 1)
#         return dp(0, 0)

class Solution:
    def stoneGameVIII(self, A: List[int]) -> int:
        n = len(A)
        s = list(accumulate(A))

        @cache
        def maxDiff(i):
            if i == n - 1: return s[n - 1]
            return max(maxDiff(i + 1), s[i] - maxDiff(i + 1))

        return maxDiff(1)