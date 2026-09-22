# import heapq
# from collections import defaultdict , deque

# class Solution:
#     def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        
#         n = len(costs)

#         machines = list(zip(costs, capacity))
#         machines.sort()

#         ans = 0
#         for c, cap in machines :
#             if c < budget :
#                 ans = max(ans , cap)
        

        
#         prefix = [0]*(n)
#         prefix[0] = machines[0][1]
#         for i in range(1,n):
#             prefix[i] = max(prefix[i-1],machines[i][1])

#         right = n-1

#         for left in range(1 , n):

#             if machines[left][0] >= budget :
#                 break

#             while right >= left or (right >= 0 and machines[left][0] + machines[right][0] >= budget) :
#                 right -= 1
            

#             if right >= 0 :
#                 ans = max(ans , machines[left][1] + prefix[right])

    
#         return ans
from bisect import bisect_left
from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        # Pair costs with capacities and sort by cost
        machines = sorted(zip(costs, capacity))
        sorted_costs = [c for c, _ in machines]

        ans = 0

        # Option 1: Choose at most one machine
        for c, cap in machines:
            if c < budget:
                ans = max(ans, cap)

        # Prefix maximum capacities
        prefix = [0] * n
        prefix[0] = machines[0][1]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], machines[i][1])

        # Option 2: Choose two machines
        for i in range(1, n):
            cost_i = machines[i][0]
            if cost_i >= budget:
                break
            
            # Find max index j < i such that costs[j] < budget - cost_i
            rem = budget - cost_i
            j = bisect_left(sorted_costs, rem) - 1
            
            # Ensure j < i (we only look at indices strictly before i)
            j = min(j, i - 1)
            
            if j >= 0:
                ans = max(ans, machines[i][1] + prefix[j])

        return ans