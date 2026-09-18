class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(indx) :

            if indx == n-1 :
                return 0

            
            ans = float("-inf")

            for new_indx in range(indx+1 , n) :
                req = nums[new_indx] - nums[indx]
                if -target <= req <= target :
                    ans = max(ans , 1 + dp(new_indx))

            
            return ans
        
        ans = dp(0)
        if ans != float("-inf") :
            return ans
        else :
            return -1