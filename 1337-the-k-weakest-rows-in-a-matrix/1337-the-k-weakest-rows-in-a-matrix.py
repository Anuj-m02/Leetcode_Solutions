# import heapq

# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
#         n , m = len(mat) , len(mat[0])

#         final = []
#         heap = []
#         ans = []
#         for row in range(n) :
#             count_1 = mat[row].count(1)
#             heapq.heappush(heap , (count_1 , row))
#             if len(heap) > n-k :
#                 cnt , indx = heapq.heappop(heap)
#                 ans.append(indx)
#             # print(heap)
#             # final.append((count_1 , row))
        
#         return ans
#         # final.sort()

#         # nlogn

#         # ans = []
#         # for i in range(k) :
#         #     ans.append(heap[i][1])
        
#         # return ans
import heapq
from typing import List


class Solution:

  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    heap = []

    for row in range(len(mat)):
      count_1 = mat[row].count(1)
      # Store negative values to invert min-heap into a max-heap
      heapq.heappush(heap, (-count_1, -row))

      if len(heap) > k:
        heapq.heappop(heap)

    # Pop remaining elements and reverse to get weakest first
    ans = []
    while heap:
      cnt, indx = heapq.heappop(heap)
      ans.append(-indx)

    return ans[::-1]