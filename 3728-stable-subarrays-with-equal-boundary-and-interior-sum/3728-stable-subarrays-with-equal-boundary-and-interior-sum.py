# # class Solution:
# #     def countStableSubarrays(self, capacity: List[int]) -> int:
        
# #         n = len(capacity)

# #         prefix = [0]*(n)
# #         for i in range(n) :
# #             prefix[i] = prefix[i-1] + capacity[i]
        
# #         d = defaultdict(list)
        
# #         for indx in range(n) :
# #             d[capacity[indx]].append(indx)
        

# #         candid = d.keys()
# #         cnt = 0
# #         for num , pos in d.items() :
# #             m = len(pos)
# #             for i in range(m) :
# #                 for j in range(i+1 , m) :
# #                     left , right = pos[i]
        
# #         return cnt
# from collections import defaultdict
# from typing import List

# class Solution:
#     def countStableSubarrays(self, capacity: List[int]) -> int:
#         n = len(capacity)

#         # 1. Build prefix sum array
#         prefix = [0] * n
#         prefix[0] = capacity[0]
#         for i in range(1, n):
#             prefix[i] = prefix[i-1] + capacity[i]
        
#         # 2. Store positions for each capacity value
#         d = defaultdict(list)
#         for indx in range(n):
#             d[capacity[indx]].append(indx)
        
#         cnt = 0
        
#         # 3. Check every pair of matching elements
#         for num, pos in d.items():
#             m = len(pos)
#             for i in range(m):
#                 for j in range(i + 1, m):
#                     l, r = pos[i], pos[j]
                    
#                     # Length at least 3 means r - l >= 2
#                     if r - l >= 2:
#                         # Sum strictly between l and r is prefix[r-1] - prefix[l]
#                         interior_sum = prefix[r - 1] - prefix[l]
#                         if interior_sum == num:
#                             cnt += 1
        
#         return cnt

from collections import defaultdict
from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        if n < 3:
            return 0
        
        # Calculate prefix sums
        prefix = [0] * n
        prefix[0] = capacity[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + capacity[i]
        
        # Frequency map for valid starting indices l
        # Key: (capacity[l], prefix[l] + capacity[l])
        seen = defaultdict(int)
        cnt = 0
        
        # For each possible right end r (r >= 2 to allow subarray length >= 3)
        for r in range(2, n):
            # The valid left index that enters the window is l = r - 2
            l = r - 2
            key_l = (capacity[l], prefix[l] + capacity[l])
            seen[key_l] += 1
            
            # Check how many valid l's match the current right boundary
            target_key = (capacity[r], prefix[r - 1])
            cnt += seen[target_key]
            
        return cnt