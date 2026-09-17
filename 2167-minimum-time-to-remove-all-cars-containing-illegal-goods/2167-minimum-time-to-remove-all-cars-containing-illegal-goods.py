class Solution:
    def minimumTime(self, s: str) -> int:
        
        n = len(s)
        
        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i < 0:
                return 0

            # If current car is '0', no cost added
            if s[i] == "0":
                return dp(i - 1)

            # If '1', min of removing middle (cost 2) vs removing entire left prefix (cost i+1)
            return min(dp(i - 1) + 2, i + 1)

        # Find min cost across all split points i (prefix cost + suffix clear cost)
        ans = n  # Max cost (removing all cars from right)

        for i in range(n):
            # dp(i) handles prefix s[0...i]
            # (n - 1 - i) removes suffix s[i+1...n-1] from the right
            ans = min(ans, dp(i) + (n - 1 - i))

        return min(ans, dp(n - 1))

        # ans = n
        # left_dp = 0

        # for indx , char in enumerate(s) :
        #     if char == "1" :
        #         left_dp = min(left_dp + 2 , indx+1)
            
        #     ans = min(ans, left_dp + (n-1-indx))
        
        # return min(ans , left_dp)

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