class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)


        # non wrapping subrray
        # direct kadane algo return max_sum

        # # wraPPING SUBARRY
        # LEFT , MID , RIGHT
        # TOTAL_SUM = SUM(LEFT) + SUM(MID) + SUM(RIGHT)
        # SUBRRY SUM = SUM(LEFT) + SUM(RIGHT)
        # SUBRRY SUM = TOTAL_SUM - SUM(MID)


        # MAXIMIZE SUBRRY SUM SO MINIMIZE MID SUM

        
        @cache
        def dp_max(indx) :

            if indx == 0 :
                return nums[indx]
            
            return max(nums[indx] , nums[indx] + dp_max(indx-1))
        

        @cache
        def dp_min(indx) :

            if indx == 0 :
                return nums[indx]
            
            return min(nums[indx] , nums[indx] + dp_min(indx-1))
        

        max_sum = max(dp_max(i) for i in range(n))
        min_sum = min(dp_min(i) for i in range(n))

        total_sum = sum(nums)

        if max_sum < 0 :
            return max_sum
        
        return max(max_sum , total_sum - min_sum)