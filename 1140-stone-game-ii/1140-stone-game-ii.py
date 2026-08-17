from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        a , b = 0 , 0

        @lru_cache(maxsize=None)
        def dp(indx , m , turn) :


            if indx >= n :
                return 0
            
            if turn == 0 :
                max_alice = 0
                curr_take = 0

                for x in range(1 , 2*m + 1) :
                    if indx+x > n :
                        break
                    
                    curr_take += piles[indx+x-1]

                    score = curr_take + dp(indx+x , max(m , x) , 1 - turn)
                    max_alice = max(max_alice , score)
                
                return max_alice
            
            else :
                min_alice = float("inf")

                for x in range(1 , 2*m + 1) :
                    if indx + x > n :
                        break
                    
                    score = dp(indx+x ,  max(m , x) , 1-turn)
                    min_alice = min(min_alice , score)
                
                return min_alice



        
        return dp(0 , 1 , 0)
