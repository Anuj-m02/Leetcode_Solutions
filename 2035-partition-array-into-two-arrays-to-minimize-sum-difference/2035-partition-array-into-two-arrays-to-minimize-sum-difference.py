# class Solution:
#     def minimumDifference(self, arr: List[int]) -> int:
#         n = len(arr)
#         totSum = sum(arr)

#     # Initialize a DP table to store subset sum information.
#         dp = [[False for i in range(totSum + 1)] for j in range(n)]

#     # Initialize the base cases for the DP table.
#         for i in range(n):
#             dp[i][0] = True

#     # Handle the base case for the first element in the array.
#         if arr[0] <= totSum:
#             dp[0][arr[0]] = True

#     # Fill in the DP table using dynamic programming.
#         for ind in range(1, n):
#             for target in range(1, totSum + 1):
#             # If the current element is not taken, the result is the same as the previous row.
#                 notTaken = dp[ind - 1][target]

#             # If the current element is taken, subtract its value from the target and check the previous row.
#                 taken = False
#                 if arr[ind] <= target:
#                     taken = dp[ind - 1][target - arr[ind]]

#             # Update the DP table with the result of taking or not taking the current element.
#                 dp[ind][target] = notTaken or taken

#     # Initialize a variable to track the minimum absolute difference.
#         mini = int(1e9)

#     # Iterate through all possible sums.
#         for i in range(totSum + 1):
#             if dp[n - 1][i] == True:
#                 # Calculate the difference between the current sum and the complement sum.
#                 diff = abs(i - (totSum - i))
#                 mini = min(mini, diff)

#         return mini


from functools import lru_cache
from bisect import bisect_left
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 2
        totSum = sum(nums)
        target = totSum / 2
        
        left_arr = nums[:N]
        right_arr = nums[N:]
        
        # Memoized DFS to collect unique sums for choosing 'count' elements from array 'arr'
        def get_sums(arr):
            sums = [set() for _ in range(N + 1)]
            
            @lru_cache(None)
            def dfs(idx, count, current_sum):
                if idx == N:
                    sums[count].add(current_sum)
                    return
                # Option 1: Do not pick arr[idx]
                dfs(idx + 1, count, current_sum)
                # Option 2: Pick arr[idx]
                dfs(idx + 1, count + 1, current_sum + arr[idx])
                
            dfs(0, 0, 0)
            return [sorted(list(s)) for s in sums]
        
        left_sums = get_sums(left_arr)
        right_sums = get_sums(right_arr)
        
        ans = float('inf')
        
        # Pick k elements from left, N - k from right
        for k in range(N + 1):
            r_sz = N - k
            r_list = right_sums[r_sz]
            
            for l_sum in left_sums[k]:
                # We want l_sum + r_sum close to target
                idx = bisect_left(r_list, target - l_sum)
                
                if idx < len(r_list):
                    r_sum = r_list[idx]
                    ans = min(ans, abs(totSum - 2 * (l_sum + r_sum)))
                if idx > 0:
                    r_sum = r_list[idx - 1]
                    ans = min(ans, abs(totSum - 2 * (l_sum + r_sum)))
                    
        return ans