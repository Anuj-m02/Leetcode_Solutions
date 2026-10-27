class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:

        n = len(nums)

        prefix = [0]*(n+1)
        for i in range(n) :
            prefix[i+1] = prefix[i] + nums[i]
        
        @lru_cache(maxsize=None)
        def dp(left , right , cnt) :

            if right == n-1 :
                if cnt <= k :
                    return (prefix[right+1]-prefix[left])/(right-left+1)

                else :
                    return float("-inf") 
            
            ans = float("-inf")

            # dont partition here
            ans = max(ans , dp(left , right+1 , cnt))

            # partition here
            if cnt < k :
                curr_avg = (prefix[right+1] - prefix[left])/(right-left+1)

                ans = max(ans , (curr_avg + dp(right+1 , right+1 , cnt+1)))

            return ans
        
        return dp(0 , 0 , 1)

            
