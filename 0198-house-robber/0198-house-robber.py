
class Solution:
    def rob(self, nums: List[int]) -> int:



        n = len(nums)

        @cache
        def dp(indx) :
            if indx >= n :
                return 0
            
            not_take = 0 + dp(indx+1)
            take = nums[indx] + dp(indx+2)

            return max(not_take , take)
        
        return dp(0)

        # if n == 1 :
        #     return nums[0]
        # if n == 0 :
        #     return 0
        # dp = [0]*n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,n):
        #     take = nums[i] + dp[i-2]
        #     nottake = 0 + dp[i-1]
        #     dp[i] = max(take,nottake)
        # return dp[n-1]