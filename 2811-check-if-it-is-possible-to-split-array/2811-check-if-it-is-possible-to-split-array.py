# from collections import defaultdict , deque ,Counter
# import heapq
# from functools import lru_cache

# class Solution:
#     def canSplitArray(self, nums: List[int], m: int) -> bool:

#         n = len(nums)

#         @lru_cache(maxsize=None)
#         def dp(left , right) :
            
#             # single element
#             if left == right :
#                 return True
            
#             ans = False

#             for k in range(left , right):
#                 left_valid = False
#                 if (k == left) or (sum(nums[left:k+1]) >= m) :
#                     left_valid = True
#                 right_valid = False
#                 if (k+1 == right) or (sum(nums[k+1:right+1]) >= m) :
#                     right_valid = True
                
#                 if left_valid and right_valid :
#                     if dp(left , k) and dp(k+1 , right) :
#                         ans = True
            
#             return ans
        
#         return dp(0,n-1)


class Solution:

    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # Base case for small arrays
        if len(nums) <= 2:
            return True

        # Check if there exists any adjacent pair with sum >= m
        return any(nums[i] + nums[i + 1] >= m for i in range(len(nums) - 1))