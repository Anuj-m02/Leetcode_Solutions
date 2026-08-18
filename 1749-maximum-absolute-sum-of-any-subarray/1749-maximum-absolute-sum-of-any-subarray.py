# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache


# # class Solution:
# #     def maxAbsoluteSum(self, nums: List[int]) -> int:
        

# #         n = len(nums)

# #         @lru_cache(maxsize=None)
# #         def dp(indx , total) :
# #             if indx == n :
# #                 return abs(total)
            

# #             # dont pick this means starting new subarr
# #             op1 = dp(indx+1 , 0)
# #             op2 = float("-inf")
# #             # pick this indx
# #             op2 = dp(indx+1 , total + nums[indx])

# #             return max(op1 , op2)
        
# #         return dp(0,0)
# from typing import List
# from functools import lru_cache

# class Solution:
#     def maxAbsoluteSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = 0

#         # state: indx -> current array index
#         #        started -> True if a contiguous subarray is currently active
#         #        total -> running sum of current contiguous subarray
#         @lru_cache(maxsize=None)
#         def dp(indx, started, total):
#             nonlocal ans
            
#             # Record the absolute sum of the current contiguous subarray
#             if started:
#                 ans = max(ans, abs(total))

#             if indx == n:
#                 return

#             if not started:
#                 # Option 1: Don't start a subarray at indx
#                 dp(indx + 1, False, 0)
                
#                 # Option 2: Start a new contiguous subarray at indx
#                 dp(indx + 1, True, nums[indx])
#             else:
#                 # If started, we can either extend the contiguous subarray
#                 dp(indx + 1, True, total + nums[indx])
#                 # Or stop the contiguous subarray here (no choice needed, handled by returning)

#         dp(0, False, 0)
#         return ans

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        current_max = 0
        current_min = 0
        
        for num in nums:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
            
        return max(abs(max_sum), abs(min_sum))