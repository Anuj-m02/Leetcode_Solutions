class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        
        @cache
        def dp(indx , prev_c1 , prev_c2) :

            if indx == n//2 :
                return 0

            # if indx >= n :
            #     return float("inf")
            
            
            left_house , right_house = indx , n-indx-1

            ans = float("inf")
            for c1 in range(3) :
                if c1 == prev_c1 :
                    continue
                for c2 in range(3) :
                    if c2 == prev_c2 :
                        continue
                    
                    if c1 == c2 :
                        continue
                    
                    curr_cost = cost[left_house][c1] + cost[right_house][c2]
                    ans = min(ans , curr_cost + dp(indx+1 , c1 , c2))
            
            return ans
        
        return dp(0 , -1 , -1)


            # for colour_indx , colour_cost in enumerate(cost[indx]) : 

            #     colour_indx += 1
            #     if colour_indx == prev_colour :
            #         continue
                
            #     else :
            #         ans = max(ans, )