class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mod = int(1e9) + 7

        @cache
        def dp(dice_left , total) :

            if total > target :
                return 0
            
            if dice_left == 0 :
                if total == target :
                    return 1
                else :
                    return 0
            
            ans = 0
            for face in range(1 , k+1) :

                ans += dp(dice_left-1 , total + face)%mod
            
            return ans % mod
        
        return dp(n , 0)
