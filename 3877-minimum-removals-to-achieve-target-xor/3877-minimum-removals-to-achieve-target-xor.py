# class Solution:
#     def minRemovals(self, nums: List[int], target: int) -> int:
        
#         n = len(nums)

#         def check(arr):
#             if not arr :
#                 return False
#             ans = 0
#             for i in range(len(arr)) :
#                 ans = ans ^ arr[i]
            
#             return ans == target


#         @lru_cache(maxsize=None)
#         def dp(indx , tup) :
#             if indx == n :
#                 if check(list(tup)) :
#                     return len(tup)
#                 else :
#                     return float("-inf")
            
#             # dont take this char
#             op1 = dp(indx+1 , tup)

#             # take this char
#             arr = list(tup)
#             arr.append(nums[indx])
#             op2 = dp(indx+1 , tuple(arr))

#             return max(op1 , op2)
        
#         max_kept = dp(0 , ())
#         if max_kept == float('-inf') and target == 0 :
#             return len(nums)

#         if max_kept == float("-inf") :
#             return -1
        

        
#         return n - max_kept

from functools import lru_cache
from typing import List

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(indx: int, curr_xor: int) -> int:
            if indx == n:
                if curr_xor == target:
                    return 0  # 0 additional removals needed
                return float("inf")  # Invalid subset

            # Option 1: Remove current element (1 removal cost)
            op1 = 1 + dp(indx + 1, curr_xor)

            # Option 2: Keep current element (0 removal cost)
            op2 = dp(indx + 1, curr_xor ^ nums[indx])

            return min(op1, op2)

        ans = dp(0, 0)
        return ans if ans != float("inf") else -1