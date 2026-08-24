class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        n = len(coins)

        @cache
        def dp(indx , target) :
            if indx == n :
                if target == 0 :
                    return 0
                else :
                    return float("inf")
            
            if target == 0 :
                return 0
            
            not_take = dp(indx+1 , target)
            take = float("inf")
            if coins[indx] <= target :
                take = 1 + dp(indx , target-coins[indx])
            
            return min(take ,not_take)
        
        ans = dp(0 , amount)
        if ans == float("inf") :
            return -1
        else :
            return ans

        # min_coins = [amount + 1] * (amount + 1)
        # min_coins[0] = 0

        # for i in range(1, amount + 1):
        #     for c in coins:
        #         if i - c >= 0:
        #             min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        # return min_coins[-1] if min_coins[-1] != amount + 1 else -1