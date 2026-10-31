class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        total_zeros = 0 # number of subsequences of 0s so far
        total_ones = 0 # the number of subsequences of 0s followed by 1s so far
        total_twos = 0 # the number of special subsequences so far
        
        M = 1000000007
        
        for n in nums:
            if n == 0:
                # if we have found new 0 we can add it to any existing subsequence of 0s
                # or use only this 0
                total_zeros += (total_zeros + 1) % M
            elif n == 1:
                # if we have found new 1 we can add it to any existing subsequence of 0s or 0s and 1s
                # to get a valid subsequence of 0s and 1s
                total_ones += (total_zeros + total_ones) % M
            else:
                # if we have found new 2 we can add it to any existing subsequence of 0s and 1s 0r 0s,1s and 2s
                # to get a valid subsequence of 0s,1s and 2s
                total_twos += (total_ones + total_twos) % M
        
        return total_twos % M

# class Solution:
#     def countSpecialSubsequences(self, nums: list[int]) -> int:
#         MOD = 10**9 + 7
#         dp0 = dp1 = dp2 = 0
        
#         for num in nums:
#             if num == 0:
#                 dp0 = (2 * dp0 + 1) % MOD
#             elif num == 1:
#                 dp1 = (2 * dp1 + dp0) % MOD
#             elif num == 2:
#                 dp2 = (2 * dp2 + dp1) % MOD
                
#         return dp2


# # # class Solution:
# # #     def countSpecialSubsequences(self, nums: list[int]) -> int:
        
# # #         n = len(nums)
# # #         mod = int(1e9) + 7


# # #         @lru_cache(maxsize=None)
# # #         def dp(indx , state) :

            
# # #             if indx == n :
# # #                 return 1 if state == 3 else 0
            
# # #             # skip
# # #             ans = dp(indx+1 , state)%mod

# # #             # if curr_num == state 
# # #             if nums[indx] == state:
# # #                 ans += dp(indx+1 , state)%mod
            
# # #             elif state < 3 and nums[indx] == state :
# # #                 ans += dp(indx+1 , state+1)%mod

            
# # #             # elif nums[indx] == state+1 :
# # #             #     ans += dp(indx+1 , state+1)%mod

# # #             return ans
        
# # #         return dp(0 , 0)

# # import sys
# # # Increase recursion depth limit for arrays up to 10^5
# # sys.setrecursionlimit(200000)

# # class Solution:
# #     def countSpecialSubsequences(self, nums: list[int]) -> int:
# #         MOD = 10**9 + 7
# #         n = len(nums)
# #         memo = {}

# #         def dp(i: int, state: int) -> int:
# #             # Base Case: Reached the end of array
# #             # state == 3 means we have successfully completed a 0-1-2 sequence
# #             if i == n:
# #                 return 1 if state == 3 else 0
            
# #             if (i, state) in memo:
# #                 return memo[(i, state)]
            
# #             # 1. Option: Skip the current element nums[i]
# #             ans = dp(i + 1, state)
            
# #             # 2. Option: Take nums[i] if it matches our current target state
# #             # (Allows repeating the same number, e.g., multiple 0s, 1s, or 2s)
# #             if nums[i] == state:
# #                 ans += dp(i + 1, state)
            
# #             # 3. Option: Take nums[i] to transition to the next state
# #             # (0 -> 1, 1 -> 2, or 2 -> completed state 3)
# #             elif state < 3 and nums[i] == state:
# #                 ans += dp(i + 1, state + 1)
# #             elif state == 0 and nums[i] == 0:
# #                 ans += dp(i + 1, 1)
# #             elif state == 1 and nums[i] == 1:
# #                 ans += dp(i + 1, 2)
# #             elif state == 2 and nums[i] == 2:
# #                 ans += dp(i + 1, 3)
                
# #             ans %= MOD
# #             memo[(i, state)] = ans
# #             return ans

# #         # Start from index 0 expecting the first '0' (state 0)
# #         return dp(0, 0)