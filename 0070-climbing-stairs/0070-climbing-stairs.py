# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0]*(n+1)
#         if n == 0 or n == 1 :
#             return 1
#         prev = 1
#         curr = 1
#         for i in range(2,n+1):
#             temp = curr
#             curr = prev+curr
#             prev = temp
#         return curr

class Solution:
    def climbStairs(self, n: int) -> int:

        
        @cache
        def dp(indx) :
            if indx == 1 or indx == 0 :
                return 1
            
            return dp(indx-1) + dp(indx-2)

        return dp(n)
    #     memo = {}
    #     return self.helper(n, memo)
    
    # def helper(self, n: int, memo: dict[int, int]) -> int:
    #     if n == 0 or n == 1:
    #         return 1
    #     if n not in memo:
    #         memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
    #     return memo[n]