from collections import defaultdict , deque , Counter
from functools import lru_cache

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        n = len(rods)

        @lru_cache(maxsize=None)
        def dp( indx , diff) :

            if indx == n :
                if diff == 0 :
                    return 0
                else :
                    return float("-inf")
            
            # not pick indx
            ans = dp(indx+1 , diff)

            # pick indx but in any of the two set
            ans = max( ans , rods[indx] + dp(indx+1 , rods[indx]+diff))

            new_diff = abs(diff - rods[indx])
            height_gain = max( 0 , rods[indx] - diff)
            ans = max(ans , height_gain + dp(indx+1 , new_diff))

            return ans
        
        return dp(0,0)


        #     temp2 = dp(indx+1 , total1+rods[indx] , total2)
        #     temp3 = dp(indx+1 , total1 , total2+rods[indx])

        #     return max(temp1 , temp2 , temp3)
        
        # return dp(0,0,0)