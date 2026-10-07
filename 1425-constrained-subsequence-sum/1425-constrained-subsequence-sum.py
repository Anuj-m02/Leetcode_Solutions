# # class Solution:
# #     def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        
# #         n = len(nums)

# #         @lru_cache(maxsize=None)
# #         def dp(indx , start) :

# #             if indx >= n :
# #                 if start :
# #                     return 0
# #                 else :
# #                     return float("-inf)
                
# #             if not start :
# #                 # dont_start here

# #                 ans = dp(indx+1 , start)

# #                 # start here
# #                 ans = max(ans , nums[indx] + dp(indx+1 , True))

            
# #             # dont take
# #             ans = dp(indx+1)

# #             # take
# #             for j in range(indx+1 , min(n , indx+k+1)) :
# #                 ans = max(ans , nums[indx] + dp(j) )

# #             return ans
        
# #         return dp(0)
            

# from functools import lru_cache

# class Solution:
#     def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
#         n = len(nums)

#         @lru_cache(maxsize=None)
#         def dp(indx: int) -> int:
#             # max_next = 0 allows us to STOP at nums[indx] if future elements are negative
#             max_next = 0 
            
#             # Pick the next element j within distance k
#             for j in range(indx + 1, min(n, indx + k + 1)):
#                 max_next = max(max_next, dp(j))

#             return nums[indx] + max_next

#         # Try starting the subsequence at EVERY possible index
#         return max(dp(i) for i in range(n))

import heapq

class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        # Max-heap storing (-dp[j], j)
        max_heap = []
        
        for i in range(n):
            # Remove top element if it is out of the window [i-k, i-1]
            while max_heap and max_heap[0][1] < i - k:
                heapq.heappop(max_heap)
            
            # Get max DP in range k
            max_prev = -max_heap[0][0] if max_heap else 0
            dp[i] = nums[i] + max(0, max_prev)
            
            heapq.heappush(max_heap, (-dp[i], i))
            
        return max(dp)