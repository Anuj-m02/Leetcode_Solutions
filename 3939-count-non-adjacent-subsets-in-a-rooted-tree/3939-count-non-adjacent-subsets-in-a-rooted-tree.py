# # class TreeNode :
# #     def __init__(self , val):
# #         self.val = val
# #         self.par = None
# #         self.left = None
# #         self.right = None
     

# class Solution:
#     def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:

#         n = len(nums)
#         mod = int(1e9) + 7

#         graph = defaultdict(int)
#         for node in range(n):
#             par = parent[node]
#             if par != -1 :
#                 # graph[u].append(par)
#                 graph[par].append(node)
        


#         def dp(node , takes_node) :

#             res = [0]*(k)

#             if takes_node :
#                 res[nums[node] % k] = 1
            
#             else :
#                 res[0] = 1
            
#             for v in graph[node] :
#                 nxt_res = [0]*(k)

#                 if takes_node :
#                     v_dp = dp(v , False)
                
#                 else :
#                     v0 = dp(v , False)
#                     v1 = dp(v , True)
#                     v_dp = [(v0[r] + v1[r]) % mod for r in range(k)]
                

#                 for r1 in range(k) :
#                     if res[r1] :
#                         for r2 in range(k) :
#                             if v_dp[r2] :
#                                 rem = (r1+r2)%k
#                                 nxt_res[rem] = (nxt_res[rem] + res[r1] * v_dp[r2]) % mod
                

from typing import List

class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # dp0[u][r]: ways to select non-adjacent subset in u's subtree WITHOUT picking u, sum % k == r
        # dp1[u][r]: ways to select non-adjacent subset in u's subtree WITH picking u, sum % k == r
        dp0 = [[0] * k for _ in range(n)]
        dp1 = [[0] * k for _ in range(n)]

        # Base initialization for each node individually before merging children
        for i in range(n):
            dp0[i][0] = 1  # Empty set inside i's subtree (excluding i) has sum 0
            dp1[i][nums[i] % k] = 1  # Selecting only node i gives sum nums[i] % k

        # Process nodes bottom-up (since parent[i] < i, iterating n-1 down to 1 processes children first)
        for v in range(n - 1, 0, -1):
            u = parent[v]

            # Merge child v's DP results into parent u's DP results
            new_dp0 = [0] * k
            new_dp1 = [0] * k

            for r1 in range(k):
                # When u is NOT taken: child v can either be taken or not taken
                total_v_ways = (dp0[v][r1] + dp1[v][r1]) % MOD
                if total_v_ways:
                    for r2 in range(k):
                        if dp0[u][r2]:
                            rem = (r2 + r1) % k
                            new_dp0[rem] = (new_dp0[rem] + dp0[u][r2] * total_v_ways) % MOD

                # When u IS taken: child v CANNOT be taken (only dp0[v] is allowed)
                if dp0[v][r1]:
                    for r2 in range(k):
                        if dp1[u][r2]:
                            rem = (r2 + r1) % k
                            new_dp1[rem] = (new_dp1[rem] + dp1[u][r2] * dp0[v][r1]) % MOD

            dp0[u] = new_dp0
            dp1[u] = new_dp1

        # Total valid subsets with sum % k == 0 (excluding the empty set)
        ans = (dp0[0][0] + dp1[0][0] - 1) % MOD
        return ans