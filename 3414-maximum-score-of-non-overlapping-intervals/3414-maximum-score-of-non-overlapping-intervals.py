# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache
# import bisect


# class Solution:
#     def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        
#         n = len(intervals)

#         # start , end , weight , indx
#         sorted_intervals = sorted([(intervals[i][0] , intervals[i][1] , intervals[i][2] , i) for i in range(n)])

#         start = [interval[0] for interval in sorted_intervals]

#         @lru_cache(maxsize=None)
#         def dp(indx , count) :

#             if indx >= n or count == 0 :
#                 return (0 , [])
            
#             # skip
#             skip_wt , skip_indx = dp(indx+1 , count)

#             # pick
#             left , right , weight , orig_indx = sorted_intervals[indx]

#             next_indx = bisect.bisect_left(start , right+1)

#             take_nxt_weight , take_nxt_indx = dp(next_indx , count-1)
#             take_weight = weight + take_nxt_weight

#             take_indices = sorted([orig_indx] + take_nxt_indx)

#             if take_weight > skip_weight :
#                 return (take_weight , take_indices)
            
#             elif take_weight < skip_weight :
#                 return (skip_weight , skip_indx)
            
#             else :
#                 if take_indices < skip_indx :
#                     return (take_weight , take_indices)
#                 else :
#                     return (skip_weight , skip_indx)
        


#         return dp(0,4)[1]


from bisect import bisect_left
from functools import lru_cache
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Store original index with interval data: (start, end, weight, orig_idx)
        sorted_intervals = sorted(
            [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        )
        
        # Array of start times for binary searching non-overlapping intervals
        starts = [interval[0] for interval in sorted_intervals]
        
        @lru_cache(maxsize=None)
        def dp(idx: int, count: int):
            # Base cases: out of intervals or already picked 4 intervals
            if idx >= n or count == 0:
                return (0, [])
            
            # Option 1: Skip the current interval
            skip_weight, skip_indices = dp(idx + 1, count)
            
            # Option 2: Pick the current interval
            l, r, weight, orig_idx = sorted_intervals[idx]
            
            # Find the next interval whose start time > r (strictly non-overlapping)
            next_idx = bisect_left(starts, r + 1)
            
            take_next_weight, take_next_indices = dp(next_idx, count - 1)
            take_weight = weight + take_next_weight
            
            # Insert original index sorted to keep lexicographical comparison clean
            take_indices = sorted([orig_idx] + take_next_indices)
            
            # Compare Option 1 vs Option 2
            if take_weight > skip_weight:
                return (take_weight, take_indices)
            elif take_weight < skip_weight:
                return (skip_weight, skip_indices)
            else:
                # Weights are equal: pick the lexicographically smaller index list
                if take_indices < skip_indices:
                    return (take_weight, take_indices)
                else:
                    return (skip_weight, skip_indices)
                    
        return dp(0, 4)[1]