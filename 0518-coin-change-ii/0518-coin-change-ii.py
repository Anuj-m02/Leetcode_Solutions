from collections import defaultdict , deque
import heapq
from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)


        @cache
        def dp(indx , target) :

            if target == 0 :
                return 1
            if indx == n :
                return 0
            
            
            not_take = dp(indx+1 , target)
            take = 0
            if coins[indx] <= target :
                take = dp(indx , target-coins[indx])
            
            return take + not_take

        # @lru_cache(None)
        # def f(indx , target):
        #     if indx == 0 :
        #         if target % coins[0] == 0:
        #             return 1
        #         return 0
            
        #     not_take = f(indx-1 , target)


        #     first = 0
        #     if coins[indx] <= target :
        #         first = f(indx , target - coins[indx])

        #     return not_take + first
        
        return dp(0, amount)

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount + 1)
#         dp[0] = 1
#         for x in coins:
#             for j in range(x, amount + 1):
#                 dp[j] += dp[j - x]
#         return dp[amount]
        
# # __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))