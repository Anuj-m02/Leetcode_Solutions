# class Solution:
#     def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        
#         n , m = len(matrix) , len(matrix[0])
#         ans = float("-inf")

#         # fix two columns
#         # left , right

#         for left in range(m) :
#             row_sums = [0]*(n)
#             for right in range(left , m) :

#                 for r in range(n) :
#                     row_sums[r] += matrix[r][right]
            
#                 max_kadane = float("-inf")
#                 curr_kadane = 0
#                 for val in row_sums :
#                     curr_kadane = max(val , curr_kadane+val)
#                     max_kadane = max(max_kadane , curr_kadane)

#                 if max_kadane <= k :
#                     ans = max(ans , max_kadane)
#                     if ans == k :
#                         return k
#                     continue

#                 sorted_prefix = [0]
#                 curr_prefix = 0

#                 for val in row_sums :
#                     curr_prefix += val
#                     target = curr_prefix - k

#                     indx = bisect_left(sorted_prefix , target)
#                     if indx < len(sorted_prefix) :
#                         ans = max(ans , curr_prefix - sorted_prefix[indx])
#                         if ans == k :
#                             return k

#                     insort(sorted_prefix , curr_prefix)

#         return ans  



        
        
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         ans = float("-inf")
#         m, n = len(matrix), len(matrix[0])
#         for i in range(n):
#             lstSum = [0] * m
#             for j in range(i, n):
#                 currSum = 0
#                 curlstSum = [0]
#                 for t in range(m):
#                     lstSum[t] += matrix[t][j]
#                     currSum += lstSum[t]
#                     pos = bisect_left(curlstSum, currSum - k)
#                     if pos < len(curlstSum):
#                         if curlstSum[pos] == currSum - k:
#                             return k
#                         else:
#                             ans = max(ans, currSum - curlstSum[pos])
#                     insort(curlstSum, currSum)
#         return ans


from bisect import bisect_left
from sortedcontainers import SortedSet
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')

        # Ensure we iterate over the smaller dimension for efficiency
        for left in range(n):
            rowSum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowSum[i] += matrix[i][right]

                s=SortedSet([0])
                curr = 0
                for x in rowSum:
                    curr += x
                    idx = bisect_left(s, curr - k)
                    if idx < len(s):
                        ans = max(ans, curr - s[idx])
                    s.add(curr)

        return ans