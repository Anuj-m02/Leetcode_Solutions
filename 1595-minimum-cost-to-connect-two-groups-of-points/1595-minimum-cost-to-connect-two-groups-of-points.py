class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        
        n1 , n2 = len(cost) , len(cost[0])

        min_cost_right = [min(cost[i][j] for i in range(n1)) for j in range(n2)]

        @lru_cache(maxsize=None)
        def dp(indx , connected_grp2) :

            if indx == n1 :
                return sum(min_cost_right[j] for j in range(n2) if j not in connected_grp2)

            res = float("inf")
            # try connnceteing node i to every node j in grp 2
            for j in range(n2) :
                res = min(res , cost[indx][j] + dp(indx+1 , connected_grp2 | frozenset({j})))
            
            return res
        
        return dp(0 , frozenset())
        # size1 matrix from 1 to 12
        # size2 matrix from A to L
