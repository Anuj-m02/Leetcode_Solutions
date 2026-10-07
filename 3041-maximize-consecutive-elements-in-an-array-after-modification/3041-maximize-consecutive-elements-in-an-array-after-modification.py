class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        dp = defaultdict(int)

        for num in nums :

            dp[num+1] = dp[num] + 1

            dp[num] = dp[num-1] + 1
        
        return max(dp.values())
        
#         n = len(nums)
#         mini , maxi = min(nums) , max(nums)
#         nums.sort()

#         @lru_cache(maxsize=None)
#         def dp(indx , prev) :

#             if indx >= n :
#                 return 0
            
#             # ans = float("-inf")
            
#             # if not start :
#             #     ans = 1 + dp(indx+1 , True , nums[indx])
#             #     ans = max(ans , 1 + dp(indx+1 , True , nums[indx] + 1))

#             ans = dp(indx+1 , prev)

#             # Option 2: Pick current element (unmodified: nums[indx])
#             if prev == -1:
#                 ans = max(ans, 1 + dp(indx + 1, nums[indx]))
#             elif nums[indx] - prev == 1:
#                 ans = max(ans, 1 + dp(indx + 1, nums[indx]))

#             # Option 3: Pick current element (incremented: nums[indx] + 1)
#             if prev == -1:
#                 ans = max(ans, 1 + dp(indx + 1, nums[indx] + 1))
#             elif (nums[indx] + 1) - prev == 1:
#                 ans = max(ans, 1 + dp(indx + 1, nums[indx] + 1))

#             # # not_take this indx
#             # ans = max(ans , dp(indx+1 , False , prev))

#             # # take this indx
#             # if nums[indx] - prev == 1 :
#             #     ans = max(ans , 1 + dp(indx+1 , True , nums[indx]))
            
#             # elif nums[indx] + 1 - prev == 1 :
#             #     ans = max(ans , 1 + dp(indx+1 , True , nums[indx] + 1))
            
#             return ans
        
#         return dp(0 , -1)





