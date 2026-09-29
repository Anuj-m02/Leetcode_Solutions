class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        mod = int(1e9) + 7

        @lru_cache(maxsize=None)
        def dp(indx , total , cnt) :
            if indx >= n :
                if total == k :
                    # no of subsequemce
                    return pow(2 , n-cnt)%mod

                return 0
            
            # skip this ele
            ans = dp(indx+1 , total , cnt)%mod

            #take this ele
            if total + nums[indx] <= k :
                ans += dp(indx + 1 , total+nums[indx] , cnt + 1)%mod
            
            return ans%mod
        
        return dp(0 , 0 , 0)%mod