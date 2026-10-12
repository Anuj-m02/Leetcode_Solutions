class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        n = len(prices)

        @lru_cache(maxsize=None)
        def dp(indx) :

            if 2*indx >= n :
                return prices[indx-1]
            
            min_nxt = float('inf')
            #[i+1 , 2i+1]
            for j in range(indx+1 , 2*indx + 2) :
                min_nxt = min(min_nxt , dp(j))
            
            return prices[indx-1] + min_nxt
        
        return dp(1)

