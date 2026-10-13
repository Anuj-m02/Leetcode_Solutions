# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
        
#         mod = int(1e9) + 7

#         @lru_cache(maxsize=None)
#         def dp(indx , count) :

#             if count < 0 :
#                 return 0
            
#             if indx >= n :
#                 return 1 if count == 0 else 0

#             # if indx >= n :
#             #     if count == k :
#             #         return 1
#             #     else :
#             #         return 0
            
#             # if count > k :
#             #     return 0

#             ans = dp(indx , count-1) + dp(indx+1 , count) - dp(indx+1 , count+indx+1)
#             return ans%mod
            
#             # total_ways = 0

#             # for pairs_added in range(min(indx+1 , k-count+1)) :
#             #     total_ways += dp(indx+1 , count + pairs_added)%mod
            
#             # return total_ways%mod
        
#         return dp(0,k)
            

from functools import cache

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(n: int, k: int) -> int:
            if k == 0:
                return 1
            if k < 0 or n == 0:
                return 0
            
            # dp(n, k) = dp(n, k - 1) + dp(n - 1, k) - dp(n - 1, k - n)
            ans = dp(n, k - 1) + dp(n - 1, k) - dp(n - 1, k - n)
            return ans % MOD

        return dp(n, k)