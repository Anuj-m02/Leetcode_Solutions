# from collections import defaultdict , deque , Counter
# import heapq

# from functools import lru_cache

# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:

#         n = len(nums)

#         @lru_cache(maxsize = None)
#         def dp(indx , rem):

#             if indx == n :
#                 if rem == 0 :
#                     return 0
#                 else :
#                     return float("-inf")

            
#             # option 1 skip
#             not_take = dp(indx+1 , rem)

#             new_rem = (rem + nums[indx])%3
#             take = nums[indx] + dp(indx+1 , new_rem)

#             return max(take , not_take)

        
#         return dp(0,0)


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[r] = max sum with remainder r
        # Initial state: 0 for remainder 0, -inf for remainders 1 & 2
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            # Copy current dp state to compute next state
            prev_dp = list(dp)
            for current_sum in prev_dp:
                if current_sum != float('-inf'):
                    new_sum = current_sum + num
                    rem = new_sum % 3
                    dp[rem] = max(dp[rem], new_sum)
                    
        return dp[0]