class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0 or n < 4 :
            return False
        
        target = total // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target :
            return False
        
        @lru_cache(maxsize=None)
        def dp(used_indices , curr_sum) :

            if len(used_indices) == n :
                return True
            
            for indx , length in enumerate(matchsticks) :
                if indx in used_indices :
                    continue
                
                if curr_sum + length > target :
                    continue
                
                nxt_sum = (curr_sum + length) % target

                if dp(used_indices | frozenset([indx]) , nxt_sum) :
                    return True
            
            return False
        
        return dp(frozenset(), 0)
        
        # @lru_cache(maxsize=None)
        # def dp(indx , up , down , left , right) :

        #     if indx >= n :
        #         if up == down and left == right and up == left :
        #             return True
        #         else :
        #             return False
            
        #     curr = matchsticks[indx]
        #     return dp(indx+1 , up + curr , down , left , right) or dp(indx+1 , up , down + curr , left , right) or dp(indx+1 , up , down , left + curr , right) or dp(indx+1 , up , down , left , right+curr)

        # return dp(0 , 0 ,0 , 0 , 0) 