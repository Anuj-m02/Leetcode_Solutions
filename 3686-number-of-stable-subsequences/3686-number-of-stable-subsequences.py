# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def countStableSubsequences(self, nums: List[int]) -> int:

#         n = len(nums)
#         mod = 10**9 + 7

#         @lru_cache(None)
#         def dp(indx , prev_par , consec) :

#             if indx == n :
#                 if prev_par != -1 :
#                     return 1
#                 else :
#                     return 0
            
#             # dont pick
#             ans = dp(indx+1 , prev_par , consec)

#             curr_par = nums[indx] % 2

#             if prev_par == -1 :
#                 # first elemnt in subsequne
#                 ans += dp(indx+1 , curr_par , 1)%mod
#             elif curr_par != prev_par :
#                 ans += dp(indx+1 , curr_par , 1)%mod
#             elif consec < 2 :
#                 ans += dp(indx+1 , curr_par , consec+1)%mod

#             return ans%mod 
        
#         return dp(0,-1,0)

            

#             # at each indx option can we pick in subsequence or not
#             # we can pick only if par diffres
#             # if last three same par then not pick
from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # Represent prev_par as:
        # 0: None (empty subsequence)
        # 1: Even
        # 2: Odd
        # consec can be 0, 1, 2
        
        # memo[indx][prev_par][consec]
        memo = [[[-1] * 3 for _ in range(3)] for _ in range(n)]

        def dp(indx: int, prev_par: int, consec: int) -> int:
            if indx == n:
                return 1 if prev_par != 0 else 0

            if memo[indx][prev_par][consec] != -1:
                return memo[indx][prev_par][consec]

            # Option 1: Skip current element
            ans = dp(indx + 1, prev_par, consec)

            # Option 2: Pick current element
            curr_par = 1 if nums[indx] % 2 == 0 else 2  # 1 = even, 2 = odd

            if prev_par == 0:
                # First element in subsequence
                ans = (ans + dp(indx + 1, curr_par, 1)) % MOD
            elif curr_par != prev_par:
                # Parity flipped, reset consecutive count
                ans = (ans + dp(indx + 1, curr_par, 1)) % MOD
            elif consec < 2:
                # Same parity, increment consecutive count
                ans = (ans + dp(indx + 1, curr_par, consec + 1)) % MOD

            memo[indx][prev_par][consec] = ans % MOD
            return ans%MOD

        return dp(0, 0, 0)