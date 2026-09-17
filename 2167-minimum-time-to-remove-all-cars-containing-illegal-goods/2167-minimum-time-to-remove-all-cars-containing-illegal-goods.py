class Solution:
    def minimumTime(self, s: str) -> int:
        
        n = len(s)


        ans = n
        left_dp = 0

        for indx , char in enumerate(s) :
            if char == "1" :
                left_dp = min(left_dp + 2 , indx+1)
            
            ans = min(ans, left_dp + (n-1-indx))
        
        return min(ans , left_dp)

        # @lru_cache(maxsize=None)
        # def dp(left , right) :

        #     if left > right :
        #         return 0

        #     if s[left:right+1].count("1") == 0 :
        #         return 0
            
        #     # op1 remove from left
        #     op1 = 1 + dp(left+1 , right)
        #     #op2  remove form rihgt
        #     op2 = 1 + dp(left , right-1)

        #     op3 = float("inf")
        #     # op3 remove from in between of them
        #     for indx in range(left+1 , right) :
        #         if s[indx] == "1" :
        #             op3 = min(op3 , 2 + dp(left , indx-1) + dp(indx+1 , right))
            
        #     return min(op1 , op2 , op3)
        
        # return dp(0 , n-1)