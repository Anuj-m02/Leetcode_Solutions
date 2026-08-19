# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache

# # class Solution:
# #     def specialPerm(self, nums: List[int]) -> int:
        
# #         n = len(nums)
# #         mod = 10**9 + 7
# #         s = set()
# #         for i in range(n) :
# #             s.add(nums[i])
        
# #         def check(start_indx) :

# #             @lru_cache(maxsize=None)
# #             def dp(indx , prev_indx , visited) :
# #                 if indx == n :
# #                     return 1
                
# #                 ans = 0 
# #                 visited_list = list(visited)
# #                 for i in range(n) :
# #                     num = nums[i]
# #                     if not visited_list[i] :
# #                         if nums[prev_indx]%num == 0 or num % nums[prev_indx] == 0 :
# #                             visited_list[i] = True
# #                             ans += dp(indx+1 , i , tuple(visited_list))%mod
# #                             visited_list[i] = False
                
# #                 return ans
            
# #             initial_visited = [False]*(n)
# #             initial_visited[start_indx] = True
# #             return dp(1 , start_indx ,tuple(initial_visited))


                


# #         ans = 0
# #         for i in range(n) :
# #             temp = check(i)
# #             ans += temp%mod
        
# #         return ans%mod


# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache
# from typing import List

# class Solution:
#     def specialPerm(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         mod = 10**9 + 7
        
#         def check(start_indx) :

#             @lru_cache(maxsize=None)
#             def dp(indx , prev_indx , visited) :
#                 if indx == n :
#                     return 1
                
#                 ans = 0 
#                 for i in range(n) :
#                     if i not in visited :
#                         num = nums[i]
#                         if nums[prev_indx] % num == 0 or num % nums[prev_indx] == 0 :
#                             ans = (ans + dp(indx+1 , i , visited | frozenset([i]))) % mod
                
#                 return ans
            
#             return dp(1 , start_indx , frozenset([start_indx]))

#         ans = 0
#         for i in range(n) :
#             temp = check(i)
#             ans = (ans + temp) % mod
        
#         return ans % mod

from functools import lru_cache
from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(prev_idx: int, visited: frozenset) -> int:
            if len(visited) == n:
                return 1

            ans = 0
            for i in range(n):
                if i not in visited:
                    if nums[prev_idx] % nums[i] == 0 or nums[i] % nums[prev_idx] == 0:
                        ans = (ans + dp(i, visited | frozenset([i]))) % mod

            return ans

        ans = 0
        for i in range(n):
            ans = (ans + dp(i, frozenset([i]))) % mod

        return ans