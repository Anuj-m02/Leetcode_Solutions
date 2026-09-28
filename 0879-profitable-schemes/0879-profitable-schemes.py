class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        

        m = len(profit)
        mod = int(1e9) + 7

        @lru_cache(maxsize=None)
        def dp(indx , money , people) :
            if indx >= m :
                if people <= n and money >= minProfit :
                    return 1
                else :
                    return 0


            # skip this crime
            ans = dp(indx+1 , money , people)%mod

            # pick this crime
            if people + group[indx] <= n :
                new_money = min(minProfit , money+profit[indx])
                ans += dp(indx+1 , new_money , people + group[indx])%mod

            return ans%mod
        
        return dp(0 , 0 , 0)%mod
