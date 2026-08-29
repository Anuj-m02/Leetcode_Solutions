import bisect
from collections import Counter
# import cache

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # nums.sort()
        count = Counter(nums)
        # n = len(nums)

        unique_nums = sorted(count.keys())
        # print(unique_nums)
        n = len(unique_nums)

        @cache
        def dp(indx) :

            if indx >= n :
                return 0
            
            chose = unique_nums[indx]
            points = chose*count[chose]

            skip = dp(indx+1)

            if indx+1 < n and unique_nums[indx+1] == chose+1 :
                take = points + dp(indx+2)
            
            else :
                take = points + dp(indx+1)
            
            return max(skip , take)
        
        return dp(0)

        # @cache
        # def dp(left , right) :

        #     if left > right :
        #         return 0
            
        #     ans = 0
        #     indx = left
        #     while indx <= right :

        #     # for indx in range(left , right+1) :
        #         # we can delete any number

        #         chose = nums[indx]
        #         chose_left , chose_right = chose-1 , chose+1
        #         indx_left , indx_right = bisect.bisect_left(nums , chose-1) - 1 , bisect.bisect_right(nums , chose+1)

        #         op1 = chose*count[chose] + dp(left , indx_left) + dp(indx_right , right)
        #         ans = max(ans , op1)

        #         indx = bisect.bisect_right(nums , chose)
            
        #     return ans

        
        # return dp(0,n-1)




