# class Solution:
#     def numberOfSets(self, n: int, k: int) -> int:
        
#         mod = int(1e9)+7

#         @lru_cache(maxsize=None)
#         def dp(indx , k) :

#             if indx >= n :
#                 if k  == 0 :
#                     return 1
#                 return 0

#             if k == 0 :
#                 return 1

#             ans = dp(indx+1 , k)

#             for j in range(indx+1 , n) :
#                 ans += dp(j , k-1)%mod
            
#             return ans%mod
            
#             # print(indx , k)

#             # # break here 
#             # op1 = dp(indx+1 , k-1)%mod
#             # # continue here
#             # op2 = dp(indx+1 , k)%mod

#             # return (op1+op2)%mod
        
#         return dp(0 , k)%mod

from functools import lru_cache

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(i: int, k: int, drawing: int) -> int:
            if k == 0:
                return 1
            if i >= n:
                return 0

            if drawing:
                # Option 1: End the segment at point i (can immediately start another from i)
                # Option 2: Continue the segment past point i
                return (dp(i, k - 1, 0) + dp(i + 1, k, 1)) % MOD
            else:
                # Option 1: Skip point i
                # Option 2: Start a segment at point i
                return (dp(i + 1, k, 0) + dp(i + 1, k, 1)) % MOD

        return dp(0, k, 0)