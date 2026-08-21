class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        
        n = len(hamsters)


        @lru_cache(maxsize=None)
        def dp(indx , covered) :

            if indx == n :
                return 0
            
            if hamsters[indx] == "." :
                # we can either place here or not
                op1 = dp(indx+1 , 0)
                op2 = 1 + dp(indx+1 , 1)

                return min(op1 , op2)

            else :
                if covered :
                    return dp(indx+1 , 0)
                
                if indx + 1 < n and hamsters[indx+1] == "." :
                    return 1 + dp(indx+2 , 1)
                
                return float("inf")
        
        ans = dp(0 , 0)
        return ans if ans != float("inf") else -1

            