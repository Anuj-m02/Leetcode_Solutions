class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        n , m = len(baseCosts) , len(toppingCosts)
        mini = float("inf")

        def dp(indx , curr_cost) :
            nonlocal mini

            if abs(curr_cost-target) < abs(mini-target) :
                mini = curr_cost
            
            elif abs(curr_cost-target) == abs(mini-target) :
                mini = min(mini , curr_cost)
            
            if indx == m or curr_cost >= target :
                return 0
            
            # take0
            dp(indx+1 , curr_cost)
            dp(indx+1 , curr_cost + toppingCosts[indx])
            dp(indx+1 , curr_cost + 2*toppingCosts[indx])
        

        for base in baseCosts :
            dp(0 ,base)
        
        return mini