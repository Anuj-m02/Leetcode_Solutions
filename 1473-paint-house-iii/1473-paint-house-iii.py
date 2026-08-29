class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        # m , n = len(houses) , len(cost[0])

        @lru_cache(maxsize=None)
        def dp(indx , prev_colour , cnt) :

            if indx >= m :
                if cnt == target :
                    return 0
                else :
                    return float("inf")
            
            if houses[indx] != 0 :
                if prev_colour != houses[indx] :
                    return dp(indx+1 , houses[indx] , cnt+1)
                else :
                    return dp(indx+1 , houses[indx] , cnt)

            # choices
            ans = float("inf")
            colour_choice = cost[indx]
            for i in range(1 , len(colour_choice)+1) :
                curr_wt , curr_colour  = colour_choice[i-1] , i
                if curr_colour == prev_colour :
                    ans = min(ans , curr_wt + dp(indx+1 ,prev_colour , cnt))
                else :
                    ans = min(ans , curr_wt + dp(indx+1 , curr_colour , cnt+1))
            
            return ans

        res =  dp(0 , -1 , 0)
        if res == float("inf") :
            return -1

        return res   

