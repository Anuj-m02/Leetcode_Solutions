class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        
        n = len(stones)



        for indx , num in enumerate(stones) :
            stones[indx] = num%3
        
        
        # # now elts say started with rem 1 , and we know the remaining stones

        cnt_rem_one , cnt_rem_two , cnt_rem_zero = stones.count(1)  , stones.count(2) , stones.count(0)

        # alice wins if even zero rem and rem one and rem 2 both exist
        if cnt_rem_zero % 2 == 0 :
            return cnt_rem_one >= 1 and cnt_rem_two >= 1 
        
        else :
            return abs(cnt_rem_one - cnt_rem_two) > 2

        # def dp(indx , turn , curr_sum) :

        #     if indx == n :
        #         return False
            
        #     if curr_sum%3 == 1 :
        #         # options to pick either zero rem or 1 rem
        #         if cnt_rem_one > 0 :
        #             dp(indx+1 , 1-turn , 2 )
                
        #         if cnt_rem_zero > 0 :
        #             dp(indx+1 , 1-turn  , 1)
            
        #     if curr_sum%3 == 2 :
        #         # now can pick 0 or 2
        #         if cnt_rem_zero > 0 :
        #             dp(indx+1 , 1-turn , 2)
        #         if cnt_rem_two > 0 :
        #             dp(indx+1 , 1-turn , 1)
            
        #     if curr_sum%3 == 0 :
        #         # now can pick 1 or 2
        #         if cnt_rem_one > 0 :
        #             dp(indx+1 , 1-turn , 1)
        #         if cnt_rem_two > 0 :
        #             dp(indx+1 , 1-turn , 2)
            
        #     return op1 or op2
        
        # return dp(0 , 0 , 0)


