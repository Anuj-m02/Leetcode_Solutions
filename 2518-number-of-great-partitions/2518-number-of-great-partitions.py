# class Solution:
#     def countPartitions(self, nums: list[int], k: int) -> int:
        
#         n = len(nums)
#         mod = int(1e9) + 7
#         total = sum(nums)

#         @lru_cache(maxsize=None)
#         def dp(indx , total1) :

#             if indx >= n :
#                 if total1 >= k and total-total1 >= k :
#                     return 1
#                 else :
#                     return 0
            
#             # skip this indx
#             ans = dp(indx+1 , total1)%mod

#             # take this indx
#             ans += dp(indx+1 , total1 + nums[indx])% mod

#             return ans%mod
        
#         return dp(0 , 0)

#         # n = len(nums)
#         # mod = int(1e9) + 7
#         # total = sum(nums)

#         # @lru_cache(maxsize=None)
#         # def dp(indx , round1 , remd1) :

#         #     if indx >= n :
#         #         total1 = round1*k + remd1
#         #         if total1 >= k and total-total1 >= k :
#         #             return 1
#         #         else :
#         #             return 0
            
#         #     # skip this indx
#         #     ans = dp(indx+1 , round1 , remd1)%mod

#         #     # take this indx
#         #     remd1 += nums[indx]
#         #     if remd1>= k :
#         #         round1 += remd1//k
#         #         remd1 = remd1%k

#         #         ans += dp(indx+1 , round1 , remd1)% mod
#         #     else :
#         #         ans += dp(indx+1 , round1 , remd1)%mod


#         #     return ans%mod
        
#         # return dp(0 , 0 , 0)

from functools import lru_cache

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        total_sum = sum(nums)
        
        # If total sum is less than 2*k, it's impossible for both groups to be >= k
        if total_sum < 2 * k:
            return 0
        
        n = len(nums)
        
        # Count number of subsets with sum < k
        @lru_cache(maxsize=None)
        def dp(idx, current_sum):
            if current_sum >= k:
                return 0
            if idx == n:
                return 1
            
            # Skip nums[idx]
            ways = dp(idx + 1, current_sum)
            # Take nums[idx]
            ways = (ways + dp(idx + 1, current_sum + nums[idx])) % mod
            
            return ways
        
        invalid_subsets = dp(0, 0)
        total_ways = pow(2, n, mod)
        
        # Subtract invalid choices for group 1 and group 2
        return (total_ways - 2 * invalid_subsets) % mod