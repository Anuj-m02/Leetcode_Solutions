# # class Solution:
# #     def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        
# #         n = len(arr)

# #         @lru_cache(maxsize=None)
# #         def dp(indx , prev_indx , length) :
# #             if indx >= n :
# #                 if length > 1 and prev_indx != -1 :
# #                     return max(arr[prev_indx : n])*(length)
# #                 else :
# #                     return 0
            
# #             if length > k :
# #                 return float("-inf")
            
# #             if prev_indx == -1 :
# #                 # first partition we can or not break here
# #                 not_take = dp(indx+1 , prev_indx , length+1)
# #                 take = max(arr[0 : indx+1])*(length) + dp(indx+1 , indx+1 , 1)
# #                 return max(take , not_take)
            
# #             else :
# #                 not_take = dp(indx+1 , prev_indx , length+1)
# #                 take = max(arr[prev_indx : indx+1])*(length) + dp(indx+1 , indx+1 , 1)
# #                 return max(take , not_take)
            
        
# #         return dp(0 , -1 , 1)

# from functools import lru_cache

# class Solution:
#     def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
#         n = len(arr)

#         @lru_cache(maxsize=None)
#         def dp(indx, prev_indx, length):
#             if indx >= n:
#                 if prev_indx != -1 and length > 0:
#                     return max(arr[prev_indx : n]) * length
#                 return 0
            
#             # Since length counts the candidate element at indx, current partition would become length + 1
#             if length + 1 > k:
#                 # Must take a split here because continuing would exceed partition length k
#                 start = 0 if prev_indx == -1 else prev_indx
#                 return max(arr[start : indx + 1]) * (length + 1) + dp(indx + 1, -1, 0)
            
#             if prev_indx == -1:
#                 # first partition: start active partition at indx
#                 not_take = dp(indx + 1, indx, 1)
#                 take = arr[indx] + dp(indx + 1, -1, 0)
#                 return max(take, not_take)
#             else:
#                 not_take = dp(indx + 1, prev_indx, length + 1)
#                 take = max(arr[prev_indx : indx + 1]) * (length + 1) + dp(indx + 1, -1, 0)
#                 return max(take, not_take)
            
#         return dp(0, -1, 0)

class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)

        @lru_cache(maxsize=None)
        def dp(i):
            if i == n:
                return 0
            
            max_val = 0
            ans = 0
            for j in range(i, min(n, i + k)):
                max_val = max(max_val, arr[j])
                ans = max(ans, max_val * (j - i + 1) + dp(j + 1))
            return ans

        return dp(0)