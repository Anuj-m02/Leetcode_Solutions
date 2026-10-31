import heapq
from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Heap stores tuples: (-dp[j], j)
        # Initialize with the starting index 0
        max_heap = [(-nums[0], 0)]
        
        curr_max = nums[0]
        
        for i in range(1, n):
            # Remove indices that are outside the current window [i - k, i - 1]
            while max_heap[0][1] < i - k:
                heapq.heappop(max_heap)
            
            # The top of the heap is the maximum dp score within the valid range
            curr_max = -max_heap[0][0] + nums[i]
            
            # Push current index's score and index onto the heap
            heapq.heappush(max_heap, (-curr_max, i))
            
        return curr_max
        
# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
        
#         n = len(nums)

#         queue = deque([])
#         queue.append((0 , 0))
#         # curr_indx , curr_total

#         vis = set()
#         vis.add(0)
#         ans = 0
#         while queue :
#             curr_node , curr_total = queue.popleft()

#             if curr_node == n-1 :
#                 ans = max(ans , curr_total)
            
#             start = curr_node + 1
#             end = min(n-1 , curr_node+k)
#             for j in range (start , end+1) :
#                 if j not in vis :
#                     queue.append((j , curr_total + nums[j]))
#                     vis.add(j)
        
#         return ans