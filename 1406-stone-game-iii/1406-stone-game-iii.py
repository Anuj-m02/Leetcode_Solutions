from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        

        n = len(stoneValue)

        @lru_cache(maxsize=None)
        def dp(indx , turn ) :

            if indx >= n :
                return 0
            
            if turn == 1 :
                # alice turn score will be added
                op1 , op2 , op3 = float("-inf") , float("-inf") , float("-inf")
                op1 = stoneValue[indx] + dp(indx+1 , 0)
                if indx+1 < n :
                    op2 = stoneValue[indx] + stoneValue[indx+1] + dp(indx+2 , 0)
                if indx+2 < n :
                    op3 = stoneValue[indx] + stoneValue[indx+1] + stoneValue[indx+2] + dp(indx+3 , 0)

                return max(op1 , op2 , op3)
            
            else :
                # bob turn alice score wont be added
                op1 , op2 , op3 = float("inf") ,  float('-inf') , float("-inf") 
                op1 = dp(indx+1 , 1)
                op2 = dp(indx+2 , 1)
                op3 = dp(indx+3 , 1)

                return min(op1 , op2 , op3)
        
        alice = dp(0 , 1)
        bob = sum(stoneValue) - alice
        if alice == bob :
            return "Tie"
        if alice > bob :
            return "Alice"
        else :
            return "Bob"